__author__ = "Shane Drabing"
__license__ = "MIT"
__email__ = "shane.drabing@gmail.com"


# IMPORTS


import csv
import re
import urllib
import xml.etree.ElementTree

import requests


# CONSTANTS


FORMAT_EUTILS = (
    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/{}.cgi"
).format

FORMAT_MITOCHONDRIA = (
    '({}[Organism]) AND ' +
    'mitochondrion[filter] AND ' +
    '("15000"[SLEN] : "25000"[SLEN])'
).format


# FUNCTIONS (GENERAL)


def title(x):
    return x[0].upper() + x[1:]


def get(key):
    def getf(itr):
        return itr[key]
    return getf


# FUNCTIONS (XML)


def parse_docsum(docsum):
    return {
        tag.attrib["Name"].lower().replace("version", str()): tag.text
        for tag in docsum
        if tag.tag == "Item"
    }


def parse_xml(xml):
    return tuple(map(parse_docsum, xml))


def filter_xml(xml):
    tup = parse_xml(xml)

    filt = (
        dct for dct in tup
        if not dct["caption"].startswith("X")
        and dct["status"] == "live"
    )

    srt = sorted(filt, key=get("createdate"), reverse=True)

    out = dict()
    for dct in srt:
        if dct["taxid"] in out:
            continue
        out[dct["taxid"]] = dct
    return out


# FUNCTIONS (FASTA)


def fasta_columns(x, nchar=70):
    raw = str().join(x.strip().split())
    return "\n".join(
        raw[i:i + nchar]
        for i in range(0, len(raw), nchar)
    )


def read_fasta(filename):
    with open(filename) as f:
        dct = dict()
        for line in map(str.strip, f):
            if line.startswith(">"):
                dct[(key := line.lstrip(">"))] = str()
            elif key in dct:
                dct[key] += line
    return dct


def write_fasta(filename, dct):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n\n".join(
            ">{}\n{}".format(k, fasta_columns(v))
            for k, v in dct.items()
        ) + "\n")


# FUNCTIONS (DATA MANIPULATION)


def append_fullnames(dct):
    taxa = esummary_taxonomy_json(dct)
    for k, v in taxa["result"].items():
        if not "taxid" in v:
            continue

        if v["commonname"]:
            spcomm = map(title, (v["scientificname"], v["commonname"]))
            dct[k]["fullname"] = "{} ({})".format(*spcomm)
        else:
            dct[k]["fullname"] = title(v["scientificname"])


def append_reads(dct):
    ids = map(get("accession"), dct.values())
    fasta = efetch_fasta(ids)
    tmp = {v["accession"]: k for k, v in dct.items()}
    lst = fasta.split("\n\n")
    for x in lst:
        title, read = x.split("\n", maxsplit=1)
        accession = title.split(maxsplit=1)[0].lstrip(">")
        dct[tmp[accession]]["read"] = read


def download_taxa_mtdna(term, filename=None):
    res = esearch_mtdna_json(term)
    ids = res["esearchresult"]["idlist"]
    xml = esummary_nucleotide_xml(ids)
    dct = filter_xml(xml)

    append_fullnames(dct)
    append_reads(dct)

    if isinstance(filename, str):
        tmp = {
            "{} {}".format(v["accession"], v["fullname"]): v["read"]
            for v in dct.values()
        }
        write_fasta(filename, tmp)
    return dct


# FUNCTIONS (EUTILS)


def eutils(cgi, **options):
    url = FORMAT_EUTILS(cgi)
    return requests.post(url, data=options)


def efetch_fasta(itr):
    ids = ",".join(map(str, itr))
    resp = eutils("efetch", db="nuccore", rettype="fasta", id=ids)
    if resp.status_code != 200:
        return
    return resp.content.decode("utf-8").strip()


def esearch_json(term):
    resp = eutils("esearch", db="nucleotide",
                  retmode="json", retmax=99999, term=term)
    if resp.status_code != 200:
        return
    return resp.json()


def esearch_mtdna_json(taxon):
    return esearch_json(FORMAT_MITOCHONDRIA(taxon))


def esummary_taxonomy_json(itr):
    ids = ",".join(map(str, itr))
    resp = eutils("esummary", db="taxonomy", retmode="json", id=ids)
    if resp.status_code != 200:
        return
    return resp.json()


def esummary_nucleotide_xml(itr):
    ids = ",".join(map(str, itr))
    resp = eutils("esummary", db="nucleotide", id=ids)
    if resp.status_code != 200:
        return
    return xml.etree.ElementTree.fromstring(resp.text)


# SCRIPT


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("term", help="Search term.", type=str)
    parser.add_argument("fout", help="Output filepath.", type=str)
    args = parser.parse_args()

    download_taxa_mtdna(args.term, filename=args.fout)

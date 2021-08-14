__author__ = "Shane Drabing"
__license__ = "MIT"
__email__ = "shane.drabing@gmail.com"


# IMPORTS


import subprocess
import sys
import time


# GLOBALS


TIME = None


# CONSTANTS


WINDOWS = str(sys.platform) in ("win32", "cygwin")


# FUNCTIONS


def tick(message=str(), pad=32):
    global TIME
    start = TIME
    TIME = time.monotonic()
    if start is None:
        return
    if message:
        print(message.rjust(pad) + ": %.1f sec" % (TIME - start))
    else:
        print("%.6f" % (TIME - start))


def system(name, command, label):
    code = subprocess.run(
        command.split(),
        stderr=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL
    )
    if code.returncode != 0:
        print((f'"{name}" ' + label).rjust(32) + ": Oops!")
        exit(code.returncode)
    tick(f'"{name}" ' + label)


# SCRIPT


if __name__ == "__main__":
    import argparse
    import os
    import sys

    # where am I?
    here = sys.path[0]

    # setup args
    parser = argparse.ArgumentParser()
    parser.add_argument("term", help="Search term.", type=str)

    # parse args
    args = parser.parse_args()
    term = args.term.strip()
    name = "_".join(term.lower().split())

    # make relative output directory
    if not os.path.exists("./out"):
        os.makedirs("./out")

    # run
    tick()
    start = time.monotonic()
    
    system(
        term,
        f"python{'3' if not WINDOWS else str()} " +
        f"{here}/../src/ncbi_eutils.py " +
        f"{term} " +
        f"./out/mtdna_{name}.fasta",
        "search"
    )

    system(
        term,
        f"{here}/../bin/trim_region{'.exe' if WINDOWS else str()} " +
        f"{here}/../data/latrans_cr.fasta " +
        f"./out/mtdna_{name}.fasta " +
        f"./out/mtdnacr_{name}.fasta ",
        "prune"
    )

    system(
        term,
        f"{here}/../bin/calc_dist{'.exe' if WINDOWS else str()} " +
        f"./out/mtdnacr_{name}.fasta " +
        f"./out/score_{name}.csv",
        "score"
    )

    system(
        term,
        f"python{'3' if not WINDOWS else str()} " +
        f"{here}/../src/calc_tree.py " +
        f"./out/score_{name}.csv " +
        f"./out/tree_{name}.txt",
        "build"
    )

    end = time.monotonic()
    print(f'"{term}" done'.rjust(32) + ": %.1f sec" % (end - start))

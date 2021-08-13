#include <iostream>
#include <algorithm>
#include <fstream>

#include "dna_alignment.h"
#include "utils_fasta.h"

using std::cout;
using std::endl;
using std::reverse;
using std::ofstream;

int main(int argc, char *argv[]) {
    vector<pair<string, string>> data;
    string mtdna, cr, new_cr;   
    size_t i, n;
    ofstream fout;

    if (argc != 4) {
        cout << "incorrect number of arguments" << endl;
        return 1;
    }

    n = 70;
    data = read_fasta(argv[1]);
    cr = data[0].second;
    data = read_fasta(argv[2]);
    fout = ofstream(argv[3]);

    for (const auto& pair : data) {
        new_cr = local_align_trace(cr.c_str(), pair.second.c_str());
        std::reverse(new_cr.begin(), new_cr.end());
        fout << ">" << pair.first << endl;

        i = 0;
        while (i < new_cr.size()) {
            fout << new_cr.substr(i, n) << endl;
            i += n;
        }
        fout << endl;
    }

    fout.close();
    return 0;
}

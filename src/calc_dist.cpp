#include <iostream>
#include <fstream>

#include "dna_alignment.h"
#include "utils_fasta.h"

using std::cout;
using std::endl;
using std::ofstream;

int main(int argc, char *argv[]) {
    vector<pair<string, string>> data;
    pair<string, string> x, y;
    const char *x_str, *y_str;
    size_t i, j, n;
    ofstream fout;

    if (argc != 3) {
        cout << "Incorrect number of arguments" << endl;
        return 1;
    }

    data = read_fasta(argv[1]);
    fout = ofstream(argv[2]);

    if (!fout.is_open()) {
        cout << "File error!" << endl;
        return 1;
    } else {
        fout << "V1,V2,p" << endl;
    }

    n = data.size();
    for (i = 0; i < n; ++i) {
        x = data[i];
    
        for (j = i + 1; j < n; ++j) {
            y = data[j];

            fout << '"' << x.first << "\",\""
                 << y.first << "\","
                 << global_align_score(x.second.c_str(), y.second.c_str(), -1)
                 << endl;
        }
    }

    fout.close();
    return 0;
}

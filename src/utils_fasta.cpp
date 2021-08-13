#include <fstream>
#include "utils_fasta.h"

using std::ifstream;

vector<pair<string, string>> read_fasta(string filename) {
    vector<pair<string, string>> data;
    pair<string, string> item;
    string k, v;

    ifstream input(filename);
    for (string line; getline(input, line);) {
        if (line.rfind(">", 0) == 0) {
            if (k.size() && v.size()) {
                item = pair<string, string>(k, v);
                data.push_back(item);
            }
            k = line.substr(1);
            v = string();
        } else {
            v.append(line);
        }
    }
    if (k.size() && v.size()) {
        item = pair<string, string>(k, v);
        data.push_back(item);
    }

    return data;
}

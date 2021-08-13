// author:  Shane Drabing
// license: MIT
// email:   shane.drabing@gmail.com


#ifndef UTILS_FASTA_H
#define UTILS_FASTA_H

#include <string>
#include <vector>

using std::string;
using std::vector;
using std::pair;

vector<pair<string, string>> read_fasta(string filename);

#endif // UTILS_FASTA_H

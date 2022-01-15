#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <set>
#include <unordered_map>
#include <cstdio>

typedef std::vector <uint64_t> IntVector;
typedef std::unordered_map <std::string, IntVector> Clustering;
typedef std::vector <std::pair <uint64_t, Clustering>> ClusteringVector;

typedef std::pair <uint64_t, uint64_t> IntPair;
typedef std::set <IntPair> ClusteringPairs;
typedef std::vector <ClusteringPairs> ClusteringPairsVector;

typedef std::vector <std::string> StringVector;


std::pair <uint64_t, Clustering> parseTSV(std::istream &inFile) {
    Clustering clustering;

    std::string line;
    if ((char) inFile.peek() == '#') getline(inFile, line);

    uint64_t index = 0;
    std::string sample = "";

    while (inFile.good()) {
        getline(inFile, line);
        if (line.empty()) break;

        StringVector s;
        std::stringstream ss(line);
        std::string val;
        while (ss >> val) {
            s.push_back(val);
        }

        if (index == 0) {
            sample = s[3];
        }

        if (s[3] == sample) {
            clustering[s.back()].push_back(index);
        }
        ++index;
    }

    return std::make_pair(index, clustering);
}

ClusteringPairs makePairs(const Clustering &clustering) {
    ClusteringPairs pairs;

    for (const auto &kv: clustering) {
        for (auto it1 = kv.second.begin(); it1 != kv.second.end(); ++it1) {
            for (auto it2 = it1 + 1; it2 != kv.second.end(); ++it2) {
                pairs.insert(std::make_pair(*it1, *it2));
            }
        }
    }

    return pairs;
}

void performComparison(const uint64_t n,
                       const ClusteringPairs &GT, const ClusteringPairs &inferred,
                       uint64_t &TP, uint64_t &TN, uint64_t &FN, uint64_t &FP) {
    std::set <std::pair<uint64_t, uint64_t>> S;

    std::set_difference(GT.begin(), GT.end(),
                        inferred.begin(), inferred.end(),
                        std::inserter(S, S.begin()));
    FN = S.size();

    S.clear();

    std::set_difference(inferred.begin(), inferred.end(),
                        GT.begin(), GT.end(),
                        std::inserter(S, S.begin()));
    FP = S.size();

    S.clear();

    std::set_intersection(GT.begin(), GT.end(),
                          inferred.begin(), inferred.end(),
                          std::inserter(S, S.begin()));
    TP = S.size();

    TN = n * (n - 1) / 2 - FN - FP - TP;
}

int main(int argc, char **argv) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <GT.tsv> <INFERRED_1.tsv> ... <INFERRED_K.tsv>" << std::endl;
        return 1;
    }

    ClusteringVector clusteringVector;
    for (int i = 1; i < argc; ++i) {
        std::ifstream inFile(argv[i]);
        if (!inFile.good()) {
            std::cerr << "Error: could not open '" << argv[i] << "' for reading" << std::endl;
            return 1;
        }

        std::cout << "Parsing " << argv[i] << " (" << (i == 1 ? "GT" : "inferred") << ")... " << std::flush;
        clusteringVector.emplace_back(parseTSV(inFile));
        std::cout << "Done! Parsed " << clusteringVector.back().first << " bins." << std::endl;
        std::cout << "Cluster\tBins" << std::endl;
        for (const auto &kv: clusteringVector.back().second) {
            std::cout << kv.first << "\t" << kv.second.size() << std::endl;
        }
        std::cout << std::endl;
    }

    for (int i = 2; i < argc; ++i) {
        if (clusteringVector[i-1].first != clusteringVector[0].first) {
            std::cerr << "Error: different number of bins." << std::endl;
            return 1;
        }
    }

    ClusteringPairsVector clusteringPairsVector;
    for (int i = 1; i < argc; ++i) {
        std::cout << "Making pairs for " << argv[i] << " (" << (i == 1 ? "GT" : "inferred") << ")..." << std::flush;
        clusteringPairsVector.emplace_back(makePairs(clusteringVector[i-1].second));
        std::cout << " Done! Identified " << clusteringPairsVector.back().size() << " pairs." << std::endl;

        std::cout << std::endl;
    }

    for (int i = 2; i < argc; ++i) {
        std::cout << "Performing comparison between " << argv[1] << " (GT) and " << argv[i] << " (inferred)..." << std::flush;
        uint64_t TP, TN, FN, FP;
        performComparison(clusteringVector[0].first, clusteringPairsVector[0], clusteringPairsVector[i-1], TP, TN, FN, FP);
        std::cout << " Done!" << std::endl;
        std::cout << "TP: " << TP << std::endl;
        std::cout << "TN: " << TN << std::endl;
        std::cout << "FN: " << FN << std::endl;
        std::cout << "FP: " << FP << std::endl;

        std::cout << std::endl;

        std::cout << "Recall: " << (double) TP / (double) (TP + FN) << std::endl;
        std::cout << "Precision: " << (double) TP / (double) (TP + FP) << std::endl;
        std::cout << "Rand index: " << (double) (TP + TN) / (double) (TP + FN + FP + TN) << std::endl;
        std::cout << "Adjusted Rand index: " << 2.0 * (TP * TN - FN * FP) / (double) ((TP + FN) * (FN + TN) + (TP + FP) * (FP + TN)) << std::endl;

        std::cout << std::endl;
    }

    return 0;
}
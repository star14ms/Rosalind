#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <Bpp/Phyl/Io/Newick.h>
#include <Bpp/Phyl/Tree/TreeTemplate.h>
#include <Bpp/Phyl/Tree/TreeTemplateTools.h>
// https://github.com/BioPP/bpp-documentation/wiki/Installation

using namespace bpp;
using namespace std;

// Utility function to calculate binomial coefficient
long long binomial_coeff(int n, int k) {
    long long result = 1;
    if (k > n - k) k = n - k;
    for (int i = 0; i < k; ++i) {
        result *= (n - i);
        result /= (i + 1);
    }
    return result;
}

// Function to get terminals
set<string> get_terminals(const TreeTemplate<Node>& tree, int nodeId) {
    set<string> terminals;
    vector<int> leavesIds;
    TreeTemplateTools::getLeavesId(tree.getNode(nodeId), leavesIds);
    for (int id : leavesIds) {
        terminals.insert(tree.getNodeName(id));
    }
    return terminals;
}

long long get_n_common_quartets_from_two_edges(const Node* edge1, const Node* edge2, const TreeTemplate<Node>& tree1, const TreeTemplate<Node>& tree2) {
    auto F1 = get_terminals(tree1, edge1->getId());
    auto G1 = get_terminals(tree2, edge2->getId());
    if (F1.size() < 2 || G1.size() < 2) return 0;

    auto F2 = get_terminals(edge1.clade[0]);  // Simplified access, real usage may differ
    auto G2 = get_terminals(edge2.clade[0]);
    auto F3 = get_terminals(edge1.clade[1]);
    auto G3 = get_terminals(edge2.clade[1]);

    long long n_common_quartets = binomial_coeff(F1.size(), 2) * (F2.size() * G2.size() + F3.size() * G3.size());
    return n_common_quartets;
}

int main() {
    Newick reader;
    TreeTemplate<Node>* tree1 = reader.read("path_to_tree1.newick");
    TreeTemplate<Node>* tree2 = reader.read("path_to_tree2.newick");

    long long n_common_quartets = 0;
    // Implement the logic to compare tree nodes
    cout << "Number of common quartets: " << n_common_quartets << endl;

    delete tree1;
    delete tree2;
    return 0;
}

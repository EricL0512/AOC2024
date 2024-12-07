#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

int main() {
    ifstream file("input");
    if (!file.is_open()) {
        cerr << "Unable to open file" << endl;
        return 1;
    }
    int total;
    vector<int> left;
    vector<int> right;
    string line;
    // This is such a terrible way to split data but it works
    while (getline(file, line)) {
        int tmp;
        istringstream stream(line);
        bool first = true;
        while (stream >> tmp) {
            if (first) left.push_back(tmp);
            if (!first) right.push_back(tmp);
            first = !first;
        }
    }
    sort(left.begin(), left.end());
    sort(right.begin(), right.end());
    for (int i = 0; i < left.size(); i++) total += abs(left.at(i) - right.at(i));
    cout << "part one: " << total << endl;
    // whether vector is sorted or not doesn't matter; just use sorted vector
    total = 0;
    // nested for loop. takes an element from left, checks repeats on right, multiply repeat and left element and add to total
    for (int i : left) {
        total += i * count(right.begin(), right.end(), i);
    }
    cout << "part two: " << total;
    file.close();
    return 0;
}

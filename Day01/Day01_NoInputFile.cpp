// this file is for manually copy + pasting inputs into terminal
// change lines to represent the total amount of lines in your input
#include <bits/stdc++.h>
using namespace std;

int main() {
	int lines = 1000;
	int l, r, total;
	vector<int> left;
	vector<int> right;
	for (int i = 0; i < lines; i++) {
		cin >> l >> r;
		left.push_back(l);
		right.push_back(r);
	}
	sort(left.begin(), left.end());
	sort(right.begin(), right.end());
	for (int i = 0; i < left.size(); i++) total += abs(left[i] - right[i]);
	cout << "part one: " <<total << endl;
	total = 0;
	for (int i : left) total += i * count(right.begin(), right.end(), i);
	cout << "part two: " << total;
}

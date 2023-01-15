#include <iostream>
#include <vector>
using namespace std;

void findCombinations(vector<int>& candidates, vector<vector<int>>& combinations, vector<int>& current, int target, int start) {
    if (target == 0) {
        combinations.push_back(current);
        return;
    }
    for (int i = start; i < candidates.size(); i++) {
        if (target < candidates[i]) {
            continue;
        }
        current.push_back(candidates[i]);
        findCombinations(candidates, combinations, current, target - candidates[i], i);
        current.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> combinations;
    vector<int> current;
    findCombinations(candidates, combinations, current, target, 0);
    return combinations;
}

int main() {
    vector<int> candidates = {2, 3, 6, 7};
    int target = 7;
    vector<vector<int>> combinations = combinationSum(candidates, target);
    for (int i = 0; i < combinations.size(); i++) {
        for (int j = 0; j < combinations[i].size(); j++) {
            cout << combinations[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
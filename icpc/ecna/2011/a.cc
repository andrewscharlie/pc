// http://acm.ashland.edu/2011/Problem-Set/Problems/2011.pdf
#include <string>
#include <vector>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <numeric>
#include <functional>
#include <limits.h>

typedef long long LL;
using namespace std;

// disables = max heap
// enables = min heap
LL calculateCost(vector<int> disables, vector<int> enables, LL constantCost) {
  LL cost = constantCost * (disables.size() + enables.size());

  int i = 0;
  while (!disables.empty()) {
    cost += disables.front() * i++;
    pop_heap(disables.begin(), disables.end());
    disables.pop_back();
  }

  i = enables.size();
  while (!enables.empty()) {
    cost += enables.front() * i--;
    pop_heap(enables.begin(), enables.end(), greater<int>());
    enables.pop_back();
  }

  return cost;
}

LL solve(string src, string dst, vector<int> costs) {
  vector<int> disables, enables, unknowns;
  
  for (int i = 0; i < src.length(); ++i) {
    if (src[i] == '1' && dst[i] == '0') {
      // It's on and must go off. We'll definitely need to disable these at some point
      disables.push_back(costs[i]);
      push_heap(disables.begin(), disables.end());
    } else if (src[i] == '0' && dst[i] == '1') {
      // It's off and must go on. We'll definitely need to enable these at some point
      enables.push_back(costs[i]);
      push_heap(enables.begin(), enables.end(), greater<int>());
    } else if (src[i] == '1' && dst[i] == '1') {
      // It's on and stays on. We may need to disable these in the interim to
      // save on landing costs
      unknowns.push_back(costs[i]);
      push_heap(unknowns.begin(), unknowns.end());
    }
  }

  LL constantCost = accumulate(unknowns.begin(), unknowns.end(), 0);
  LL lowestCost = calculateCost(disables, enables, constantCost);

  while (!unknowns.empty()) {
    int highestUnknown = unknowns.front();
    pop_heap(unknowns.begin(), unknowns.end());
    unknowns.pop_back();

    // Mark it as necessary to both disable and enable
    disables.push_back(highestUnknown);
    push_heap(disables.begin(), disables.end());    

    enables.push_back(highestUnknown);
    push_heap(enables.begin(), enables.end(), greater<int>());

    constantCost = accumulate(unknowns.begin(), unknowns.end(), 0);
    LL currentCost = calculateCost(disables, enables, constantCost);

    if (currentCost < lowestCost) {
      lowestCost = currentCost;
    } else {
      break;
    }
  }

  return lowestCost;
}

int main() {
  int caseNo = 1, length;

  cin >> length;
  while (length != 0) {
    string src, dst;
    cin >> src >> dst;
    vector<int> costs(src.length());

    for(int i = 0; i < src.length(); ++i) {
      scanf("%i", &costs[i]);
    }
    
    printf("Case %i: %lld\n", caseNo++, solve(src, dst, costs));
    cin >> length;
  }
  
  return 0;
}

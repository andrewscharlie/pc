#include <cstdio>
#include <set>
#include <string>
#include <numeric>
#include "../../../common/strings.h"

using namespace std;

multiset<int> weights;

string solve() {
  // Replace this with common 2d array func
  int weightSum = accumulate(weights.begin(), weights.end(), 0);
  int **dpTable = new int*[weightSum];

  for (int i = 0; i < weightSum; ++i) {
    dpTable[i] = new int[weights.size()];
  }

  return toString(weights);
}

int main() {
  int cc = 1;

  for (;;) {
    int weightCount, quota;
    scanf("%i %i", &weightCount, &quota);
    if (weightCount == 0) break;

    for (int i = 0; i < weightCount; ++i) {
      int weight, membersWithWeight;
      scanf("%i %i", &weight, &membersWithWeight);

      for (int j = 0; j < membersWithWeight; ++j) {
        weights.insert(weight);
      }
    }

    printf("Case %i: %s\n", cc++, solve().c_str());
  }
}

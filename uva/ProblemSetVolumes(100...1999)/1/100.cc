#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int getCycleLength(int n) {
  int length = 1;

  while (n != 1) {
    n = (n % 2) ? (3 * n + 1) : (n / 2);
    ++length;
  }

  return length;
}

int solve(int start, int end) {
  int currentMax = 0;

  if (start > end)
    swap(start, end);
  
  for (int i = start; i <= end; ++i) {
    currentMax = max(currentMax, getCycleLength(i));
  }
  
  return currentMax;
}

int main() {
  int i, j;

  while(scanf("%d %d", &i, &j) != EOF) {
    printf("%i %i %i\n", i, j, solve(i, j));
  }

  return 0;
}

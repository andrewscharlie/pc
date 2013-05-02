#include <cstdio>
#include <math.h>

int a, b;

// n * (n + 1) / 2
bool isTriangular(int i) {
  int root = floor(sqrt(double(i) * 2));
  return ((root * (root + 1)) == (i * 2));
}

int solve() {
  int resultCount = 0;

  // Check only the perfect squares in our range
  int startRoot = ceil(sqrt(a + 1));
  int endRoot = floor(sqrt(b - 1));

  for (int i = startRoot; i <= endRoot; ++i) {
    int square = i * i;
    if (isTriangular(square - 1)) {
      ++resultCount;
    }
  }
  
  return resultCount;;
}

int main() {
  for (int cc = 1;; ++cc) {
    scanf("%i %i", &a, &b);
    if (a == 0 && b == 0) break;
    
    printf("Case %i: %i\n", cc, solve());
  }
}

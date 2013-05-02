// http://acm.ashland.edu/2011/Problem-Set/Problems/2011.pdf
#include <cstdio>

using namespace std;

// n = number of prongs/links to move by
void moveChain(int n, int s, int c, int *p, int *l, int *moveCounter) {
  (*l) = ((*l) + n) % c;
  (*p) = ((*p) + n) % s;
  (*moveCounter) += n;
}

int solve(int s, int c, int p, int l) {
  int moveCounter = 0;

  // Move the broken prong to position 0
  moveChain((s - p), s, c, &p, &l, &moveCounter);

  int i = 0;
  while (!(p == 0 && l == 0)) {
    // Move sprocket forward one rotation
    moveChain(s, s, c, &p, &l, &moveCounter);

    // There are only c possible values that l can hold, including 0.
    // That means that if we've moved the sprocket forward c times and
    // they still haven't aligned, it's had a duplicate value at least
    // once.  This means that we're in a cycle, and the broken
    // components will never line up.
    if (i++ > c) {
      return -1;
    }
  }

  return moveCounter;;
}

int main() {
  int s, c, p, l, cc = 1;

  for (;;) {
    scanf("%i %i %i %i", &s, &c, &p, &l);
    if (s == 0) break;
    
    int result = solve(s, c, p, l);
    
    if (result != -1) {
      printf("Case %i: %i %i/%i\n", cc++,
	     result / s,
	     result % s,
	     s);
    } else {
      printf("Case %i: Never\n", cc++);
    }

  }
  
  return 0;
}

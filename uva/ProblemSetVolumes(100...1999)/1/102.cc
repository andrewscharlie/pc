#include <cstdio>
#include <limits.h>
#include <algorithm>
#include <string>

using namespace std;

string GetOrderingString(int colors[]) {
  char charColors[] = {'B', 'G', 'C'};
  string ordering;

  for(int i = 0; i < 3; ++i) {
    ordering += charColors[colors[i]];
  }
  
  return ordering;
}

int main() {
  int bins[3][3];
  
  while (scanf("%i %i %i %i %i %i %i %i %i",
	       &bins[0][0], &bins[0][1], &bins[0][2],
	       &bins[1][0], &bins[1][1], &bins[1][2],
	       &bins[2][0], &bins[2][1], &bins[2][2]) != EOF) {
    int lowestMoveCount = INT_MAX;
    string ordering;

    int colors[] = {0, 1, 2};
    sort(colors, colors+3);

    do {
      int moveCount = 0;
      
      for (int bin = 0; bin < 3; ++bin) {
	// Determine which color we're keeping in the current bin
	int colorToKeep = colors[bin];
	
	for (int color = 0; color < 3; ++color) {
	  // Determine how many moves it'll take to move the others out
	  if (color != colorToKeep) {
	    moveCount += bins[bin][color];
	  }
	}
      }

      if (moveCount < lowestMoveCount) {
	lowestMoveCount = moveCount;
	ordering = GetOrderingString(colors);
      } else if (moveCount == lowestMoveCount) {
	if (GetOrderingString(colors) < ordering) {
	  lowestMoveCount = moveCount;
	  ordering = GetOrderingString(colors);
	}
      } 
    } while (next_permutation(colors, colors+3));

    printf("%s %i\n", ordering.c_str(), lowestMoveCount);
  }
}

// http://acm.ashland.edu/2011/Problem-Set/Problems/2011.pdf
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

// ballot[i] indicates the order that candidate i was chosen in the ballot
typedef vector<int> Ballot;

int b; // number of ballots
int c; // number of candidates
vector<Ballot> ballots; 

int determineWinner(int a, int b) {
  int majority = ballots.size() / 2 + 1, aVotes = 0, bVotes = 0;

  for (int i = 0; i < ballots.size(); ++i) {
    if (ballots[i][a] < ballots[i][b])
      ++aVotes;
    else
      ++bVotes;

    if (aVotes > majority || bVotes > majority)
      break;
  }

  if (aVotes > bVotes)
    return a;
  else
    return b;
}
  
int solve() {
  int winner = 0;

  for (int i = 1; i < c; ++i)
    winner = determineWinner(winner, i);

  // Check winner against all candidates that came before him
  for (int i = 0; i < winner; ++i)
    if (determineWinner(winner, i) != winner)
      return -1;

  return winner;
}

int main() {
  int cc = 1;

  for (;;) {
    scanf("%i %i", &b, &c);
    if (b == 0) break;

    int vote;n
    for(int i = 0; i < b; ++i) {
      Ballot ballot(c);
      
      for(int j = 0; j < c; ++j) {
    	scanf("%i", &vote);
	ballot[vote] = j;
      }
      
      ballots.push_back(ballot);
    }
    
    int result = solve();
    if (result >= 0)
      printf("Case %i: %i\n", cc++, result);
    else 
      printf("Case %i: No Condorcet winner\n", cc++);

    ballots.clear();
  }
}

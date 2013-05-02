// http://acm.ashland.edu/2011/Problem-Set/Problems/2011.pdf
// CURRENTLY INCORRECT
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
typedef vector<int> Ballot;

int b, c;
vector<Ballot> ballots;

bool candidateLessThan(const int &a, const int &b) {
  int majority = ballots.size() / 2 + 1, aVotes = 0, bVotes = 0;
  
  for (int i = 0; i < ballots.size(); ++i) {
    for (int j = 0; j < ballots[i].size(); ++j) {
      if (ballots[i][j] == a) {
	++aVotes;
	break;
      }
      if (ballots[i][j] == b) {
	++bVotes;
	break;
      }
    }

    if (aVotes == majority || bVotes == majority) {
      return aVotes < bVotes;
    }
  }

  // The two received equal votes
  return false;
}
  
int solve() {
  vector<int> candidates;
  while (candidates.size() < c) {
    candidates.push_back(candidates.size());
  }

  // Create a max heap from the candidates. This uses minimax to
  // calculate the top-most item on the heap
  make_heap(candidates.begin(), candidates.end(), candidateLessThan);

  // Get the possible winner
  int winner = candidates.front();
  pop_heap(candidates.begin(), candidates.end(), candidateLessThan);
  candidates.pop_back();

  // Make sure some other candidate didn't beat this one
  for (int i = 0; i < candidates.size(); ++i) {
    if (candidateLessThan(winner, candidates[i]))
      return -1;
  }
  
  return winner;
}

int main() {
  int cc = 1;

  for (;;) {
    scanf("%i %i", &b, &c);
    if (b == 0) break;

    int vote;
    for(int i = 0; i < b; ++i) {
      Ballot ballot;

      for(int j = 0; j < c; ++j) {
    	scanf("%i", &vote);
    	ballot.push_back(vote);
      }
      
      ballots.push_back(ballot);
    }
    
    int result = solve();

    if (result >= 0) {
      printf("Case %i: %i\n", cc++, result);
    } else {
      printf("Case %i: No Condorcet winner\n", cc++);
    }

    ballots.clear();
  }
}

#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

const int NUMVOTERS = 500;
const int NUMCAND = 2500;

short ballots[NUMVOTERS][NUMCAND];

int oneOnOne(int c1, int c2, int nvotes, int ncand)
{
	int v1=0, v2=0;
	for(int i=0; i<nvotes; i++) {
		if (ballots[i][c1] < ballots[i][c2])
			v1++;
		else
			v2++;
	}
//cout << c1 << ":" << v1 << ", " << c2 << ":" << v2 << endl;
	if (v1>v2)
		return c1;
	else 
		return c2;
}

int findCondorcet(int nvotes, int ncand)
{
	int c, currWinner = 0;
	for(c=1; c<ncand; c++)
		currWinner = oneOnOne(currWinner, c, nvotes, ncand);
	for(c=0; c<currWinner; c++)
		if (oneOnOne(currWinner, c, nvotes, ncand) != currWinner)
			return -1;
	return currWinner;
}

int findCondorcetDumb(int nvotes, int ncand)
{
	int c1, c2;
	for(c1=0; c1<ncand; c1++) {
		int count = 0;
		for(c2=0; c2<ncand; c2++) {
			if (c1 != c2) {
				if (oneOnOne(c1, c2, nvotes, ncand) == c1)
					count++;
				else
					break;
			}
		}
		if (count == ncand-1)
			return c1;
	}
	return -1;
}

int main()
{

	int i, j, nvotes, ncands;
	int icase = 0;

	srand(time(0));
	cin >> nvotes >> ncands;

	while (nvotes != 0) {
		icase++;
		for(i=0; i<nvotes; i++) {
			for(j=0; j<ncands; j++)  {
				int val;
				cin >> val;
				ballots[i][val] = j;
			}
		}
		int win = findCondorcet(nvotes, ncands);
		cout << "Case " << icase << ": ";
		if (win != -1)
			cout << win << endl;
		else
			cout << "No Condorcet winner" << endl;
		cin >> nvotes >> ncands;
	}
}

#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <vector>

using namespace std;

typedef vector<int> Stack;

void PrintStacks(vector<Stack> stacks) {
  for (int i = 0; i < stacks.size(); ++i) {
    printf("%i:", i);
    for (int j = 0; j < stacks[i].size(); ++j) {
      printf(" %i", stacks[i][j]);
    }
    printf("\n");
  }
}

void FindBlock(vector<Stack> &stacks, int blockNum, vector<Stack>::iterator *stack, Stack::iterator *block) {
  for(vector<Stack>::iterator stackIt = stacks.begin(); stackIt != stacks.end(); ++stackIt) {
    Stack::iterator blockIt = find(stackIt->begin(), stackIt->end(), blockNum);

    if (blockIt != stackIt->end()) {
      (*stack) = stackIt;
      (*block) = blockIt;
    }
  }
}

// Moves all blocks starting at startingBlock in sourceStack to the top of destStack
void MovePile(vector<Stack>::iterator sourceStack, Stack::iterator startingBlock, vector<Stack>::iterator destStack) {
  for(Stack::iterator it = startingBlock; it != sourceStack->end(); ++it) {
    destStack->push_back(*it);
  }

  sourceStack->erase(startingBlock, sourceStack->end());
}

// Returns all blocks starting at startingBlock in sourceStack to their original positions
void ReturnHome(vector<Stack> *stacks, vector<Stack>::iterator sourceStack, Stack::iterator startingBlock) {
  for(Stack::iterator it = startingBlock; it != sourceStack->end(); ++it) {
    (*stacks)[*it].push_back(*it);
  }

  sourceStack->erase(startingBlock, sourceStack->end());
}

int main() {
  string command1, command2;
  int a, b;
  int blockCount;
  cin >> blockCount;

  vector<Stack> stacks;
  for (int i = 0; i < blockCount; ++i) {
    stacks.push_back(Stack(1, i));
  }

  while (cin.good()) {
    cin >> command1 >> a >> command2 >> b;

    vector<Stack>::iterator aStack, bStack;
    Stack::iterator aBlock, bBlock;
    FindBlock(stacks, a, &aStack, &aBlock);
    FindBlock(stacks, b, &bStack, &bBlock);

    if ((a != b) && (aStack != bStack)) {
      if (command1 == "move" && command2 == "onto") {
	ReturnHome(&stacks, aStack, aBlock + 1);
	ReturnHome(&stacks, bStack, bBlock + 1);
	MovePile(aStack, aBlock, bStack);
      } else if (command1 == "move" && command2 == "over") {
	ReturnHome(&stacks, aStack, aBlock + 1);
	MovePile(aStack, aBlock, bStack);
      } else if (command1 == "pile" && command2 == "onto") {
	ReturnHome(&stacks, bStack, bBlock + 1);
	MovePile(aStack, aBlock, bStack);
      } else if (command1 == "pile" && command2 == "over") {
	MovePile(aStack, aBlock, bStack);
      }
    }
  }

  PrintStacks(stacks);
  
  return 0;
}

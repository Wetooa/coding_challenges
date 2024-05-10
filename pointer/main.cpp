#include <iostream>

using namespace std;

void sort(int *array, int n, int (*compare)(int, int)) {}

int (*(*x())[])() { /* return  */ }

int ascending(int a, int b) { return a < b ? -1 : a > b ? 1 : 0; }

int y(char *) { return 0; }

int main() {
  int n = 3;
  int *array = new int[3]{1, 2, 3};

  sort(array, n, &ascending);

  return 0;
}

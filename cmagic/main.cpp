#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
  int arr[5] = {1, 2, 3, 4, 5};
  for (int i = 0; i < 5; i++) {
    cout << arr[i] << ' ';
  }
  cout << endl;

  for (int i = 0; i < 5; i++) {
    cout << i[arr] << ' ';
  }
  cout << endl;

  for (int i = 0; i < 5; i++) {
    cout << &i << ' ' << &arr << endl;
  }

  return EXIT_SUCCESS;
}

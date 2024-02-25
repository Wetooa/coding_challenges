
#include "Counting/CountingSort.cpp"
#include "Merge/MergeSort.cpp"

#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

string print(vector<int> &arr) {
  stringstream result;
  for (int num : arr)
    result << num << ' ';
  result << endl;
  return result.str();
}

int main() {

  vector<int> arr = {4, 6, 5, 7, 2, 1, 2};
  cout << "Original: " << print(arr);

  counting_sort(arr);
  cout << "Sorted: " << print(arr);

  return 0;
}

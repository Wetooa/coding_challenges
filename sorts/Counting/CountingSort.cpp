#include <algorithm>
#include <vector>

using namespace std;

void counting_sort(vector<int> &arr) {
  int maximum = *max_element(begin(arr), end(arr));

  vector<int> freq(maximum + 1, 0);
  for (int num : arr) {
    freq[num]++;
  }

  for (int i = 1; i <= maximum; ++i) {
    freq[i] += freq[i - 1];
  }

  vector<int> copy = arr;
  for (int num : copy) {
    if (freq[num])
      arr[--freq[num]] = num;
  }
}

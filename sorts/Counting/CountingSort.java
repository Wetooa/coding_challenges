
package Counting;

import java.util.Arrays;
import java.util.SortedMap;

/**
 * CountingSort
 */
public class CountingSort {

  public static void main(String[] args) {

    int[] arr = { 4, 6, 5, 7, 2, 1, 2 };
    int[] sorted_arr = sort(arr);

    System.out.println(Arrays.toString(arr));
    System.out.println(Arrays.toString(sorted_arr));

  }

  public static int[] sort(int[] arr) {

    // Get maximum element
    int max_element = Arrays.stream(arr).max().orElse(0);

    // Get frequency table
    int[] freq = new int[max_element + 1];
    for (int num : arr) {
      freq[num]++;
    }

    // Create prefix sums table
    for (int i = 1; i <= max_element; ++i) {
      freq[i] += freq[i - 1];
    }

    // Create sorted arr
    int[] sorted_arr = new int[arr.length];
    Arrays.fill(sorted_arr, -1);

    for (int num : arr) {
      if (freq[num] > 0)
        sorted_arr[freq[num] - 1] = num;
    }

    for (int i = arr.length - 2; i > -1; --i) {
      if (sorted_arr[i] == -1)
        sorted_arr[i] = sorted_arr[i + 1];
    }

    return sorted_arr;
  }
}

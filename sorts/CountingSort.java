
import java.util.Arrays;

public class CountingSort extends Sort {

  public void sort(int[] arr) {
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

    // Sort array
    int[] clone = arr.clone();
    for (int num : clone) {
      if (freq[num] > 0)
        arr[--freq[num]] = num;
    }
  }
}

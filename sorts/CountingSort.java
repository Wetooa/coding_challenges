
import java.util.Arrays;

public class CountingSort extends Sort {

  public void sortNoNeg(int[] arr) {
    // Get maximum element
    int max_element = Arrays.stream(arr).max().orElse(0);

    // Get frequency table
    int[] freq = new int[max_element + 1];
    for (int num : arr) {
      freq[num]++;
    }

    // Create prefix sums table
    int running_sum = 0;
    for (int i = 0; i <= max_element; ++i) {
      running_sum += freq[i];
      freq[i] = running_sum;
    }

    // Sort array
    int[] clone = arr.clone();
    for (int num : clone) {
      if (freq[num] > 0)
        arr[--freq[num]] = num;
    }
  }

  // with neg
  public void sort(int[] arr) {
    // Get maximum element
    int max_element = Arrays.stream(arr).max().orElse(0);

    // Get minimum element and offset
    int min_element = Arrays.stream(arr).min().orElse(0);
    int offset = -min_element;

    System.out.println(max_element + " " + min_element);

    // Get frequency table
    int[] freq = new int[offset + max_element + 1];
    for (int num : arr) {
      freq[num + offset]++;
    }

    // Create prefix sums table
    int running_sum = 0;
    for (int i = 0; i <= offset + max_element; ++i) {
      running_sum += freq[i];
      freq[i] = running_sum;
    }

    // Sort array
    int[] clone = arr.clone();
    for (int num : clone) {
      if (freq[num + offset] > 0)
        arr[--freq[num + offset]] = num;
    }
  }
}

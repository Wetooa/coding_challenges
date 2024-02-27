import java.util.Arrays;

/**
 * Sorts
 *
 * A sorting Class
 * sorts all kinds of shit
 */
public class Sorts {

  public static void main(String[] args) {

    Sorts sort = new Sorts();

  }

  public void quickSort(int[] arr) {

  }

  private void quickSort(int[] arr, int left, int right) {

  }

  public void countingSort(int[] arr) {

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
    int[] copy = arr.clone();

    for (int num : copy) {
      if (freq[num] > 0)
        arr[--freq[num]] = num;
    }

  }

}

import java.util.Arrays;

public class Main {

  public static void main(String[] args) {
    checkSpeeds(new CountingSort());
    // checkSpeeds(new BubbleSort());
    // checkSpeeds(new QuickSort());
    // checkSpeeds(new MergeSort());
  }

  private static void checkSpeeds(Sort sort) {
    int[] arr = createUnsortedArray();

    long startTime = System.currentTimeMillis();
    sort.sort(arr);
    long endTime = System.currentTimeMillis();
    System.out.println(
        sort.getClass().getSimpleName() +
            " Runtime: " +
            (endTime - startTime) +
            "ms");

    checkSorted(arr);
  }

  public static int[] createUnsortedArray() {
    // number of elements to sort
    int n = 100;

    // inclusive
    int lower_bound = -100;

    // exclusive
    int upper_bound = 100;

    return Arrays
        .stream(new int[n])
        .map(num -> (int) (Math.random() * (upper_bound - lower_bound) + lower_bound))
        .toArray();
  }

  public static void checkSorted(int[] arr) {
    System.out.println(Arrays.toString(arr));
    for (int i = 1; i < arr.length; ++i) {
      assert (arr[i - 1] <= arr[i]);
    }
  }
}

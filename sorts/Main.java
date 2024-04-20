import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {

  public static void main(String[] args) {
    // checkSort(new CountingSort());
    // checkSort(new BubbleSort());
    checkSort(new QuickSort());
    // checkSort(new MergeSort());
  }

  private static void checkSort(Sort sort) {
    int[] arr = createUnsortedArray();

    long startTime = System.currentTimeMillis();
    sort.sort(arr);
    long endTime = System.currentTimeMillis();
    System.out.println(
        sort.getClass().getSimpleName() +
            " Runtime: " +
            (endTime - startTime) +
            "ms");

    try {
      checkSorted(arr);
    } catch (AssertionError e) {
      System.out.println(e.getMessage());
    }
  }

  public static int[] createUnsortedArray() {
    // number of elements to sort
    int n = 100000;

    // inclusive
    int lower_bound = -100;

    // exclusive
    int upper_bound = 100;

    return Arrays
        .stream(new int[n])
        .map(num -> (int) (Math.random() * (upper_bound - lower_bound) + lower_bound))
        .toArray();
  }

  public static int[] createSortedArray() {
    // number of elements to sort
    int n = 1000000;

    return IntStream.rangeClosed(0, n).toArray();
  }

  public static void checkSorted(int[] arr) {
    for (int i = 1; i < arr.length; ++i) {
      assert arr[i - 1] <= arr[i] : "Unsorted!!!!";
    }
  }

}

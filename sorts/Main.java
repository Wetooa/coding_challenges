import java.util.Arrays;

public class Main {

  public static void main(String[] args) {
    checkSpeeds(new QuickSort());
    // checkSpeeds(new BubbleSort());
    checkSpeeds(new CountingSort());
    checkSpeeds(new MergeSort());
  }

  private static void checkSpeeds(Sort sort) {
    int[] arr = createUnsortedArray();

    long startTime = System.currentTimeMillis();
    sort.sort(arr);
    long endTime = System.currentTimeMillis();

    System.out.println(
        sort.getClass() + " Runtime: " + (endTime - startTime) + "ms");

    checkSorted(arr);
  }

  public static int[] createUnsortedArray() {
    int n = 1000000;
    int upper_bound = 10;

    return Arrays
        .stream(new int[n])
        .map(num -> (int) (Math.random() * upper_bound))
        .toArray();
  }

  public static void checkSorted(int[] arr) {
    for (int i = 1; i < arr.length; ++i) {
      assert (arr[i - 1] <= arr[i]);
    }
  }
}

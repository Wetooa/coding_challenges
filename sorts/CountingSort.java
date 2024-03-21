
import java.util.Arrays;
import java.util.Scanner;

public class CountingSort extends Sort {

  public void sortNoNegWithGuide(int[] arr) {
    Scanner sc = new Scanner(System.in);

    System.out.println(" --- Unsorted array: " + Arrays.toString(arr) + " --- \n");
    System.err.print(" >>> 1. Getting maximum element <<<");
    sc.nextLine();

    int max_element = Arrays.stream(arr).max().orElse(0);

    System.out.println("Maximum element: " + max_element);
    sc.nextLine();

    System.err.print(" >>> 2. Creating the frequency array <<<");
    sc.nextLine();

    int[] freq = new int[max_element + 1];
    for (int num : arr) {
      freq[num]++;
    }

    System.out.println("Frequency array: " + Arrays.toString(freq));
    sc.nextLine();

    System.err.print(" >>> 3. Creating the prefix summed array <<< ");
    sc.nextLine();

    for (int i = 1; i <= max_element; ++i) {
      freq[i] += freq[i - 1];
    }

    System.out.println("Prefix sums array: " + Arrays.toString(freq));
    sc.nextLine();

    System.err.print(" >>> 4. Creating the sorted array <<< ");
    sc.nextLine();

    int[] clone = arr.clone();
    for (int num : clone) {
      arr[--freq[num]] = num;
    }

    System.out.println("Sorted array: " + Arrays.toString(arr));

    sc.close();

  }

  public void sortWithNegWithGuide(int[] arr) {
    Scanner sc = new Scanner(System.in);

    System.out.println("Unsorted array: " + Arrays.toString(arr) + "\n");

    System.out.print(" >>> 1. Getting maximum and minimum element <<<");
    sc.nextLine();

    int max_element = Arrays.stream(arr).max().orElse(0);
    int min_element = Arrays.stream(arr).min().orElse(0);
    int offset = -min_element;

    System.out.println("Maximum element: " + max_element);
    System.out.println("Minimum element: " + min_element);
    System.out.println("Offset (-1 multiplied the minimum element): " + offset);
    sc.nextLine();

    System.out.print(" >>> 2. Creating the frequency array <<<");
    sc.nextLine();

    int[] freq = new int[offset + max_element + 1];
    for (int num : arr) {
      freq[num + offset]++;
    }

    System.out.println("Frequency array: " + Arrays.toString(freq));
    sc.nextLine();

    System.out.print(" >>> 3. Creating the prefix summed array <<< ");
    sc.nextLine();

    for (int i = 1; i <= offset + max_element; ++i) {
      freq[i] += freq[i - 1];
    }

    System.out.println("Prefix sums array: " + Arrays.toString(freq));
    sc.nextLine();

    System.out.print(" >>> 4. Creating the sorted array <<< ");
    sc.nextLine();

    int[] clone = arr.clone();
    for (int num : clone) {
      arr[--freq[num + offset]] = num;
    }

    System.out.println("Sorted array: " + Arrays.toString(arr));

    sc.close();

  }

  public void sortNoNeg(int[] arr) {
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
      arr[--freq[num]] = num;
    }
  }

  public void sortWithNeg(int[] arr) {
    // Get maximum element
    int max_element = Arrays.stream(arr).max().orElse(0);

    // Get minimum element and offset
    int min_element = Arrays.stream(arr).min().orElse(0);
    int offset = -min_element;

    // Get frequency table
    int[] freq = new int[offset + max_element + 1];
    for (int num : arr) {
      freq[num + offset]++;
    }

    // Create prefix sums table
    for (int i = 1; i <= offset + max_element; ++i) {
      freq[i] += freq[i - 1];
    }

    // Sort array
    int[] clone = arr.clone();
    for (int num : clone) {
      arr[--freq[num + offset]] = num;
    }
  }

  @Override
  public void sort(int[] arr) {
    sortNoNegWithGuide(arr);
  }
}

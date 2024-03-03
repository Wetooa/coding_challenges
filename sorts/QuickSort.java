
public class QuickSort extends Sort {

  public void sort(int[] arr) {
    quickSort(arr, 0, arr.length - 1);
  }

  private void quickSort(int[] arr, int left, int right) {
    if (left >= right)
      return;

    // Get a pivot and swap it for the rightmost element
    int pivot = (int) (Math.random() * (right - left) + left);
    swap(arr, pivot, right);

    // Sort the array numbers relative to the pivot
    // elements greater than the pivot go to the right while the rest go to the left
    int l = left, r = right - 1;
    while (l <= r) {
      while (l <= r && arr[l] <= arr[right])
        l++;
      while (l <= r && arr[r] > arr[right])
        r--;

      if (l <= r) {
        swap(arr, l, r);
        ++l;
        --r;
      }
    }

    // Bring pivot back to position
    swap(arr, l, right);

    // Recursively sort the two paritions (divide-and-conquer)
    if (l + 1 < right) {
      quickSort(arr, left, l - 1);
      quickSort(arr, l + 1, right);
    }
  }
}

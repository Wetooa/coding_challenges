import java.util.Arrays;

class MergeSort extends Sort {

  private void mergeSort(int[] arr, int left, int right) {
    if (left >= right)
      return;

    int half = (left + right) / 2;

    mergeSort(arr, left, half);
    mergeSort(arr, half + 1, right);

    int[] copy = Arrays.copyOfRange(arr, left, right + 1);
    int l = 0, r = half - left + 1;

    for (int i = left; i <= right; i++) {
      arr[i] = (r > right - left || (l <= half - left && copy[l] <= copy[r])) ? copy[l++] : copy[r++];
    }
  }

  @Override
  public void sort(int[] arr) {
    mergeSort(arr, 0, arr.length - 1);
  }

}

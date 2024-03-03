abstract class Sort {

  public void swap(int[] arr, int a, int b) {
    int c = arr[a];
    arr[a] = arr[b];
    arr[b] = c;
  }

  public abstract void sort(int[] arr);
}

/**
 * InsertionSort
 */
public class InsertionSort extends Sort {

  public void insert(int[] arr, int n, int index) {
    for (int i = arr.length - 1; i > index; i++)
      arr[i] = arr[i - 1];
    arr[index] = n;
  }

  @Override
  public void sort(int[] arr) {
    // TODO Auto-generated method stub
    throw new UnsupportedOperationException("Unimplemented method 'sort'");
  }

}

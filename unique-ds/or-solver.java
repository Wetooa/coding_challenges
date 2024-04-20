
class OrSolver {
  private final int N = 32;
  private int[] d = new int[N];

  private int update(int num, int increment) {
    int l = N;
    while (num > 0) {
      d[--l] += (num & 1) * increment;
      num >>= 1;
    }
    return get();
  }

  public int add(int num) {
    return update(num, 1);
  }

  public int remove(int num) {
    return update(num, -1);
  }

  public int get() {
    int res = 0;
    for (int i = 0; i < N; i++) {
      res |= (d[i] > 0 ? 1 : 0) << (N - i - 1);
    }
    return res;
  }
}

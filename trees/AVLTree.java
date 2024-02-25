class AVLTree<K extends Comparable<K>, V extends Comparable<V>> {

  class AVLNode {

    public K key;
    public V val;

    public AVLNode left, right, parent;
    public int height;

    public AVLNode(K key, V val, AVLNode left, AVLNode right, AVLNode parent) {
      this.key = key;
      this.val = val;
      this.left = left;
      this.right = right;
      this.parent = parent;
      this.height = 1;

    }

    public AVLNode(K key, V val, AVLNode parent) {
      this(key, val, null, null, parent);
    }

    public AVLNode(K key, V val) {
      this(key, val, null);
    }

    @Override
    public String toString() {
      return String.format("(%s=%s | bf=%d)", String.valueOf(key), String.valueOf(val), getBalance());
    }

    public AVLNode rightRotate() {
      AVLNode x = this.left;
      AVLNode T2 = x.right;

      x.right = this;
      this.left = T2;

      this.updateHeight();
      x.updateHeight();

      return x;
    }

    public AVLNode leftRotate() {
      AVLNode x = this.right;
      AVLNode T2 = x.left;

      x.left = this;
      this.right = T2;

      this.updateHeight();
      x.updateHeight();

      return x;
    }

    public int getBalance() {
      int l = left != null ? left.height : 0;
      int r = right != null ? right.height : 0;

      return l - r;
    }

    public void updateHeight() {
      int l = left != null ? left.height : 0;
      int r = right != null ? right.height : 0;

      this.height = Math.max(l, r) + 1;
    }
  }

  public static void main(String[] args) {

    Timer t = new Timer();

    t.timeFunction(() -> {

      int n = 100;
      AVLTree<Integer, Integer> map = new AVLTree<>();

      map.upsert(10, 10);
      map.upsert(20, 20);
      map.upsert(30, 30);
      map.upsert(40, 40);
      map.upsert(50, 50);
      map.upsert(25, 25);
      map.preorder();
      System.out.println(map);

      // for (int i = 0; i < n; i++) {
      // map.upsert(i, i);
      // }

      // for (int i = 0; i < n; ++i) {
      // Integer key = (int) (Math.random() * 1000);
      // Integer val = (int) (Math.random() * 1000);
      // map.upsert(key, val);
      // }

      // for (int i = 0; i < n; i += n / 100) {
      // System.out.println("Element at key " + i + ": " + map.get(i));
      // }
      //
      // for (int i = 0; i < n; i += 2) {
      // System.out.println("Removing " + i);
      // map.remove(i);
      // }

    });

  }

  private AVLNode root;

  private int size;

  public AVLTree() {
    root = null;
    size = 0;
  }

  public int getSize() {
    return size;
  }

  public V get(K key) {
    try {
      V res = get(root, key);
      return res;
    } catch (Exception e) {
      System.out.println(e.getMessage());
    }
    return null;
  }

  public void upsert(K key, V val) {
    root = upsert(root, key, val);
  }

  @Override
  public String toString() {
    return String.format("Tree:%s\nSize: %d\n", print(root, 1), size);
  }

  public void preorder() {
    preorder(root);
    System.out.println();
  }

  private V get(AVLNode curr, K key) throws Exception {
    if (curr == null)
      throw new Exception("Key does not exist!");

    if (key.equals(curr.key))
      return curr.val;

    return key.compareTo(curr.key) == -1 ? get(curr.left, key) : get(curr.right, key);
  }

  private AVLNode upsert(AVLNode curr, K key, V val) {
    if (curr == null) {
      ++size;
      return new AVLNode(key, val);
    }

    // when we insert an already present key, update the value
    if (key.equals(curr.key)) {
      curr.val = val;
      return curr;
    }

    // when less go left, like normal BST
    if (key.compareTo(curr.key) == -1) {
      curr.left = upsert(curr.left, key, val);
    } else {
      curr.right = upsert(curr.right, key, val);
    }

    // recursive bottom-up uproach
    curr.updateHeight();
    int balance = curr.getBalance();

    // left left
    if (balance > 1 && key.compareTo(curr.left.key) == -1) {
      return curr.rightRotate();
    }

    // right right
    if (balance < -1 && key.compareTo(curr.right.key) == 1) {
      return curr.leftRotate();
    }

    // left right
    if (balance > 1 && key.compareTo(curr.left.key) == 1) {
      curr.left = curr.left.leftRotate();
      return curr.rightRotate();
    }

    // right left
    if (balance < -1 && key.compareTo(curr.right.key) == -1) {
      curr.right = curr.right.rightRotate();
      return curr.leftRotate();
    }

    return curr;
  }

  private String print(AVLNode curr, int depth) {
    String spaces = "\n" + "  ".repeat(depth);

    if (curr == null)
      return spaces + "None";

    String res = "";
    res += (spaces + "Element: " + curr);
    res += (spaces + "Left: " + print(curr.left, depth + 1));
    res += (spaces + "Right: " + print(curr.right, depth + 1));

    return res;
  }

  private void preorder(AVLNode curr) {
    if (curr == null)
      return;

    System.out.print(curr.key + " ");
    preorder(curr.left);
    preorder(curr.right);
  }
}

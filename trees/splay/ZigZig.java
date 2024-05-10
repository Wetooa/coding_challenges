
// FIX: i dunno this seems like its a splay tree to me

public class ZigZig<K extends Comparable<K>, V> {

  public class Node {

    Node left, right, parent;
    K key;
    V val;

    public Node(K key, V val) {
      this(key, val, null, null, null);
    }

    @Override
    public String toString() {
      return String.format("(%s = %s)", key, val);
    }

    public Node(K key, V val, Node left, Node right, Node parent) {
      this.key = key;
      this.val = val;
      this.left = left;
      this.right = right;
      this.parent = parent;
    }

    public Node rightRotate() {
      Node par = this.parent;

      par.left = this.right;
      this.right = par;

      return this;
    }

    public Node leftRotate() {
      Node par = this.parent;

      par.right = this.left;
      this.left = par;

      return this;
    }

  }

  Node root;

  public V get(K key) {
    root = get(root, key);
    return root != null ? root.val : null;
  }

  public void put(K key, V val) {
    root = put(root, key, val);
  }

  private Node get(Node root, K key) {
    if (root == null)
      return null;

    if (root.key.equals(key)) {
      return root;
    }

    // TODO: learn more about this, and the normal ZIGZIG operation
    if (root.key.compareTo(key) == 1) {
      root.left = get(root.left, key);
      root.left.parent = root;
      return root.left.rightRotate();
    } else {
      root.right = get(root.right, key);
      root.right.parent = root;
      return root.right.leftRotate();
    }
  }

  private Node put(Node root, K key, V val) {
    if (root == null)
      return new Node(key, val);

    if (root.key.compareTo(key) == 1) {
      root.left = put(root.left, key, val);
      root.left.parent = root;
      return root.left.rightRotate();
    } else {
      root.right = put(root.right, key, val);
      root.right.parent = root;
      return root.right.leftRotate();
    }
  }

  public void print() {
    System.out.println(print(root, 0));
  }

  private String print(Node curr, int depth) {
    String spaces = "\n" + "  ".repeat(depth);

    if (curr == null)
      return spaces + "None";

    String res = "";
    res += (spaces + "E: " + curr);
    res += (spaces + "L: " + print(curr.left, depth + 1));
    res += (spaces + "R: " + print(curr.right, depth + 1));

    return res;
  }

  public static void main(String[] args) {
    Splay<Integer, Integer> t = new Splay<>();

    t.put(1, 1);
    t.put(2, 2);
    t.put(3, 3);
    t.put(4, 4);

    t.print();

    t.get(1);
    t.print();

    t.get(3);
    t.print();
  }
}

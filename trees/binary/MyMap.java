import java.util.HashMap;
import java.util.Map;

/**
 * BetterBST
 */
public class MyMap<K extends Comparable<K>, V> {

  class Node {
    public K key;
    public V val;

    public Node left, right, parent;

    public Node(K key, V val, MyMap<K, V>.Node right, MyMap<K, V>.Node left, MyMap<K, V>.Node parent) {
      this.key = key;
      this.val = val;
      this.right = right;
      this.left = left;
      this.parent = parent;
    }

    public Node(K key, V val) {
      this(key, val, null, null, null);
    }

  }

  private Node root;
  private int size;

  public int getSize() {
    return size;
  }

  public MyMap() {
    root = null;
    size = 0;
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

  private V get(Node curr, K key) throws Exception {
    if (curr == null)
      throw new Exception("Key does not exist!");

    if (key.equals(curr.key))
      return curr.val;

    return key.compareTo(curr.key) == -1 ? get(curr.left, key) : get(curr.right, key);
  }

  public void insert(K key, V val) {
    root = insert(root, key, val);
  }

  private Node insert(Node node, K key, V val) {
    if (node == null) {
      ++size;
      return new Node(key, val);
    }

    if (node.key.equals(key)) {
      node.val = val;
      return node;
    }

    if (key.compareTo(node.key) == -1) {
      node.left = insert(node.left, key, val);
    } else {
      node.right = insert(node.right, key, val);
    }

    return node;
  }

  public void remove(K key) {
    root = remove(root, key);
  }

  private Node remove(Node node, K key) {
    if (node == null)
      return null;

    if (node.key.equals(key)) {
      --size;

      if (node.left != null && node.right != null) {

        Node successor = node.right;
        while (successor.left != null)
          successor = successor.left;

        node.key = successor.key;
        node.val = successor.val;

        successor.parent.left = null;

        return node;
      }

      if (node.left == null) {
        return node.right;
      } else {
        return node.left;
      }
    }

    if (key.compareTo(node.key) == -1) {
      node.left = remove(node.left, key);
    } else {
      node.right = remove(node.right, key);
    }

    return node;
  }

  public static void main(String[] args) {

    Timer t = new Timer();

    t.timeFunction(
        () -> {
          int n = 10000;
          MyMap<String, Integer> map = new MyMap<>();

          // for (int i = 0; i < n; i++) {
          // map.insert(i, i);
          // }

          // for (int i = 0; i < n; ++i) {
          // Integer key = (int) (Math.random() * 1000);
          // Integer val = (int) (Math.random() * 1000);
          // map.insert(key, val);
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

}

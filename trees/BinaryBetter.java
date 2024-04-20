/**
 * BinaryBetter
 */
public class BinaryBetter<K extends Comparable<K>, V> {

  public class Node {
    K key;
    V val;

    Node left, right;

    public Node(K key, V val) {
      this.key = key;
      this.val = val;
    }
  }

  Node root;

  public void insert(K key, V val) {
    insert(root, key, val);
  }

  public V get(K key) {
    return get(root, key);
  }

  public void remove(K key) {
    remove(root, key);
  }

  private Node insert(Node root, K key, V val) {
    if (root == null) {
      return new Node(key, val);
    }

    if (root.key.compareTo(key) < 0)
      root.left = insert(root.left, key, val);
    else
      root.right = insert(root.right, key, val);

    return root;
  }

  private V get(Node root, K key) throws IllegalArgumentException {
    if (root == null)
      throw new IllegalArgumentException("Key not found");

    if (root.key.equals(key))
      return root.val;

    return root.key.compareTo(key) < 0 ? get(root.left, key) : get(root.right, key);
  }

  private Node remove(Node root, K key) throws IllegalArgumentException {
    if (root == null)
      throw new IllegalArgumentException("Key not found");

    if (root.key.compareTo(key) == -1) {
      root.left = remove(root.left, key);
    } else if (root.key.compareTo(key) == 1) {
      root.right = remove(root.right, key);
    } else {

      if (root.left == null || root.right == null) {
        root = root.left == null ? root.right : root.left;
      } else {

        Node successor = root.right;
        while (successor.left != null)
          successor = successor.left;

        root.key = successor.key;
        root.val = successor.val;
        root.right = remove(root.right, root.key);
      }
    }

    return root;
  }
}

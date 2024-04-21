
/**
 * Tree
 */
public class Tree {

  private Node root;
  private int size;

  public Tree() {
    this.size = 0;
    this.root = null;
  }

  public boolean isEmpty() {
    return this.size == 0;
  }

  public boolean contains(Integer elem) {
    return find(elem) != null;
  }

  private Node find(Integer elem, Node curr) {
    if (curr == null)
      return null;
    if (curr.elem == elem)
      return curr;

    Node leftSearch = find(elem, curr.left);
    Node rightSearch = find(elem, curr.right);

    return leftSearch != null ? leftSearch : rightSearch;
  }

  public Node find(Integer elem) {
    return find(elem, root);
  }

  public void insert(Integer elem, Node parent, boolean insertLeft) {
    Node newNode = new Node(elem, parent);

    if (size == 0) {
      root = newNode;
    } else if (insertLeft) {
      parent.left = newNode;
    } else {
      parent.right = newNode;
    }

    ++size;
  }

  public void remove(Node node) throws IllegalArgumentException {
    if (node.left != null && node.right != null)
      throw new IllegalArgumentException("Deleted node can't have two children!");

    Node children = node.left != null ? node.left : node.right;

    if (node == root) {
      root = children;
      children.parent = null;
    } else {
      if (node.parent.left == node) {
        node.parent.left = children;
      } else {
        node.parent.right = children;
      }
      children.parent = node.parent;
    }
    --size;
  }

  public Node getRoot() {
    return root;
  }

  public int getSize() {
    return size;
  }

  @Override
  public String toString() {
    return String.format("Tree:%s\nSize: %d\n", print(root, 1), size);
  }

  public String print(Node curr, int depth) {
    String spaces = "\n" + "  ".repeat(depth);

    if (curr == null)
      return spaces + "None";

    String res = "";
    res += (spaces + "Element: " + curr);
    res += (spaces + "Left: " + print(curr.left, depth + 1));
    res += (spaces + "Right: " + print(curr.right, depth + 1));

    return res;
  }

}

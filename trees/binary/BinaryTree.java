
// lame ass BST
public class BinaryTree {

  private Tree t;

  public BinaryTree() {
    t = new Tree();
  }

  private Node findParentToInsert(Integer elem, Node curr, Node parent) {
    if (curr == null)
      return parent;

    return elem < curr.elem ? findParentToInsert(elem, curr.left, curr) : findParentToInsert(elem, curr.right, curr);
  }

  public Node find(Integer elem, Node curr) {
    if (curr == null)
      return null;
    if (elem == curr.elem)
      return curr;

    return elem < curr.elem ? find(elem, curr.left) : find(elem, curr.right);
  }

  public Node find(Integer elem) {
    return find(elem, t.getRoot());
  }

  public void insert(Integer elem) {
    Node parent = findParentToInsert(elem, t.getRoot(), null);

    if (parent == null) {
      t.insert(elem, parent, true);
    } else if (elem < parent.elem) {
      t.insert(elem, parent, true);
    } else {
      t.insert(elem, parent, false);
    }
  }

  public void remove(Integer elem) throws IllegalArgumentException {
    Node target = find(elem);

    if (target == null)
      throw new IllegalArgumentException("Node not found!");

    if (target.left != null && target.right != null) {

      Node replacer = target.right;
      while (replacer.left != null) {
        replacer = replacer.left;
      }

      target.elem = replacer.elem;
      t.remove(replacer);
    } else {
      t.remove(target);
    }

  }

  @Override
  public String toString() {
    return t.toString();
  }

  public boolean isEmpty() {
    return this.t.getSize() == 0;
  }

}

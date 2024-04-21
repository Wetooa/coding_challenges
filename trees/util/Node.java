class Node {

  public Integer elem;
  public Node left, right, parent;

  public Node(Integer elem, Node left, Node right, Node parent) {
    this.elem = elem;
    this.left = left;
    this.right = right;
    this.parent = parent;
  }

  public Node(Integer elem, Node parent) {
    this(elem, null, null, parent);
  }

  public Node(Integer elem) {
    this(elem, null);
  }

  @Override
  public String toString() {
    return String.valueOf(elem);
  }

}

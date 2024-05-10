// DO NOT modify this file.
// Go to mybinarytree's zigleft and zigright methods.

struct node {
  node *parent;
  node *right;
  node *left;
  int elem;

  int height() {
    int l = left ? left->height() : 0;
    int r = right ? right->height() : 0;
    return (l > r ? l : r) + 1;
  }
};

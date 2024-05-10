#include "mybinarytree.h"

class BST {
  BinaryTree *tree = new MyBinaryTree();

public:
  bool search(int num) { return search_node(tree->getRoot(), num); }

  bool search_node(node *n, int num) {
    if (n == NULL) {
      return false;
    }
    if (n->elem == num) {
      return true;
    }
    if (num > n->elem) {
      // proceed to right
      return search_node(n->right, num);
    } else {
      return search_node(n->left, num);
    }
  }

  // TODO perform post-processing by checking for violation after insertion
  // from the node inserted (or from its parent) until the root
  node *insert(int num) {
    node *n = tree->getRoot();
    if (n == NULL) {
      return tree->addRoot(num);
    }
    return insert_node(n, num);
  }

  node *insert_node(node *n, int num) {
    if (n == NULL) {
      return NULL;
    }
    if (n->elem == num) {
      return NULL;
    }

    node *res = NULL;
    if (num > n->elem) {
      if (!n->right) {
        res = tree->addRight(n, num);
      } else {
        res = insert_node(n->right, num);
      }
    } else {
      if (!n->left) {
        res = tree->addLeft(n, num);
      } else {
        res = insert_node(n->left, num);
      }
    }

    if (check(n))
      restructure(n);

    return res;
  }

  // TODO perform post-processing by checking for violation after deletion
  // from the parent of the node removed until the root
  bool remove(int num) { return remove_node(tree->getRoot(), num); }

  bool remove_node(node *n, int num) {
    if (n == NULL) {
      return false;
    }

    bool res;
    if (n->elem == num) {
      if (n->left && n->right) {
        node *r = n->right;
        while (r->left) {
          r = r->left;
        }

        node *par = r->parent;
        int rem = tree->remove(r);
        n->elem = rem;

        while (par != n && check(par)) {
          node *nex = par->parent;
          restructure(par);
          par = nex;
        }
      } else {
        tree->remove(n);
      }
      res = true;
    } else if (num > n->elem) {
      res = remove_node(n->right, num);
    } else {
      res = remove_node(n->left, num);
    }

    if (check(n))
      restructure(n);

    return res;
  }

  bool check(node *gp) {
    int l = gp->left ? gp->left->height() : 0;
    int r = gp->right ? gp->right->height() : 0;
    return l - r > 1 || l - r < -1;
  }

  // HACK: dont use
  bool fake_restructure(node *child) {
    node *par = child->parent;
    node *gp = par->parent;

    bool gtop_right = false;
    if (gp->right == par) {
      gtop_right = true;
    }

    bool ptoc_right = false;
    if (par->right == child) {
      ptoc_right = true;
    }

    // FOR THE FOLLOWING: Write in each of the if statements a console output
    // on its corresponding operation (ZIGLEFT, ZIGRIGHT, ZIGZAGLEFT, or
    // ZIGZAGRIGHT)

    // z
    //  \
        //   y
    //    \
        //     x
    if (gtop_right && ptoc_right) {
      zigleft(par);
      zigleft(child);
      cout << "ZIGZIGLEFT" << endl;
    }

    // z
    //   \
        //     y
    //    /
    //   x
    else if (gtop_right && !ptoc_right) {
      zigright(child);
      zigleft(child);
      cout << "ZIGZAGLEFT" << endl;
    }

    //     z
    //    /
    //   y
    //  /
    // x
    else if (!gtop_right && !ptoc_right) {
      zigright(par);
      zigright(child);
      cout << "ZIGZIGRIGHT" << endl;
    }

    //      z
    //    /
    //  y
    //   \
        //    x
    else {
      // TODO call to either zigleft or zigright or both
      zigleft(child);
      zigright(child);
      cout << "ZIGZAGRIGHT" << endl;
    }

    return true;
  }

  // TODO copy and paste your completed restructure method here
  bool restructure(node *gp) {
    node *par; // parent
    // TODO find parent

    int l = gp->left ? gp->left->height() : 0;
    int r = gp->right ? gp->right->height() : 0;
    par = l > r ? gp->left : gp->right;

    // This is an indicator of the placement of grandparent to parent (gtop)
    bool gtop_right = false;
    if (gp->right == par) {
      gtop_right = true;
    }

    node *child;
    // TODO find child
    l = par->left ? par->left->height() : 0;
    r = par->right ? par->right->height() : 0;
    child = l < r || (l == r && gtop_right) ? par->right : par->left;

    // This is an indicator of the placement of parent to child (ptoc)
    bool ptoc_right = false;
    if (par->right == child) {
      ptoc_right = true;
    }

    // FOR THE FOLLOWING: Write in each of the if statements a console output
    // on its corresponding operation (ZIGLEFT, ZIGRIGHT, ZIGZAGLEFT, or
    // ZIGZAGRIGHT)

    // z
    //  \
        //   y
    //    \
        //     x
    if (gtop_right && ptoc_right) {
      // TODO call to either zigleft or zigright or both
      zigleft(par);
      cout << "ZIGLEFT" << endl;
    }

    // z
    //   \
        //     y
    //    /
    //   x
    else if (gtop_right && !ptoc_right) {
      // TODO call to either zigleft or zigright or both
      zigright(child);
      zigleft(child);
      cout << "ZIGZAGLEFT" << endl;
    }

    //     z
    //    /
    //   y
    //  /
    // x
    else if (!gtop_right && !ptoc_right) {
      // TODO call to either zigleft or zigright or both
      zigright(par);
      cout << "ZIGRIGHT" << endl;
    }

    //      z
    //    /
    //  y
    //   \
        //    x
    else {
      // TODO call to either zigleft or zigright or both
      zigleft(child);
      zigright(child);
      cout << "ZIGZAGRIGHT" << endl;
    }

    return true;
  }

  void zigleft(node *curr) { tree->zigleft(curr); }

  void zigright(node *curr) { tree->zigright(curr); }

  void print() { tree->print(); }
};

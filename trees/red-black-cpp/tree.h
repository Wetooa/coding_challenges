
#include <cstdlib>
#include <iostream>

#include "node.h"

using namespace std;

class BSTree {
  node *root;
  int size;

public:
  BSTree() {
    root = NULL;
    size = 0;
  }

  bool insert(int num) {
    insert(root, num, NULL, false);
    size++;
    return true;
  }

  node *create_node(int element, bool is_red = true, node *parent = NULL) {
    node *n = new node();
    n->element = element;
    n->is_red = is_red;
    n->parent = parent;
    return n;
  }

  bool insert(node *curr, int num, node *par, bool is_left) {

    if (root == NULL) {
      root = create_node(num, false, NULL);
      return true;
    }

    if (curr == NULL) {
      node *n = create_node(num, true, par);

      if (is_left)
        par->left = n;
      else
        par->right = n;

      restructure(n);
      return true;
    }

    if (curr->element > num) {
      insert(curr->left, num, curr, true);
    } else {
      insert(curr->right, num, curr, false);
    }

    restructure(curr);
    return true;
  }

  void recolor(node *curr) {
    curr->is_red = false;
    curr->left->is_red = true;
    curr->right->is_red = true;
  }

  bool restructure(node *child) {
    node *par = child->parent;

    if (!par || !par->is_red || !child->is_red)
      return true;

    node *gp = par->parent;
    node *sib = gp->left == par ? gp->right : gp->left;

    if (!sib || !sib->is_red) {
      cout << "INSERTION Violation: Case 1" << endl;

      bool ptop_right = par->left == child;
      bool gtop_right = gp->left == par;

      if (gtop_right && ptop_right) {
        zigright(par);
        recolor(par);
        cout << "ZIGRIGHT" << endl;
      } else if (gtop_right && !ptop_right) {
        zigleft(child);
        zigright(child);
        recolor(child);
        cout << "ZIGZAGRIGHT" << endl;
      } else if (!gtop_right && !ptop_right) {
        zigleft(par);
        recolor(par);
        cout << "ZIGLEFT" << endl;
      } else {
        zigright(child);
        zigleft(child);
        recolor(child);
        cout << "ZIGZAGLEFT" << endl;
      }

    } else {
      cout << "INSERTION Violation: Case 2" << endl;

      par->is_red = false;
      sib->is_red = false;

      if (gp != root)
        gp->is_red = true;

      return true;
    }

    return true;
  }

  void zigleft(node *curr) {
    node *x = curr;
    node *y = x->parent;
    node *z = y->parent;

    if (z == NULL)
      root = x;
    else if (y == z->left)
      z->left = x;
    else
      z->right = x;

    x->parent = z;
    y->parent = x;

    if (x->left)
      x->left->parent = y;
    y->right = x->left;

    x->left = y;
  }

  void zigright(node *curr) {
    node *x = curr;
    node *y = x->parent;
    node *z = y->parent;

    if (z == NULL)
      root = x;
    else if (y == z->left)
      z->left = x;
    else
      z->right = x;

    y->parent = x;
    x->parent = z;

    if (x->right)
      x->right->parent = y;
    y->left = x->right;

    x->right = y;
  }

  // WARNING. Do not modify these methods below.
  // Doing so will nullify your score for this activity.
  void print() {
    if (isEmpty()) {
      cout << "EMPTY" << endl;
      return;
    }
    cout << "PRE-ORDER: ";
    print_preorder(root);
    cout << endl << "IN-ORDER: ";
    print_inorder(root);
    cout << endl << "POST-ORDER: ";
    print_postorder(root);
    cout << endl << "STATUS: " << check_health(root, NULL) << endl;
  }

  bool isEmpty() { return size == 0; }

  void print_preorder(node *curr) {
    cout << curr->element;
    if (curr->is_red) {
      cout << "(R) ";
    } else {
      cout << "(B) ";
    }
    if (curr->left != NULL) {
      print_preorder(curr->left);
    }
    if (curr->right != NULL) {
      print_preorder(curr->right);
    }
  }

  void print_inorder(node *curr) {
    if (curr->left != NULL) {
      print_inorder(curr->left);
    }
    cout << curr->element;
    if (curr->is_red) {
      cout << "(R) ";
    } else {
      cout << "(B) ";
    }
    if (curr->right != NULL) {
      print_inorder(curr->right);
    }
  }

  void print_postorder(node *curr) {
    if (curr->left != NULL) {
      print_postorder(curr->left);
    }
    if (curr->right != NULL) {
      print_postorder(curr->right);
    }
    cout << curr->element;
    if (curr->is_red) {
      cout << "(R) ";
    } else {
      cout << "(B) ";
    }
  }

  // WARNING. Do not modify this method.
  // Doing so will nullify your score for this activity.
  bool check_health(node *curr, node *parent) {
    bool health = curr->parent == parent;
    if (curr->left != NULL) {
      health &= check_health(curr->left, curr);
    }
    if (curr->right != NULL) {
      health &= check_health(curr->right, curr);
    }
    return health;
  }
};

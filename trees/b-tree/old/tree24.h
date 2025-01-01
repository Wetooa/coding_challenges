#include "node.h"

class Tree24 {
  Node *root;
  int size;

public:
  Tree24() {
    root = NULL;
    size = 0;
  }

  void print() {
    cout << "Size: " << size << endl;
    root->print();
  }

  void insert(int num) {
    if (!root) {
      root = new Node(num, NULL);
    } else {
      Node *w = search(num);

      while (true) {
        bool ok = w->addKey(num);

        if (ok)
          break;

        // TODO: wla pani sir hAHFNOAJDNFUISDBGUSIDFSDF
        if (root == w) {
          Node *u = new Node(w->getData(MAX_KEYS / 2), NULL);
          u->addChildren(w);
          w->split(MAX_KEYS / 2);
          root = u;
        } else {
        }
      }
    }

    size++;
  }

  Node *search(int num) { return root ? root->search(num) : NULL; }
};

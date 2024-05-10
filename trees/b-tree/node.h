
#include <climits>
#include <cstdlib>
#include <iostream>

using namespace std;

// this means that if we get 4, there will be a violation
#define MAX_KEYS 4

class Node {
  int size;
  int *data;
  Node **children;
  Node *parent;

public:
  Node(int num, Node *parent) {
    this->data = (int *)calloc(MAX_KEYS, sizeof(int));
    this->data[0] = num;

    this->children = (Node **)calloc(MAX_KEYS + 1, sizeof(Node *));
    this->parent = parent;
    this->size = 1;
  }

  Node() {
    this->data = (int *)calloc(MAX_KEYS, sizeof(int));
    this->children = (Node **)calloc(MAX_KEYS + 1, sizeof(Node *));
    this->parent = NULL;
    this->size = 0;
  }

  void print() {
    cout << "DATA: ";
    for (int i = 0; i < size; i++) {
      cout << data[i] << ' ';
    }
    cout << endl;

    for (int i = 0; i < MAX_KEYS + 1; i++) {
      if (children[i])
        children[i]->print();
    }
  }

  int getData(int index) { return data[index]; }

  Node *search(int num) {
    if (this->children[0] == NULL)
      return this;

    int i;
    for (i = 0; i < size; i++) {
      if (data[i] == num)
        return this;
      if (num <= data[i]) {
        break;
      }
    }

    return children[i]->search(num);
  }

  void removeKey(int num) {
    int i;
    for (i = 0; i < size; i++) {
      if (num == data[i]) {
        break;
      }
    }
    for (int j = i; j < size - 1; j++) {
      data[j] = data[j - 1];
    }
    size--;
  }

  bool addKey(int num) {
    int i;
    for (i = size; i > 0; i--) {
      if (data[i - 1] > num) {
        data[i] = data[i - 1];
      } else
        break;
    }
    data[i] = num;
    return ++size != MAX_KEYS;
  }

  Node *split(int index) {
    Node *split = new Node(data[index + 1], NULL);

    // adding the right keys
    for (;;) {
    }

    // adding the right children
    for (int i = index + 1;; i++) {
    }

    size = index;
    return split;
  }

  bool addChildren(Node *node) {

    // TODO: we add the children here

    // FIX: do something with this boolean return value
    return true;
  }

  Node *getParent() { return parent; }
  Node *getChild(int index) { return children[index]; }
  int getSize() { return size; }
};

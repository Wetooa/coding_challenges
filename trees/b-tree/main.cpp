#include "tree24.h"

using namespace std;

int main(int argc, char *argv[]) {
  /* char choice; */
  /**/
  /* switch (choice) { */
  /* case '+': */
  /*   break; */
  /**/
  /* default: */
  /*   cout << "Invalid decision" << endl; */
  /* } */

  Tree24 *tree = new Tree24();
  tree->insert(25);
  tree->insert(100);
  tree->insert(75);
  tree->insert(50);
  /* tree->print(); */

  tree->search(25)->print();

  return 0;
}

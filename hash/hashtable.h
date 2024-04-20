#include <cstdlib>
#include <iostream>
using namespace std;

class HashTable {
  char *table;
  int N;
  int count;

  int a = 59;
  int b = 17;
  int p = 509;

  // Use the ASCII code of the character
  int hash_code(char key) { return key; }

  // This hash table uses a MAD compression function
  // where a = 59, b = 17, p = 509
  int compress(int code) { return (a * code + b) % p % N; }

  // Using the knowledge that a hash function is composed of two portions
  int hashfn(char key) { return compress(hash_code(key)); }

  int mod(int a) { return (a % N + N) % N; }

public:
  HashTable(int N) {
    table = new char[N];

    for (int i = 0; i < N; i++)
      table[i] = ' ';

    this->N = N;
    this->count = 0;
  }

  /* _ _ _ _ _ - - _ _ */

  int insert(char key) {
    if (count == N)
      return -1;

    int i = hashfn(key);
    int res = 0;

    while (table[i] != '?' && table[i] != ' ') {
      i = mod(i + 1);
      res++;
    }
    count++;
    table[i] = key;

    return res;
  }

  int search(char key) {
    if (count == 0)
      return -1;

    int i = hashfn(key);

    int res = 1;
    while (table[i] != ' ') {
      if (table[i] == key) {
        return res - 1;
      }
      res++;
      i = mod(i + 1);
    }

    return -res;
  }

  int remove(char key) {
    if (count == 0)
      return 0;

    int i = hashfn(key);
    int res = search(key);

    if (res < 0)
      return -1;

    i = mod(i + res);
    table[i] = '?';
    while (table[i] == '?' && table[mod(i + 1)] == ' ') {
      table[i] = ' ';
      i = mod(i - 1);
    }

    count--;
    return res;
  }

  void print() {
    for (int i = 0; i < N; i++) {
      cout << i << "\t";
    }
    cout << "\n";
    for (int i = 0; i < N; i++) {
      if (table[i] == ' ' || table[i] == '?')
        cout << "\t";
      else
        cout << table[i] << "\t";
    }
    cout << "\n";
  }
};

/* class DoubleHashing {} */
/* class QuadraticHashTable : public HashTable {} */

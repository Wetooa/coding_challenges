import java.util.TreeMap;

class CounterMap<K, V extends Number> extends TreeMap<Integer, Integer> {
  public void addCount(Integer key) {
    this.put(key, this.getOrDefault(key, 0) + 1);
  }

  public void removeCount(Integer key) {
    this.put(key, this.get(key) - 1);

    if (this.get(key) == 0)
      this.remove(key);
  }
}

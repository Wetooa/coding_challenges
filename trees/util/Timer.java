
class Timer {

  public void timeFunction(Function func) {
    long startTime = System.currentTimeMillis();

    func.apply();

    long endTime = System.currentTimeMillis();

    System.out.println("Runtime: " + (endTime - startTime) + "ms");
  }

}

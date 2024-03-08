
/**
 * Main
 */
public class Main {

  public static void main(String[] args) {
    Thread bg = new Thread(new BingoGame());
    bg.start();
  }
}

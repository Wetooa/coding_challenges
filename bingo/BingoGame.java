
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class BingoGame implements Runnable {

  static boolean[] result;
  static boolean isBingo;

  public BingoGame() {
    isBingo = false;
    result = new boolean[76];
    result[0] = true;
  }

  @Override
  public void run() {

    Scanner sc = new Scanner(System.in);
    int cnt = 5;
    char pattern = '+';

    // System.out.print("Enter number of players: ");
    // cnt = sc.nextInt();
    // sc.nextLine();
    //
    // System.out.print("Enter pattern: ");
    // pattern = sc.nextLine().charAt(0);

    List<BingoCard> cards = IntStream.range(0, cnt).boxed().collect(Collectors.toList()).stream()
        .map((id) -> new BingoCard(id + 1)).toList();
    List<Thread> patternCheckers = new ArrayList<>();

    cards.forEach((card) -> System.out.println(card));

    switch (pattern) {
      case '+':
        cards.forEach(card -> {
          patternCheckers.add(new Thread(new BingoPattern.BingoPatternPlus(card)));
          patternCheckers.getLast().start();
        });
        break;
      default:
        break;
    }

    int randomNumber;
    while (!isBingo) {
      while ((result[(randomNumber = (int) (Math.random() * 75))]))
        ;
      result[randomNumber] = true;

      System.out.println("Chosen number: " + randomNumber);

      for (int i = 1; i <= 75; ++i) {
        if (result[i])
          System.out.print(i + " ");
      }
      System.out.println();

      synchronized (BingoGame.result) {
        BingoGame.result.notifyAll();
        try {
          BingoGame.result.wait(100);
        } catch (InterruptedException e) {
          e.printStackTrace();
        }
      }
    }

    System.out.println("B I N G O");
    patternCheckers.forEach((patternChecker) -> patternChecker.interrupt());

    sc.close();

  }

}

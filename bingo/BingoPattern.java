
import java.util.ArrayList;
import java.util.List;

/**
 * BingoPattern
 */
public abstract class BingoPattern implements Runnable {

  BingoCard card;
  List<BingoChecker> bc;

  public BingoPattern(BingoCard card) {
    this.card = card;
  }

  @Override
  public void run() {
    List<Thread> thrds = bc.stream().map((checker) -> new Thread(checker)).toList();

    thrds.stream().forEach((thrd) -> thrd.start());

    for (Thread thrd : thrds) {
      try {
        thrd.join();
      } catch (InterruptedException e) {
        System.out.println(String.format("Card %d Loses..", card.id));
        return;
      }
    }

    System.out.println(String.format("Card %d Wins!!!", card.id));
    System.out.println(card);

    BingoGame.isBingo = true;
  }

  public static class BingoPatternPlus extends BingoPattern {

    public BingoPatternPlus(BingoCard card) {
      super(card);
      bc = new ArrayList<>();
      bc.add(new BingoChecker.BingoCheckerRow(card, 2));
      bc.add(new BingoChecker.BingoCheckerCol(card, 2));
    }

  }

}

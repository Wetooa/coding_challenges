
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
    this.bc = new ArrayList<>();
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
        thrds.forEach((t) -> t.interrupt());
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
      bc.add(new BingoChecker.BingoCheckerRow(card, 2));
      bc.add(new BingoChecker.BingoCheckerCol(card, 2));
    }

  }

  public static class BingoPatternHash extends BingoPattern {

    public BingoPatternHash(BingoCard card) {
      super(card);
      bc.add(new BingoChecker.BingoCheckerRow(card, 1));
      bc.add(new BingoChecker.BingoCheckerRow(card, 3));
      bc.add(new BingoChecker.BingoCheckerCol(card, 1));
      bc.add(new BingoChecker.BingoCheckerCol(card, 3));
    }
  }

  public static class BingoPatternE extends BingoPattern {

    public BingoPatternE(BingoCard card) {
      super(card);
      bc.add(new BingoChecker.BingoCheckerRow(card, 0));
      bc.add(new BingoChecker.BingoCheckerRow(card, 2));
      bc.add(new BingoChecker.BingoCheckerRow(card, 4));
      bc.add(new BingoChecker.BingoCheckerCol(card, 1));

    }
  }

  public static class BingoPatternJ extends BingoPattern {

    public BingoPatternJ(BingoCard card) {
      super(card);
      bc.add(new BingoChecker.BingoCheckerRow(card, 4));
      bc.add(new BingoChecker.BingoCheckerCol(card, 4));
    }

  }

}

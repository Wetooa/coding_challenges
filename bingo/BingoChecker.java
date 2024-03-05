
/**
 * BingoChecker
 */
public abstract class BingoChecker implements Runnable {

  BingoCard card;

  public BingoChecker(BingoCard card) {
    this.card = card;
  }

  public static class BingoCheckerRow extends BingoChecker {

    int row;

    public BingoCheckerRow(BingoCard card, int row) {
      super(card);
      this.row = row;
    }

    @Override
    public void run() {
      for (int col = 0; col < 5; col++) {
        while (!BingoGame.result[card.nums[row][col]]) {
          synchronized (BingoGame.result) {
            try {
              BingoGame.result.wait();
            } catch (InterruptedException e) {
            }
          }
        }
      }
    }

  }

  public static class BingoCheckerCol extends BingoChecker {

    int col;

    public BingoCheckerCol(BingoCard card, int col) {
      super(card);
      this.col = col;
    }

    @Override
    public void run() {
      for (int row = 0; row < 5; row++) {
        while (!BingoGame.result[card.nums[row][col]]) {
          synchronized (BingoGame.result) {
            try {
              BingoGame.result.wait();
            } catch (InterruptedException e) {
            }
          }
        }
      }
    }

  }

}

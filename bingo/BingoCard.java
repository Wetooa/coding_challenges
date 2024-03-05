
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class BingoCard {
  public int[][] nums;
  public int id;

  public BingoCard(int id) {
    this.nums = new int[5][5];
    this.id = id;

    for (int i = 0; i < 5; i++) {
      List<Integer> rand = IntStream.range(i * 15 + 1, (i + 1) * 15 + 1).boxed().collect(Collectors.toList());
      Collections.shuffle(rand);

      for (int j = 0; j < 5; ++j)
        nums[j][i] = rand.get(j);
    }

    nums[2][2] = 0;

  }

  @Override
  public String toString() {
    StringBuilder res = new StringBuilder("Card " + id + "\n");
    for (int i = 0; i < 5; i++) {
      for (int j = 0; j < 5; j++) {
        res.append(nums[i][j] + "     ");
      }
      res.append("\n");
    }
    return res.toString();
  }
}

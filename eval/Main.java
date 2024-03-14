
public class Main {

  public static void main(String[] args) {
    Eval eval = new Eval();
    System.out.println(eval.eval("4((-5+3*3)+2*4)/2*6"));
    System.out.println(eval.eval("4.3+3"));
    System.out.println(eval.eval("4.3+3.323"));
    System.out.println(eval.eval("(5.3/0)+5"));
    System.out.println(eval.eval("(24.34-3)+5"));

    Sequential sq = new Sequential();

    sq.onClickNumber(10);
  }
}

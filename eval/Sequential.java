
public class Sequential {

  Double number1;
  Double number2;
  Integer decimalPoint = 0;

  public void onClickAdd() {
    number1 += number2;
    number2 = 0d;
    decimalPoint = 0;
  }

  public void onClickSub() {
    number1 -= number2;
    number2 = 0d;
    decimalPoint = 0;
  }

  public void onClickMultiply() {
    number1 *= number2;
    number2 = 0d;
    decimalPoint = 0;
  }

  public void onClickDivide() {
    number1 /= number2;
    number2 = 0d;
    decimalPoint = 0;
  }

  public void onClickPeriod() {
    decimalPoint++;
  }

  public void onClickPercent() {
    number2 /= 100;
  }

  public void onClickNumber(Integer num) {
    if (decimalPoint > 0) {
      number2 += num / Math.pow(10, decimalPoint++);
    } else {
      number2 = number2 * 10 + num;
    }
  }

}

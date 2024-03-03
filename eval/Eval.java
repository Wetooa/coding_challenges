
package eval;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

/**
 * Eval
 */

public class Eval {

  private int index;

  private double eval(String equation) {

    List<Double> numbers = new ArrayList<>();
    boolean isNegative = false;
    double number = 0;

    for (int i = index; i < equation.length(); ++i) {
      if (equation.charAt(i) == ')') {
        break;
      } else if (equation.charAt(i) == '(') {

      }
    }

    return numbers.stream().mapToDouble(Double::doubleValue).sum();

  }

  public double simpleEval(String equation) {
    this.index = 0;
    return eval(equation);
  }

}

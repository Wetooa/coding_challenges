
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;
import java.util.regex.*;

public class Eval {
  List<Character> operationsList = new ArrayList<>(Arrays.asList(new Character[] { '+', '-', '*', '/' }));
  String isNumeric = "^\\d+$";

  private int getParenthesisPair(String equation, int index) {
    int counter = 0;
    for (int i = index; i < equation.length(); i++) {
      if (equation.charAt(i) == '(')
        counter++;
      else if (equation.charAt(i) == ')')
        counter--;
      if (counter == 0)
        return i;
    }
    return -1;
  }

  public double eval(String equation) {
    if (equation.length() == 0)
      return 0;
    if (Pattern.matches(isNumeric, equation))
      return Double.parseDouble(equation);

    List<Character> operations = new ArrayList<>();
    List<Double> numbers = new ArrayList<>();
    double number = 0;
    double decimal_point = 0;

    // tokenize symbols for easy parsing
    for (int i = 0; i < equation.length(); i++) {
      char s = equation.charAt(i);
      if (operationsList.contains(s)) {
        numbers.add(number);
        operations.add(s);
        number = 0;
        decimal_point = 0;
      } else if (s == '(') {
        if (number > 0) {
          numbers.add(number);
          operations.add('*');
        }
        number = 0;
        decimal_point = 0;
        int next_index = getParenthesisPair(equation, i);
        number = eval(equation.substring(i + 1, next_index));
        i = next_index;
      } else if (Character.isDigit(s)) {
        if (decimal_point > 0) {
          number += (s - '0') / (Math.pow(10, decimal_point++));
        } else {
          number = number * 10.0 + s - '0';
        }
      } else if (s == '.') {
        decimal_point++;
      } else if (s == '%') {
        number /= 100;
      } else {
        // Error lol
      }
    }
    numbers.add(number);

    // evaluate
    Stack<Double> stack = new Stack<>();
    stack.add(numbers.getFirst());
    for (int i = 1; i < numbers.size(); i++) {
      switch (operations.get(i - 1)) {
        case '+':
          stack.add(numbers.get(i));
          break;
        case '-':
          stack.add(numbers.get(i) * -1);
          break;
        case '*':
          stack.add(stack.pop() * numbers.get(i));
          break;
        case '/':
          stack.add(stack.pop() / numbers.get(i));
          break;
        default:
          break;
      }
    }

    return stack.stream().reduce((n, acc) -> n + acc).get();
  }

}

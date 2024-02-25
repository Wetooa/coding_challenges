
import java.util.Scanner;

/**
 * Main
 */
public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    try {
      BinaryTree t = new BinaryTree();

      while (true) {
        System.out.print("\nSelect choice: ");

        switch (sc.nextLine().charAt(0)) {
          case 'a':
            System.out.print("Select what number to add: ");
            int add = sc.nextInt();
            sc.nextLine();
            t.insert(add);
            break;
          case 'r':
            System.out.print("Select what number to remove: ");
            int remove = sc.nextInt();
            sc.nextLine();
            t.remove(remove);
            break;
          case 'p':
            System.out.println(t);
            break;
          default:
            System.out.println("Invalid choice!");
        }
      }

    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      sc.close();
    }
  }
}

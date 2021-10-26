import java.util.Scanner;

public class calc {

    public static void main(String[] args) {

        Scanner myObj = new Scanner(System.in);

        System.out.println("Enter the operator");
        char operator = myObj.next().charAt(0);

        System.out.println("Enter first num");
        int num1 = myObj.nextInt();
        System.out.println("Enter second num");
        int num2 = myObj.nextInt();

        switch (operator) {
        case '+':
            System.out.println(num1 + num2);
            break;
        case '-':
            System.out.println(num1 - num2);
            break;
        case '*':
            System.out.println(num1 * num2);
            break;
        case '/':
            System.out.println(num1 / num2);
            break;
        case '%':
            System.out.println(num1 % num2);
            break;

        default:
            System.out.println("Goodbye");
            break;
        }

    }

}

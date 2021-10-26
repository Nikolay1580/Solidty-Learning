import java.util.Scanner;

public class morgage {

    public static void main(String[] args) {

        Scanner myObj = new Scanner(System.in);

        System.out.print("How much you investing");
        double payment = myObj.nextDouble();
        System.out.print("What is your rate");
        double rate = myObj.nextDouble() / 100;
        System.out.print("for how many years");
        int time = myObj.nextInt();

        double m = payment * (rate * (1 + time) / (Math.pow(1 + rate, time) - 1));

        System.out.println("Your total will end up being " + m);
    }

}

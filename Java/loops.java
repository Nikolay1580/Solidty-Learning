public class loops {

    public static void main(String[] args) {
        // for loops
        for (byte i = 0; i < 5; i++) {
            System.out.println(i);
        }

        byte j = 0;
        // while loop
        while (true) {
            System.out.println("j = " + j);
            if (j == 3)
                break;
            j++;
        }

        boolean x = false;
        // do while loops
        do {
            System.out.println("x is " + x);
        } while (x == true);

        // for each loops to loop through array
        String[] fruits = { "Apple", "Banna", "hello" };
        // base the ietem depending on the array type
        for (String fruit : fruits) {
            System.out.println(fruit);
        }

    }

}

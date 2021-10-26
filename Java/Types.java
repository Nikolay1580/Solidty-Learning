class Types {
    public static void main(String[] args) {
        // variable bellow 120
        byte temp = 40;
        // declare variable. In java you can use an underscore for every 3 digits to
        // make the number easier to read
        int population = 134_345_445;
        // if num too big we use long and after the number we need to specify that it is
        // long by using L
        long largeNum = 234_344_478_989L;
        // decimal
        float pie = 3.41F;
        // a lot of decimal places
        double extendedPie = 3.412423423;
        // char is one single text can also be one letter
        char Acronym = 'A';
        // boolian is true or flase
        boolean isMale = true;
        System.out.println(isMale);

        // doing constants, they don't change throughout your program
        // constants should always be fully capitalised
        final float PIE = 3.14F;

    }

}
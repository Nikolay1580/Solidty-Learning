class strings {
    public static void main(String[] args) {
        String name =  "Nikolay";
        System.out.println(name);
        name = name + " !!";
        System.out.println(name);
        // checks the length of characters of the string 
        System.out.println(name.length());
        // returns index of first occurence 
        System.out.println(name.indexOf('k'));
    }
}
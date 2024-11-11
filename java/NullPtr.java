public class NullPtr {
    public static void main(String[] args) {
        String A= null;
        try {
            System.out.println("Length of String = " + A.length());
        } catch (Exception e) {
            System.out.println("String has no length");
        }
    }
}

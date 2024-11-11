import java.io.*;
import java.lang.*;

public class NumberFrmt {
  
    public static void main(String[] args) {
    String a = "HelloWorld";
    try {
        int p = Integer.parseInt(a);
    } catch (NumberFormatException e) {
        System.out.println("String Cannot be Converted to Inteager");
    }
    }
    
}

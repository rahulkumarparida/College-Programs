import java.io.*;
import java.lang.*;

public class ArithmeticExtn {
    
    void Divide(int a , int b){
        try {
            System.out.println("The division is "+ a/b);
        } catch (ArithmeticException e) {
            System.out.println("Dviding Error");
        }
    }
    public static void main(String[] args) {
        ArithmeticExtn a = new ArithmeticExtn();
        a.Divide(20, 10);
        a.Divide(20, 0);
    }
    
}


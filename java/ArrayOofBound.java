import java.io.*;
import java.lang.*;

public class ArrayOofBound {
    public static void main(String[] args) {
        int A[] = new int[10];
        try {
            A[20]=7;
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("The provided index is out of bound");    
        }
    }
}

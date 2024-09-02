import java.io.*;
import java.util.*;
public class overloadingconstructor {
    int real;
    int imaginary;
    public overloadingconstructor(){
        real= 5;
        imaginary= 10;
    }
    public overloadingconstructor(int r){
        real = r;
        imaginary= 12;

    }
    public overloadingconstructor(int r , int i){
        real = r;
        imaginary= i;
    }
    public void show(){
        System.out.println((real+"+"+imaginary + " = "+ real+imaginary ));
    }
    public static void main(String[] args) {
        overloadingconstructor A = new overloadingconstructor();
        overloadingconstructor B = new overloadingconstructor(4);
        overloadingconstructor C = new overloadingconstructor(5,6);
        A.show();
        B.show();
        C.show();
    }
}


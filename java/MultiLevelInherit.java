import java.io.*;
import java.util.*;

class Grandfather {
    String Gnm;
    int Gage;

    void getdata(String nm, int a) {
        Gnm = nm;
        Gage = a;
    }

    void dis() {
        System.out.println("GrandFather's name is " + Gnm + " \nGrandFather's age is " + Gage);
    }
}

class Father extends Grandfather {
    String Fnm;
    int age;

    void getdata(String nm, int a) {
        Fnm = nm;
        age = a;
    }

    void display() {
        System.out.println("Father's name is " + Fnm + " \nFather's age is " + age);
    }
}

class Son extends Father {
    String Snm;
    int Sage;

    void get(String A, int B, String C, int D, String E, int F) {
        Fnm = A;
        age = B;
        Snm = C;
        Sage = D;
        Gnm = E;
        Gage = F;
    }

    void disp() {
        dis();
        display();
        System.out.println("Son's name is " + Snm + " \nSon's age is " + Sage);
    }
}

public class MultiLevelInherit {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.print("Enter GrandFather's Name: ");
        String Gnm = s.nextLine();
        System.out.print("Enter GrandFather's age: ");
        int Gage = s.nextInt();
        s.nextLine(); // Consume the newline

        System.out.print("Enter Father's Name: ");
        String Fnm = s.nextLine();
        System.out.print("Enter Father's age: ");
        int age = s.nextInt();
        s.nextLine(); // Consume the newline

        System.out.print("Enter Son's name: ");
        String Snm = s.nextLine();
        System.out.print("Enter Son's age: ");
        int Sage = s.nextInt();

        Son k = new Son();
        k.get(Fnm, age, Snm, Sage, Gnm, Gage);
        k.disp();
        s.close(); // Close the scanner
    }
}

// Enter GrandFather's Name: Mahendra
// Enter GrandFather's age: 77
// Enter Father's Name: Bibhisan
// Enter Father's age: 49
// Enter Son's name: Rahul
// Enter Son's age: 20
// GrandFather's name is Mahendra 
// GrandFather's age is 77
// Father's name is Bibhisan 
// Father's age is 49
// Son's name is Rahul 
// Son's age is 20
import java.io.*;
import java.util.*;

interface Rate {
    float rint();
}

class RBI implements Rate {
    public float rint() {
        return 3.0f;
    }
}

class SBI implements Rate {
    public float rint() {
        return 3.5f;
    }
}

class IOB implements Rate {
    public float rint() {
        return 3.7f;
    }
}

public class InterfaceRate {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the name for the bank: ");
        String bn = sc.nextLine();

        if (bn.equals("RBI")) {
            RBI r = new RBI();
            System.out.println("Interest rate is " + r.rint());
        } else if (bn.equals("SBI")) {
            SBI s = new SBI();
            System.out.println("Interest rate is " + s.rint());
        } else if (bn.equals("IOB")) {
            IOB i = new IOB();
            System.out.println("Interest rate is " + i.rint());
        } else {
            System.out.println("Error 404 Bank NOT FOUND");
        }

        sc.close(); // It's good practice to close the scanner
    }
}
// OUTPUT
// Enter the name for the bank : 
// SBI
// Error 404 Bank NOT FOUND
// Enter the name for the bank: 
// IOB
// Interest rate is 3.7
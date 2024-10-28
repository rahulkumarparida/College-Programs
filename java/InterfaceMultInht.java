import java.util.*;

interface Rate {
    double R = 12; 
}

interface SI {
    double Simple = 0; 
}

class Calculates implements Rate, SI {
    double P, T;

    public Calculates(double Pri, double Ti) { 
        this.P = Pri;
        this.T = Ti;
    }

    public double SimpleInterest() { 
        return (P * R * T / 100);
    }
}

public class InterfaceMultInht {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Principle,Time:");
        double P = sc.nextDouble(); 
        double T = sc.nextDouble();

        Calculates calc = new Calculates(P, T); 
        double simp = calc.SimpleInterest();
        System.out.println("Simple interest is " + simp);
        System.out.println("In total You have to pay : " +(simp+P)); 

    }
}
// OutPut
// Enter Principle, Time:
// 1000 2.5      
// Simple interest is 300.0
// In total You have to pay : 1300.0
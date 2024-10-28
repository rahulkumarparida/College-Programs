import java.util.*;

interface Rate {
    double r = 0; 
}

interface SI {
    double Simple = 0; 
}

class Calculates implements Rate, SI {
    double P, T, R;

    public Calculates(double Pri, double Ti, double R) { 
        this.P = Pri;
        this.T = Ti;
        this.R = R; 
    }

    public double SimpleInterest() { 
        return (P * R * T / 100);
    }
}

public class InterfaceMultInht {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Principle, Rate, Time:");
        double P = sc.nextDouble(); 
        double R = sc.nextDouble();
        double T = sc.nextDouble();

        Calculates calc = new Calculates(P, T, R); 
        double simp = calc.SimpleInterest();
        System.out.println("Simple interest is " + simp);
        System.out.println("In total You have to pay : " +(simp+P)); 

    }
}
// OutPut
// Enter Principle, Rate, Time:
// 1000 2.5 12      
// Simple interest is 300.0
// In total You have to pay : 1300.0
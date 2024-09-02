/**
 * performtasks
 */
import java.io.*;
import java.util.*;
public class performtasks {
    // to check if a number is palidrome or not
        public void palidrome(int n){
            int m= n;
            int rev = 0;
            while (n>0) {
              int  R = n%10;
              rev = R;
             rev = rev*10+R;
             n=n/10;
            }
            if(m==rev){
            System.out.println("palidrome");
            
            }
            else{
                System.out.println("Not a Palidrome");
            }

        }
        public void prime(int n){
            if (n>1) {
                for (int i = 2; i<=(n/2); i++) {
                    if(n%i==0){
                        System.out.println("Composite Number");
                        break;
                    }
                    if (i>n/2) {
                        System.out.println("Prime Number");
                    }
                }
            }
            else{
                System.out.println("Enter a valid numebr");
            }
                
            }
        public void fibo(int n){
            int a = 0 , b=1 , i=2 ;
            do {
                int c = a+b;
                System.out.println(c);
                a=b;
                b=c; 
                i++;
            } while (i<n);

        }
        public void fact(int n){
            int f= 1;
            for (int i = n; i> 0; i--) {
             f = f*i;
            
            }
            System.out.println("Factorial will be " + f);   
        }
        public static void main(String[] args) {
            Scanner sc= new Scanner(System.in);
            System.out.println("Enter a number : ");
            int n = sc.nextInt();
            performtasks t = new performtasks();
            t.palidrome(n);
            t.prime(n);
            t.fibo(n);
            t.fact(n);

        }
    
    }

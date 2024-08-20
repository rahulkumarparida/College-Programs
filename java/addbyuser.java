import java.io.*;
import java.util.*;
class addbyuser{
   double a,b;
   void getdata()
   {
   Scanner s= new Scanner(System.in);
   System.out.println("Enter a number:");
   a=s.nextDouble();
   System.out.println("Enter 2nd number:");
   b=s.nextDouble();
   }
   double process()
   {
   return(a+b);
   }
   void display()
   {
   System.out.println("sum=" +process());
   }
   public static void main(String args[])
    {
    addbyuser obj=new addbyuser();
    obj.getdata();
    obj.display();
    }
}

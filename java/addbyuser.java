import java.io.*;
import java.util.*;
class addbyuser{
   double 4a,b;
   void getdata()
   {
   Scanner S= new Scanner(System.in);
   System.out.println("Enter a number:");
   a=S.nextDouble();
   System.out.println("Enter 2nd number:");
   b=S.nextDouble();
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

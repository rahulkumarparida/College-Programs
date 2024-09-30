import java.io.*;
import java.util.*;
class father{
   String Fnm;
   int age;
   void getdata(String nm , int a){
      Fnm = nm;
      age = a;

   }
   void display(){
      System.out.println("Father's name is "+ Fnm + " "+" \nFather's age is "+age+" ");
   }
}
class son extends father{
   String Snm;
   int Sage;
   void get(String A , int B,String C , int D){
      Fnm = A;
      age = B;
      Snm = C;
      Sage = D;
   }
   void disp(){
      display();
      System.out.println("Son's name is "+ Snm + " "+" \nSon's age is "+Sage+" ");
   }
}
 class single {
  public static void main(String[] args) {
   Scanner s = new Scanner(System.in);
   System.out.println(" Enter Father's Name :- ");
   String Fnm = s.nextLine();
   System.out.print("Enter Father's age :- ");
   int age = s.nextInt();
   System.out.println("Enter Son's name :- ");
   String Snm = s.nextLine();
   s.nextLine();
   System.out.print("Enter Son's age :- ");
   int Sage = s.nextInt();
   son k = new son();
   k.get(Fnm,age,Snm,Sage);
   k.disp();
  }  

   }

/* Output
 *  Enter Father's Name :- 
Bibhisan Parida
Enter Father's age :- 49
Enter Son's name :- 
Rahul Kumar Parida
Enter Son's age :- 20
Father's name is Bibhisan Parida  
Father's age is 49 
 */
import java.io.*;
import java.util.*;
class bankaccount{
String cn;
int an;
int b;
int w;
void getdata()
{
Scanner S = new Scanner(System.in);
System.out.println("*********HELLO!! WELCOME TO SOUL-SOCIETY BANK*********");
System.out.println("To Create an account Please Enter Your Name:-");
cn=S.nextLine();
System.out.println("Please Enter Some Desired Numbers:-");
an=S.nextInt();
System.out.println("Enter the Amount of Money you have to deposit:--$");
b=S.nextInt();
System.out.println("THANK YOU FOR OPENING AN ACCOUNT IN SOUL-SOCIETY BANK");
System.out.println("Enter the Amount of Money you want to Withdraw:--$");
w=S.nextInt();
}
int with(){
return(b-w);
}
void display() {
System.out.println("-------YOUR BANK DETAILS-------");
System.out.println("Your Name is " +cn);
System.out.println("Your Balance is $" +with());
System.out.println("THANK YOU FOR USING OUR BANK ;]");
}
public static void main(String args[]){
bankaccount obj=new bankaccount();
obj.getdata();
obj.display();
}
}

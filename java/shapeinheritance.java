import java.io.*;
import java.util.*;
class profile{
String name;
int age , percentage;

public void get(int x , int y , String nm){
    name = nm;
    age= x;
    percentage = y;
    System.out.println("Name :"+ name);
    System.out.println("Age :"+age);
    System.out.println("Percentage :"+percentage);
}


}
class enggineering extends profile{
    public void display(int x, int y , String nm){
        super.get(percentage, age, name);
        System.out.println("Congratulation's you are eligible for Engineering");
    }
}
class medical extends profile{
    public void display(int x, int y , String nm){
        super.get(percentage, age, name);
        System.out.println("Congratulation's you are eligible for Medical");
    }
}
class agriculture extends profile{
    public void display(int x, int y , String nm){
        super.get(percentage, age, name);
        System.out.println("Congratulation's you are eligible for Agriculture");
    }
}


public class shapeinheritance {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Provide YOUR Name , Age , Percentage (RESPECTIVELY)");
        String nam= sc.nextLine();
        int age = sc.nextInt();
        int percent = sc.nextInt();
        if (percent >= 95) {
            medical m = new medical();
            m.display(age, percent, nam);
        } else if (percent >= 50) {
            enggineering e = new enggineering();
            e.display(age, percent, nam);
        }else{
            agriculture a = new agriculture();
            a.display(age, percent, nam);
        }
    }
}

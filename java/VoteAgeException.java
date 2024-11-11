import java.io.*;
import java.util.*;
import java.lang.*;

public class VoteAgeException {
    public void check(String nm , int ag ) throws IOException{
        if(ag>18){
            System.out.println(nm+" is Eligible to vote");
        }else{
            throw new IOException("Age Must be 18 or 18+ to vote");
        }
    }
    public static void main(String[] args) {
        Scanner s= new Scanner(System.in);
        System.out.println("Enter Name :- ");
        String name= s.nextLine();
        System.out.println("Enter age :- ");
        int age = s.nextInt();
        VoteAgeException v = new VoteAgeException();
        try {
            v.check(name, age);
        } 
        catch (IOException t){
           System.out.println("I caught an Exception");
        }
        finally{
            System.out.println("Age is less than 18");
        }
    }
}

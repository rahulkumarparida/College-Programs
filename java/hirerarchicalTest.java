import java.io.*;
import java.util.*;
class  shape{
float xco,yco,rad,side;
    
}
class rectangle extends shape{
    public void get(float x,float y){
        xco= x;
        yco=y;
    }
    public void area(){
        System.out.println("Area of the rectangle is "+ (xco*yco));
    }
}
class circle extends shape{
    public void get(float r){
       rad = r;
       
    }
    public void area(){
        System.out.println("Area of the circle is "+ (3.14*(rad*rad)));
    }
}
class square extends shape{
    public void get(float s){
     side= s;
    }
    public void area(){
        System.out.println("Area of the square is "+ (side*side));
    }
}

public class hirerarchicalTest {
 public static void main(String[] args) {
    rectangle r = new rectangle();
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the length and breadth :- ");
    float l = sc.nextFloat();
    float b = sc.nextFloat();
    r.get(l, b);
    r.area();
    
        circle c = new circle();
    System.out.println("Enter the radius :- ");
    float rad = sc.nextFloat();
    c.get(rad);
    c.area();
    
    square sq = new square();
    System.out.println("Enter the side :- ");
    float side = sc.nextFloat();
    sq.get(side);
    sq.area();

}
// output
// Enter the length and breadth :- 
// 10 12
// Area of the rectangle is 120.0
// Enter the radius :- 
// 25
// Area of the circle is 1962.5
// Enter the side :- 
// 55
// Area of the square is 3025.0


    
}

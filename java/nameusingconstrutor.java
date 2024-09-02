public class Nameusingconstructor {
    String name;
    int age;
    String branch;
    public Nameusingconstructor(){
      name = "Rahul Kumar Parida";
      age = 20;
      branch = "CSE";
    }
  
    public void show(){
        System.out.println("My name is "+name);
        System.out.println("I am "+age+" Years old");
        System.out.println("My Branch is "+branch);

    }
    public static void main(String[] args) {
        Nameusingconstructor A = new Nameusingconstructor();
        A.show();
    }
}


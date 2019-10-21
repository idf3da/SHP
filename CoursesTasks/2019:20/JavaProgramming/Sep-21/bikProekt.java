import java.util.Scanner;

public class Grid{
    public String[] icons = new String[10];
        
    public void print(){
        for (byte i = 0; i < 10; i++){
            System.out.print(icons[i]);
        }
    }
}

class Play{
    public static void main(String argv[]){
        Scanner scanner = new Scanner(System.in);
        int n;
        n = scanner.nextInt();
        if (n > 0 && n < 11){
            System.out.println(n);
            Grid 
        }
        else{
            System.out.print("Please input from 1 to 10.");
        }

        /////////////////////
        scanner.close();   
        /////////////////////
    }
}
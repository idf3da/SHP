import java.util.Scanner;
     
class Sum
{
   public static void main(String args[])
   {
      float a, b, c;
 
      Scanner in = new Scanner(System.in);
     
      a = in.nextFloat();
      b = in.nextFloat();
      c = in.nextFloat();

      if (a + b == c){
          System.out.println("YES");
      }
      else{
          System.out.print("NO");
      }
      System.out.print((a + b));
   }
}
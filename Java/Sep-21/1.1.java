import java.util.*;
import java.lang.*;

class Rextester
{  
    public static void main(String args[])
    {
        for (int i = 1; i < 10; ++i) {
            for (int q = 1; q < 10; ++q) {
                System.out.print(i * q);
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}
import java.util.Arrays;
import java.util.Scanner;

class C{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] pos = new int[0];
        int[] neg = new int[0];
        
        for (int i = 0; i < n; i++) {
            int input = scan.nextInt();
            if (input < 0) {
                neg = Arrays.copyOf(neg, neg.length + 1);
                neg[neg.length - 1] = input;
            } else {
                pos = Arrays.copyOf(pos, pos.length + 1);
                pos[pos.length - 1] = input;
            }
        }
        for (int elem: neg){
            System.out.print(elem + " ");
        }
        for (int elem: pos){
            System.out.print(elem + " ");
        }
    }
}
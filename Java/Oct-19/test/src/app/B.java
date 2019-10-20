package app;

import java.util.Scanner;

class B{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            int input = scan.nextInt();
            if (input % 2 != 0) {
                arr[i] = input;
            } else {
                i--;
            }
        }
        
        for(int elem: arr) {
            System.out.print(elem + " ");
        }

    }
}
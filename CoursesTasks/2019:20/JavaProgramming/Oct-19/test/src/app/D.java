package app;

import java.util.Arrays;
import java.util.Scanner;

class E{

    public static int abs(int a) {
        if (a < 0) {
            return -a;
        } else {
            return a; 
        }
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        int k, n, nD, o, ded = 0, mem = 0;
        int[] pand = new int[num];
        int[] place = new int[num];
        int[] error = new int[num];
        int[] eror = new int[num];

        for (int i = 0; i < n; i++) {
            pand[i] = scan.nextInt();
        }
        for (int i = 0; i < n; i++) {
            place[i] = scan.nextInt();
            if (pand[i] >= place[i]) {
                n++;
                error[n] = pand[i] - place[i];
            }
        }
        for (int i = 0; i < n; i++) {
            if (place[i] >= pand[i]) {
                nD++;
                eror[nD] = place[i] - pand[i];
            }
        }
        for (int i = 0; i < n; i++) {
            ded += error[i];
            mem += error[i];
        }

        System.out.Print(ded);
        System.out.Print(abs(ded - mem));

        

    }
}
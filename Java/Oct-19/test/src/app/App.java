package app;
import java.util.Arrays;
import java.util.Random;

public class App {
    public static void main(String[] args) {
        int arr[] = new int[10];
        Random gena = new Random(System.currentTimeMillis());
        for(int i =0; i < arr.length; i++){
            arr[i] = gena.nextInt(101);
        }
        for(int elem: arr){
            System.out.print(elem + " ");
        }
        int x = arr[gena.nextInt(arr.length)];
        Arrays.sort(arr);
        System.out.println();

        for(int elem: arr){
            System.out.print(elem + " ");
        }
        
        System.out.println();
        System.out.println("Searching for: " + x);
        System.out.println(x + " position is: " + Arrays.binarySearch(arr, x));
    }
}
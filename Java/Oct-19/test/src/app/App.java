package app;
import java.util.Arrays;

public class App {
    public static void main(String[] args) {
        int arr1[] = new int[10];
        int arr2[] = new int[10];
        
        Arrays.fill(arr1, 0);
        Arrays.fill(arr2, 0);
        
        System.out.println(Arrays.equals(arr1, arr2));
    }
}
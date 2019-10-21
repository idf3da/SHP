import java.util.Scanner;

class B{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] arr1 = new int[n];
        int[] arr2 = new int[n];

        for (int i = 0; i < n; i++) {
            int input = scan.nextInt();
            arr1[i] = input;
        }

        int c = 0;

        for (int elem: arr1){
            if (elem % 2 != 0){
                arr2[c] = elem;
                c++;
            }
        }

        for (; c < n; c++) {
            arr2[c] = 0;
        }
        
        for(int elem: arr2) {
            System.out.print(elem + " ");
        }

    }
}
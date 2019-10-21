package app;
import java.util.Random;

public class test {
    //Inf req 32bits
    public static void main(String[] args) {
        //10len support                                     @
        int[] inputData = DataInStream.GetData();

        if (DataValidator.isOkay(inputData))
            DataOut(inputData);
    }

    static void DataOut(int[] data){
        for (byte i = 0; i < data.length; i++){
            System.out.println(data[i]);
        }
        //All 19                                            @
    }
}

class DataInStream {
    public static int[] GetData(){
        int[] data = new int[10];
        for (byte i = 0; i < data.length; i++){
            Random rnd = new Random();
            data[i] = rnd.nextInt(-2147483648, 2,147,483,647);
        }
        return data;
        //RandInt32                                          @
    }
}

class DataValidator {
    public static boolean isOkay(int[] data){
        long sum = 0;
        for (byte i = 0; i < data.length - 1; i++){
            sum += data[i];
        }
        if (sum == data[data.length]){
            return true;
        }
        else{
            return false;
        }
         
        //10th packet = contSum ( p1 + p2... + p9 == p10 )   @
    }
}



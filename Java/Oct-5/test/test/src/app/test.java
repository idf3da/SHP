package app;

public class test {
    public static void main(String[] args) { 
        int inputData = DataInStream.GetData();
        if (DataValidator.isOkay(inputData))
            DataOut(inputData);
    }

    static void DataOut(int data){
        System.out.println(data);
    }
}

class DataInStream {
    public static int GetData(){
        return 0;
    }
}

class DataValidator {
    public static boolean isOkay(int inputData){
        return true;
    }
}



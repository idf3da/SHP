public class test {
    public static void main(String[] args){
        nextUpdate = System.nanoTime();
        while (true){
            if (TimeToUpdate(System.nanoTime())){
                Update();
            }
        }
    }
    static long nextUpdate = 0;
    public static boolean TimeToUpdate(long currentTime) {
        if (currentTime > nextUpdate){
            nextUpdate += 60;
            return true;
        }
        return false;
    }
    public static void Update(){
        System.out.println("Ping");
    }
}
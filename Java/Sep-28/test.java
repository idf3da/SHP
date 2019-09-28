public class test {
    static int worldSize = 255;
    static Char[] World;
    static long nextUpdate = 0;
    public static Obj1D[] objs;
    public static void main(String[] args){
        World = new char[worldSize];
        objs = new char[worldSize];
        for (int i = 0; i < worldSize; i++){ World[i] = "_"; }
        nextUpdate = System.nanoTime();
        while (true){
            Obj1D newObj = new Obj1D();
            if (TimeToUpdate(System.nanoTime())){
                Update();
                Draw();
            }
        }
    }
    public static boolean TimeToUpdate(long currentTime) {
        if (currentTime > nextUpdate){
            nextUpdate += 1000000000;
            return true;
        }
        return false;
    }
    public static void Update() {
        Obj1D newObj = new Obj1D();
        System.out.println("Ping");
    }
    public static void Draw() {
        for (int i = 0; i < worldSize; i++){
            if (objs[i] == null){
                System.out.println("_");
            } else {
                objs[i].Draw();
            }
        }
        System.out.println();
    }
}
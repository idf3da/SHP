import java.util.Random;
import Java.util.random;

public class Obj1D {
    static byte superType = 5;

    byte type;
    int possition;

    public byte GetType() { return type; }
    public int GetPossition(){ return possition ;}
    public Obj1D(){
        Random rnd = new Random();
        type = (byte) rnd.nextFloat() * 10;
        possition = (int)(rnd.nextFloat() * test.worldSize);
    }
    public void Update(){
        type++;
        if (type > 9) {

        }
    }
    public void Draw(){

    }
}
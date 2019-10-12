package app;

public class App{
    public static void main(String[] args) {
        A a = new A();
        B b = new B();
        C c = new C();
        D d = new D();
        
        d.cheb();
        d.lol();
        
    }
}

class A {
    void kek(){
        System.out.println("Kek");
    }
}

class B {
    void lol(){
        System.out.println("Lol");
    }
}

class C {
    void arb(){
        System.out.println("Arb");
    }
}

class D extends B {
    void cheb(){
        System.out.println("Cheb");
    }
}
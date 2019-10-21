package Bank;

class Singleton {
    private static Singleton instance;
    public String value;

    private Singleton(String value) {
        this.value = value;
    }

    public static Singleton getInstance(String value) {
        if (instance == null) {
            instance = new Singleton(value);
        }
        return instance;
    }
}

public class BankClient {
    private String CardNumber;
    private long Balance;
    private String cardType;

    public String getCardNumber() {
        return CardNumber;
    }
    
    public long getBalance() {
        return Balance;
    }

    public void setBalance(long balance) {
        this.Balance = balance;
        if (this.cardType == "Debit") {
            if (balance < 0) {
                this.Balance = 0;
            }
        }
    }

    public BankClient(String CardNumber, String cardType){
        this.CardNumber = CardNumber;
        this.Balance = 0;
        this.cardType = cardType;
    }

}

class Kek{
    public static void main(String[] args){
        BankClient bc = new BankClient("123", "Debit");
        Singleton st = new ;
    }
}
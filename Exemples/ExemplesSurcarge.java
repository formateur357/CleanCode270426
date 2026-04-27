public class Money {
    private double amount;

    public double getAmount() {
        return amount;
    }

    public void setAmount(double amount) {
        if (amount < 0) {
            throw new IllegalArgumentException();
        }
        this.amount = amount;
    }
}

money.setAmount(150);
money.getAmount();
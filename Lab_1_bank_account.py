class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        """Create a new bank account."""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount: float) -> str:
        """Deposit money into the account."""
        if amount <= 0:
            return "Deposit amount must be positive."
        
        self.balance += amount
        return f"Deposited ₹{amount:.2f}. New balance: ₹{self.balance:.2f}"

    def withdraw(self, amount: float) -> str:
        """Withdraw money from the account."""
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient funds."
        
        self.balance -= amount
        return f"Withdrew ₹{amount:.2f}. New balance: ₹{self.balance:.2f}"

    def check_balance(self) -> str:
        """Return the current account balance."""
        return f"Account holder: {self.account_holder}\nCurrent balance: ₹{self.balance:.2f}"

    def __str__(self) -> str:
        return self.check_balance()


# ---------- Example usage ----------
if __name__ == "__main__":
    # Create an account
    account = BankAccount("Rahul Sharma", 5000)

    print(account.check_balance())
    print()

    # Deposit money
    print(account.deposit(2500))
    print()

    # Withdraw money
    print(account.withdraw(1200))
    print()

    # Try to withdraw more than available
    print(account.withdraw(10000))
    print()

    # Final balance
    print(account.check_balance())
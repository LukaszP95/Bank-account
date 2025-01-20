class BankAccount:


    def __init__(self, owner: str):
        self.owner = owner
        self.balance = 0

    def get_balance(self) -> float:
        return self.balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"{amount} was paid into the account.")

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} was withdrawn from the account.")
        else:
            raise ValueError(f"{amount} amount is too high.")


if __name__ == "__main__":

    account = BankAccount("Alice")

    print(f"account owner: {account.owner} \naccount balance: {account.balance}")

    account.deposit(500)
    print("Balance:", account.get_balance())
    account.deposit(1500)
    print("Balance:" , account.get_balance())
    account.withdraw(500)
    print("Balance:" , account.get_balance())
    account.deposit(400)
    print("Balance:", account.get_balance())
    account.withdraw(200)
    print("Balance:" , account.get_balance())
    print(f"account owner: {account.owner} \naccount balance: {account.balance}")

"""Klasa Konto Bankowe

Cel:
Zaprojektuj klasę BankAccount, która będzie symulować podstawowe operacje związane z kontem bankowym.
 Zadanie ma na celu praktyczne zastosowanie programowania obiektowego, w tym pracy z atrybutami, metodami oraz prostą logiką biznesową.

Pola:
- owner: str - imie i nazwisko wlasciciela
- balance: float, domyślnie ma wartość 0 - stan konta

Metody:
- get_balance() - zwraca Ci aktualny stan konta
- deposit() - wpłaca pieniądze na konto
- withdraw() - wypłaca pieniądze z konta

Standardowo po if _name_ ... tworzysz instancje konta, i wywołujesz kilka razy różne metody, żeby sprawdzić czy dziala poprawnie
to dodasz walidacje:
- wprowadzona kwota nie może być ujemna, np. nie możesz wpłacić -200 zł
- jeśli na koncie jest 100 zł, to nie możesz wypłacić 150zł - powinien zostać wyrzucony wyjątek"""


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


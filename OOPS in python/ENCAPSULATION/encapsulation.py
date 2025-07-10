'''✅ 🔶 Encapsulation (क्लास के अंदर data छुपाना और control देना)
📘 Definition (Simple Hinglish):
Encapsulation ka matlab hai data ko छुपाना (hide karna) aur usse access karne ke liye controlled methods dena.

Isme hum class ke variables ko private banate hain, taaki unhe direct bahar se access na kiya ja sake.

🔒 Real-Life Example:
Socho ek ATM Machine:

Tum directly bank database access nahi kar sakte.

Tumhare paas interface (screen + buttons) hote hain.

Uske through tum balance dekhte ho, paisa nikaalte ho, etc.

Yahi Encapsulation hai.

'''


# ✅ BankAccount class with encapsulation
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # 🔒 private variable

    # ✅ Method to deposit amount
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Please enter a valid amount!!!")

    # ✅ Method to withdraw amount
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Enter a valid amount!")

    # ✅ Method to access private balance safely
    def get_balance(self):
        return self.__balance


# ✅ Object creation and usage (outside the class)
acc1 = BankAccount("Keshav", 20000)

acc1.deposit(1000)       # ₹1000 deposit
acc1.withdraw(500)       # ₹500 withdraw

# ✅ Safely accessing private balance via getter method
print("Available Balance: ₹", acc1.get_balance())

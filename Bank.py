import random

# Variabler
user = 0
acc = 0
password = 0
pin = 0
balance = 0
logPass = 0
menuLoop = True

while pin == 0:

    if int(input("[1] Create new account [2] Login: ")) == 1:
        user = input("Username: ")
        password = input("Password: ")
        pin = int(input("Pincode: "))
        acc = random.randint(1000, 9999)
    else:
        print("There's no account in our database yet..")
print("Login")
input("Username: ")
logPass = input("Password: ")
if logPass != password:
    exit()

print(user, acc, password, pin, balance, logPass)

while menuLoop == True:
    menu = int(input("[1] View Balance [2] Deposit [3] Withdrawal: "))
    if menu == 1:
        print(balance, " kr")
    elif menu == 2:
        deposit = int(input("How much: "))
        if input("Confirm? y/N: ").lower() == "y":
            balance += deposit
            print("Your new balance is: ", balance, " kr")
        else:
            print("Cancelling deposit...")
    elif menu == 3:
        withdrawal = int(input("How much: "))
        if input("Confirm withdrawal y/N: ").lower() == "y":
            balance -= withdrawal
            print("Your new balance is: ", balance, " kr")
        else:
            print("Cancelling withdrawal...")
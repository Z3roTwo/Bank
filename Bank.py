import random # Importerar en modul som bland annat ger oss tillgång till ett slumpmässigt tal
import json # Importerar bland annat json.dump för att skriva ut variablerna i ett json document

# Variabler
# (Definerar alla variabler i början så jag vet vilka jag har ._.)
login = False # Bool som är loopar startsidan tills en lyckad inloggning har skett
user = 0 # Variabel för användarnamnet, den används egentligen inte för att logga in med men det sätts när man skapar en användare
acc = 0 # Slumpmässigt kontonummer, samma som med user
password = 0 # Lösenord som sätts när man skapar användare
pin = False # Pinkod som bara används för att kolla om det finns en användare
balance = 0 # Saldo
logPass = 0 # Input lösenord vid inloggning
menuLoop = True # Loopar meny sidan så länge den är 'True'
menu = 0 # Sparar meny valet
deposit = 0 # Hur mycket pengar som sätts in
withdrawal = 0 # Hur mycket pengar som tas ut

try:
    with open("Storage.json", "r") as storage:
        for line in storage:
            print()
except:
    print("Welcome to GurkBank")

while login == False:

    if int(input("[1] Create new account [2] Login: ")) == 1:
        user = input("Username: ")
        password = input("Password: ")
        pin = input("Pincode: ")
        acc = random.randint(1000, 9999)
    elif pin == False:
        print("There's no account in our database yet..")
    else:
        print("Login")
        input("Username: ")
        logPass = input("Password: ")
        if logPass != password:
            print("Something went wrong!")
        else:
            login = True

print(user, acc, password, pin, balance, logPass)

while menuLoop:
    try:
        menu = int(input("[1] View Balance [2] Deposit [3] Withdrawal [4] Exit: "))
        if menu == 1:
            print(balance, " kr")
        elif menu == 2:
            deposit = float(input("How much: "))
            if input("Confirm? y/N: ").lower() == "y":
                if deposit < 0:
                    print("You can't deposit a negative amount, please use withdrawal instead.")
                else:
                    balance += deposit
                    print("Your new balance is: ", balance, " kr")
            else:
                print("Cancelling deposit...")
        elif menu == 3:
            withdrawal = float(input("How much: "))
            if input("Confirm withdrawal y/N: ").lower() == "y":
                if balance - withdrawal < -100:
                    print("Cannot withdraw that amount")
                else:
                    balance -= withdrawal
                    print("Your new balance is: ", balance, " kr")
            else:
                print("Cancelling withdrawal...")
        else:
            menuLoop = False
    except:
        print("Selet the number only.")

x = {"login": login, "user": user, "acc": acc, "password": password, "pin": pin, "balance": balance}
jsondumps = json.dumps(x, indent=4)
f = open('Storage.json', 'w')

json.dump(jsondumps, f)

print(jsondumps)

f.close()

# \/ Doesn't work \/
f = open('Storage.json')

y = json.load(f)
print(y["login"])
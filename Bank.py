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
logUser = 0 # Input användarnamn vid inloggning
logPass = 0 # Input lösenord vid inloggning
menuLoop = True # Loopar meny sidan så länge den är 'True'
menu = 0 # Sparar meny valet
deposit = 0 # Hur mycket pengar som sätts in
withdrawal = 0 # Hur mycket pengar som tas ut

# Skriptet kollar om Storage.json finns och öppnar den, om den inte finns så printar den bara en hälsningsfras
try:
    with open('Storage.json', 'r') as JSON:
        data = json.load(JSON)
        type(data)
        print(data["user"])
except:
    print("Welcome to GurkBank")

# While login == False loopar igenom login sidan tills en användare har skapats
# När man skapar en användare sparar den alla input som variabler
# Vid inloggnig så jämför den 'logPass' med 'pass', om det är samma så loggas man in
while login == False:

    if input("[1] Create new account [2] Login: ") == "1":
        user = input("Username: ")
        password = input("Password: ")
        pin = input("Pincode: ")
        acc = random.randint(1000, 9999)
    elif pin == False:
        # Om variabeln pin är oförändrad så måste man göra en användare
        print("There's no account in our database yet..")
    else:
        print("Login")
        logUser = input("Username: ")
        logPass = input("Password: ")
        if logPass != password or logUser != user:
            print("Something went wrong!")
        else:
            # Avslutar loopen
            login = True

# if user == data["user"]:
#    balance == data["balance"]

# Temp print för att hålla koll på om allting fungerade
# print(user, acc, password, pin, balance, logPass)

# While menuLoop loopar igenom men sidan så länge menuLoop är 'True'
# Menyn är en try/except för att koden inte ska krascha om inputen inte är en int
while menuLoop:
    try:
        menu = int(input("[1] View Balance [2] Deposit [3] Withdrawal [4] Exit: "))
        if menu == 1:
            print(balance, " kr")
        elif menu == 2:
            deposit = float(input("How much: "))
            if input("Confirm? y/N: ").lower() == "y":
                # För att förhindra att man sätter in ett negativt tal så kollar koden om 'deposit' är mindre än 0, om det är 0 eller mer så adderar den 'deposit' med'balance'
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
                if withdrawal < 0:
                    print("You can't withdraw a negative amount, please use deposit")
                else:
                    if balance - withdrawal < -100:
                        # Skriptet tillåter ett saldo på minus 100 kr
                        print("Cannot withdraw that amount")
                    else:
                        balance -= withdrawal
                        print("Your new balance is: ", balance, " kr")
            else:
                print("Cancelling withdrawal...")
        else:
            menuLoop = False # Avslutar meny loopen om man väljer vilken siffra som helst förutom 1, 2 eller 3
    except:
        print("Selet the number only.")

# Sparar variablerna som json format i x
x = {"login": login, "user": user, "acc": acc, "password": password, "pin": pin, "balance": balance}
# Sparar x i Storage.json
f = open('Storage.json', 'w')
json.dump(x, f)
# Stänger filen
f.close()
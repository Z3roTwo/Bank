# inloggning
användarnamn = "jonas"
lösenord = 123

user = input("Skriv in ditt användarnamn: ")
pin = int(input("Skriv in din pinkod:"))

while user != användarnamn:
    user = input("Fel användarnamn, prova igen: ").lower()

while pin != lösenord:
    pin = int(input("Fel pinkod, prova igen:  "))


# Insättning/ Uttag
# menu 1 insättning
# menu 2 uttag
# menu 3 avsluta
saldo = 0
menu = 0
while menu == 0:
    menu = int(input("Insättning 1, uttag 2, avsluta 3: "))
    if menu == 1: # Insättning
        insättning = float(input("Hur mycket vill du sätta in? "))
        saldo = saldo + insättning
        print(saldo)
        menu = 0

    elif menu == 2: # Uttag
        uttag = float(input("Hur mycket vill du ta ut? "))
        saldo = saldo - uttag
        if saldo < 0:
            print("Oops nu har du inga perngar kvar")
            menu = 0
        print(saldo)
        menu = 0

    elif menu == 3: # Stänger av
        print("BYE BYE")

    else:
        menu = 0
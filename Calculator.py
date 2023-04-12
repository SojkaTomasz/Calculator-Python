#Calculator program in the terminal

liczba = 0
operacja = None
reset = True
wynik = None
calcOperations = ["+", "-", "*", "/", "**"]

while True:
    if reset == True:
        liczba = int(input("Podaj pierwsza wartość: "))
        reset = False
    operacja = input("podaj dzielknik "+ str(calcOperations)+ " lub \"reset\" aby zresetować lub \"exit\" aby zakończyć: ")

    if operacja == "exit":
        print("""
        
        
        MAM NADZIEJĘ ŻE POMOGŁEM :)
        
        
        """) 
        break
    if operacja == "reset":
        reset = True
        continue
    if not operacja in calcOperations:
        print("BŁĄD! ZŁA WARTOŚĆ POPRAW")
        continue
    druga = int(input("Podaj drugą wartość: "))

    if operacja == "+":
        wynik = liczba + druga
    if operacja == "-":
        wynik = liczba - druga
    if operacja == "*":
        wynik = liczba * druga
    if operacja == "/":
        wynik = liczba / druga    
    if operacja == "**":
        wynik = liczba ** druga
    print(f'WYNIK: {liczba} {operacja} {druga} = {wynik}')
    liczba = wynik 
    wynik = None
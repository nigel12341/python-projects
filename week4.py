import math
import time


op = ""
num1 = ""
num2 = ""
woord = ""
oppervlaktecalc = ""

def oppervlakte():
    num1 = int(input("Voer de lengte in"))
    num2 = int(input("Voer de breedte in"))
    oppervlaktecalc = num1 * num2
    print(oppervlaktecalc)
    calc()

# deze functie heeft drie parameters en 1 uitvoer (het grootste van drie getallen)
def maxThree(getal1, getal2, getal3): # een functie definen die 3 variablen nodig heeft
    grootste = getal1 # Hier word gezegd dat grootste gelijk is aan getal 1
    if getal2>grootste: # Hier word gezegd dat als getal2 grote is dan grootste dan word getal2 het grootste
        grootste = getal2 # grootste = getal2
    if getal3>grootste: # als voorw
       grootste = getal3 # Hier word gezegd dat als getal3 grote is dan grootste dan word getal3 het grootste
    return grootste #Hier word het variable grootste gereturned als de functie word gecalled

def grootstegetal():
    aantal = input("Hoe vaak wil je het maximum van drie getallen berekenen? ") # Hier heb je een input dus kun je iets invullen
    for i in range(0, int(aantal)): # een For loop in een range van 0 tot variable aantal
        getalen1 = input("Het eerste van de drie getallen: ") # Weer een input
        getalen2 = input("Het tweede van de drie getallen: ") #Nog een input
        getalen3 = input("Het derde van de drie getallen:  ") #nog een input
        grootste = maxThree(getalen1 ,getalen2 ,getalen3 ) # hier doen ze de grootste kiezen via een funcite
    print("Het grootste getal van : " + getalen1 + ", " + getalen2 + " en " + getalen3 + " is " + str(grootste)) # Hier printen ze het grootste getal
    calc()

def aantalletters():
    print("Voer een woord in") #Print een string
    Totaalwoord = input("Typ een woord in: ") # een input
    woordLengte = 0 # variable is gelijk aan 0
    for i in Totaalwoord: #een For loop d ie door het variable totaalwoord gaat tot ie alles heeft
        woordLengte += 1 # telt omhoog met 1 per keer
    print("Het totaal aantal letter in het woord: " + Totaalwoord + " is " + str(woordLengte)) # print het totaal aantal letter met variablen
    calc()

def oppervlaktecirkel():
    print("Voer de straal van de cirkel in")
    num1 = int(input())
    print(math.pi*num1*num1)
    calc()

def inhoudcirkel():
    print("Voer de straal van de cirkel in")
    num1 = int(input())
    num2 = int(input("Voer de hoogte van de circel in"))
    print(math.pi*num1*num1*num2)
    calc()

def calc():
    print("Welkom!")
    print("Wat wil je doen? oppervlakte, grootste getal, aantal letters, oppervlakte cirkel, inhoud cilinder")
    op = input("")
    if op == "oppervlakte":
        oppervlakte()
    elif op == "grootste getal":
         grootstegetal()
    elif op == "aantal letters":
        aantalletters()
    elif op == "oppervlakte cirkel":
        oppervlaktecirkel()
    elif op == "inhoud cilinder":
        inhoudcirkel()
    else:
        print("Error")

calc()

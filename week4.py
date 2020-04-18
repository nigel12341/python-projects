import math #Hier word de math library geimporteerd


#Dit script is een gemodificeerde versie van mijn calculator https://github.com/nigel12341/python-projects/blob/master/calculator.py samen met week2 en week3 van de python opdrachten


op = "" #Komende regels wat variabelen
num1 = ""
num2 = ""
woord = ""
oppervlaktecalc = ""

def oppervlakte(): #De oppervlakte circel
    num1 = int(input("Voer de lengte in")) #hier kun je het eerste nummer invoeren
    num2 = int(input("Voer de breedte in")) #hier het 2e nummer
    oppervlaktecalc = num1 * num2 #Hier word de oppervlakte uitgerekend
    print(oppervlaktecalc) #Hier word ie geprint
    calc() # Hier word het calc functie gerund zodat je niet de hele tijd het script opnieuw moet openen

# deze functie heeft drie parameters en 1 uitvoer (het grootste van drie getallen)
def maxThree(getal1, getal2, getal3): # een functie definen die 3 variablen nodig heeft
    grootste = getal1 # Hier word gezegd dat grootste gelijk is aan getal 1
    if getal2>grootste: # Hier word gezegd dat als getal2 grote is dan grootste dan word getal2 het grootste
        grootste = getal2 # grootste = getal2
    if getal3>grootste: # als voorw
       grootste = getal3 # Hier word gezegd dat als getal3 grote is dan grootste dan word getal3 het grootste
    return grootste #Hier word het variable grootste gereturned als de functie word gecalled

def grootstegetal(): # Dit is de functie voor het grootste getal
    aantal = input("Hoe vaak wil je het maximum van drie getallen berekenen? ") # Hier heb je een input dus kun je iets invullen
    for i in range(0, int(aantal)): # een For loop in een range van 0 tot variable aantal
        getalen1 = input("Het eerste van de drie getallen: ") # Weer een input
        getalen2 = input("Het tweede van de drie getallen: ") #Nog een input
        getalen3 = input("Het derde van de drie getallen:  ") #nog een input
        grootste = maxThree(getalen1 ,getalen2 ,getalen3 ) # hier doen ze de grootste kiezen via een funcite
    print("Het grootste getal van : " + getalen1 + ", " + getalen2 + " en " + getalen3 + " is " + str(grootste)) # Hier printen ze het grootste getal
    calc() # Hier word het calc functie gerund zodat je niet de hele tijd het script opnieuw moet openen

def aantalletters(): #Dit is de functie voor het aantal letter uitrekenen
    print("Voer een woord in") #Print een string
    Totaalwoord = input("Typ een woord in: ") # een input
    woordLengte = 0 # variable is gelijk aan 0
    for i in Totaalwoord: #een For loop d ie door het variable totaalwoord gaat tot ie alles heeft
        woordLengte += 1 # telt omhoog met 1 per keer
    print("Het totaal aantal letter in het woord: " + Totaalwoord + " is " + str(woordLengte)) # print het totaal aantal letter met variablen
    calc() # Hier word het calc functie gerund zodat je niet de hele tijd het script opnieuw moet openen

def oppervlaktecirkel(): #Hier word het oppervlakte berekend
    print("Voer de straal van de cirkel in")#print
    num1 = int(input())#hier moet je de straal invullne
    print(math.pi*num1*num1)#hier rekend ie de oppervlakte uit
    calc() # Hier word het calc functie gerund zodat je niet de hele tijd het script opnieuw moet openen

def inhoudcirkel():#inhoud uitrekende
    print("Voer de straal van de cirkel in") #print
    num1 = int(input()) #het eerste nummer 
    num2 = int(input("Voer de hoogte van de circel in")) # het 2e nummer
    print(math.pi*num1*num1*num2) #rekend de inhoud uit
    calc() # Hier word het calc functie gerund zodat je niet de hele tijd het script opnieuw moet openen

def calc(): #de main functie
    print("Welkom!")#print
    print("Wat wil je doen? oppervlakte, grootste getal, aantal letters, oppervlakte cirkel, inhoud cilinder") #print
    op = input("")# hier moet je kiezen uit oppervlakte, grootste getal, aantal letters, oppervlakte cirkel, inhoud cilinder
    if op == "oppervlakte": #if oppervlakte
        oppervlakte() #de oppervlakte funcite
    elif op == "grootste getal": #een elif
         grootstegetal() #de grootste getal funcite
    elif op == "aantal letters": #een elif
        aantalletters() # de aantalletters funcite
    elif op == "oppervlakte cirkel": #een elif
        oppervlaktecirkel() #de oppervlakte cirkel nummer
    elif op == "inhoud cilinder": #een elif 
        inhoudcirkel() #inhoud cirkel funcite
    else: #als niks werkt word error laten zien
        print("Error")

calc() #zodat de calc functie opend

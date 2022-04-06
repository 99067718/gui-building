import tkinter
from tkinter import messagebox
from tkinter import ttk
import threading
from tkinter import font

##### functions #####

def updateExampleText(*args):
    exampleText.config(font=("Comic_Sans",textSizeValue.get()))

def settings():
    global textSizeValue
    global exampleText
    settingsWindow = tkinter.Tk()
    textSizeValue = tkinter.IntVar(value=20)
    exampleText = tkinter.Label(settingsWindow,text="Example",font=("Comic_Sans",textSizeValue.get()))
    exampleText.grid(column=1,row=1)
    textSize = ttk.Scale(settingsWindow,from_=1,to=50,orient="horizontal",variable=textSizeValue,length=200)
    textSize.grid(column=1,row=3)
    textSize.grid(columnspan=2)
    textSizeValue.trace("w",updateExampleText)
    settingsWindow.mainloop()

def zakelijkOfParticulierCheck(*args):
    global textLabel
    particulier.destroy()
    zakelijk.destroy()

    # ##### Create settings button #####     (I don't know how to make the labels update live without crashing the program.)
    # settingsButton = tkinter.Button(text="Settings",bg="green",command=settings,font=("Comic_Sans",textSizeValue.get()))
    # settingsButton.grid(column=3,row=5)

    ##### Create Label for text #####
    textVar = tkinter.StringVar(value="Default Text")
    textLabel = tkinter.Label(window, textvariable=textVar, font=("Comic_Sans",textSizeValue.get()))
    textLabel.grid(columnspan=3)
    textLabel.grid(column=1,row=0)

    # ##### Start threading timer #####
    # threading.Timer(1,callUpdateLabels).start()
    
    ##### gaat naar particulier of zakelijk #####
    if partOfZak.get() == "z":
        textVar.set("How much Liter of icecream do you want?")
        Liter = tkinter.IntVar()
        howMuchLiter = tkinter.Entry(window,textvariable=Liter,font=("Comic_Sans",textSizeValue.get()))
        howMuchLiter.grid(column=2,row=2)
    elif partOfZak.get() == "p":
        textVar.set("How many ice cream scoops do you want?")
    else:
        messagebox.showerror(message="idk what you did, but you broke it.")

settings()

window = tkinter.Tk()

##### kies particulier/zakelijk #####
partOfZak = tkinter.StringVar()
zakelijk = ttk.Radiobutton(window,variable=partOfZak,value="z",text="zakelijk")
particulier = ttk.Radiobutton(window,variable=partOfZak,value="p",text="particulier")
zakelijk.pack()
particulier.pack()
partOfZak.trace("w",zakelijkOfParticulierCheck)

window.mainloop()

##### Einde window 1 #####
























######### oude code #########

aantal = 0
herhalen = "y"
repeat = True
TotaalBakjes = 0
totaalHoorntjes = 0
TotaleBolletjes = 0
particulier = "...."

#------Zakelijk------#
Liters_ijs = 0
Btw = 6
prijsPerLiter = 9.80
#-----------------------#

Besteldesmakenlijst = []
BestaandeSmaken = ["aardbei", "a", "chocolade", "c", "vanille", "v"]

toppings = []
aantalToppings = 0
bestaandeToppings = ["sl", "slagroom", "sp", "sprinkels", "c", "caramel"]
toppingKosten = 0.00

prijsPerBakje = 0.75
prijsPerHoorntje = 1.25
prijsPerBolletje = 0.95

print("Welkom bij Papi Gelato.")

def WrongAnswer():
    print("Sorry dat is geen optie die we aanbieden...")

def AantalLiter():
    global Liters_ijs
    Liters_ijs = int(input("Hoeveel liter ijs wilt U bestellen?: "))

def topping():
    
    
        toppingKeuze = input("Wat voor topping wilt u: (G) Geen, (Sl) Slagroom, (Sp) Sprinkels of (C) Caramel Saus?: ").lower()
        if toppingKeuze == "g":
            print("")
            
        elif toppingKeuze in bestaandeToppings:
            
            toppings.append(toppingKeuze)
            global aantalToppings
            global toppingKosten
            aantalToppings += 1

            if toppingKeuze == "sl" or "slagroom":
                
                toppingKosten += 0.50
            elif toppingKeuze == "sp" or "sprinkels":
                
                toppingKosten += (0.30 * aantal)
            elif toppingKeuze == "c" or "caramel":
                if bakjeOfHoorntje == "bakje":
                    
                    toppingKosten += 0.90
                elif bakjeOfHoorntje == "hoorntje":
            
                    toppingKosten += 0.60

        else:
            WrongAnswer()

def ParticulierSmaak():
    print("Welke smaak wilt u hebben?")
    print("Aardbei(A), Chocolade(C) of Vanille(V)")
    smaak = input("Welke smaak ijs wilt U?")


def smaak():
    print("Welke smaak wilt u hebben?")
    print("Aardbei(A), Chocolade(C) of Vanille(V)")
    returnsInLoop = 1
    while returnsInLoop != aantal + 1:
        smaak = input("Welke smaak wilt U hebben voor uw "+ str(returnsInLoop) + "e bolletje?").lower()
        if smaak in BestaandeSmaken:
            returnsInLoop += 1
            Besteldesmakenlijst.append(smaak)
            
        else:
            WrongAnswer()


def aantalbolletjes():
    repeater = "enabled"
    while repeater == "enabled":
        aantalBolletjesijs = int(input("Hoe veel bolletjes ijs wil je?: "))
        if aantal > 0:
            repeater = "disabled"
            return aantalBolletjesijs
        else:
            WrongAnswer()

def WatVoorVerpakking():
    if aantal <= 3:
        waarin = keuzeBakjeOfHoorntje()

    elif aantal > 3 and aantal < 8:
        print("Dan krijgt u van mij een bakje met", aantal, "bolletjes.")
        waarin = "bakje"
    
    elif aantal > 8:
        print("Sorry, maar zulke grote bakjes hebben wij niet.")
        waarin = "ERROR"
      
    else:
        WrongAnswer()
        waarin = "ERROR"
       
    return waarin

def keuzeBakjeOfHoorntje():
    soort = input("Wilt U een hoorntje of een bakje?(H of B): ").lower()
    if soort == "b":
        soort = "bakje"
    elif soort == "h":
        soort = "hoorntje"
    return soort

def nogEenKeer():
    smaak()
    topping()
    print("Hier is uw", bakjeOfHoorntje, "met", aantal, "bolletje(s)")
    overnieuw = input("Wilt u nog wat bestellen?(Y/N): ").lower()
    return overnieuw

while repeat == True:
    Soort = input("Bent u Particulier (P) of zakelijk (Z)?: ").lower()
    if Soort == "p" or Soort == "particulier":
        herhalen = "y"
        particulier = "ja"
        repeat = False
    elif Soort == "z" or Soort =="zakelijk":
        particulier = "nee"
        herhalen = "n"
        repeat = False
    else:
        WrongAnswer()
        repeat = True


while herhalen == "y":
    
    aantal = aantalbolletjes()

    bakjeOfHoorntje = WatVoorVerpakking()
    if bakjeOfHoorntje != "ERROR":
        herhalen = nogEenKeer()
        TotaleBolletjes += aantal
        if bakjeOfHoorntje == "bakje":
            
            TotaalBakjes = TotaalBakjes + 1
        elif bakjeOfHoorntje == "hoorntje":
            totaalHoorntjes = totaalHoorntjes + 1
        else:
            WrongAnswer()
    else:

        print("")

if particulier == "nee":
    Litersijs = AantalLiter()
    ParticulierSmaak()

if particulier == "ja":
    print('---------["Papi Gelato"]---------')
    print("")
    if TotaleBolletjes >= 1:
        print("Bolletje(s)    "+ str(TotaleBolletjes)+ " X " + "€" + str(round(float(TotaleBolletjes) * prijsPerBolletje,2)))

    if totaalHoorntjes >= 1:
        print("Hoorntje(s)    "+ str(totaalHoorntjes)+ " X " + "€" + str(round(float(totaalHoorntjes) * prijsPerHoorntje,2)))

    if TotaalBakjes >= 1:
        print("Bakje(s)       "+ str(TotaalBakjes)+ " X " + "€" + str(round(float(TotaalBakjes) * prijsPerBakje,2)))

    if aantalToppings >= 1:
        print("topping(s)     "+ str(aantalToppings)+ " X " + "€" + str(round(toppingKosten,2)))

    print("                   ----- +")
    totaalprijs = float(totaalHoorntjes) * prijsPerHoorntje + float(TotaalBakjes) * prijsPerBakje + TotaleBolletjes * prijsPerBolletje
    totaal2 = round(float(totaalprijs),2)

    print("Totaal"+ "              "+ "€" + str(totaal2))
else:
    print('---------["Papi Gelato"]---------')
    print("")
    totaalprijs = float(Liters_ijs) * float(prijsPerLiter)
    totaalprijs2 = round(float(totaalprijs),2)
    print("Liter   "+ str(Liters_ijs), " X "+ str(prijsPerLiter)+ " = "+"€"+ str(totaalprijs2))
    print("                -------- +")
    btwprijs = round(float(totaalprijs/100 * Btw),2)
    print("Totaal           = €"+ str(totaalprijs2))
    print(f'BTW               {round(totaalprijs2 / 106 * Btw, 2)}€')




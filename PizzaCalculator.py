import tkinter
from tkinter import Checkbutton, Grid, ttk
import threading
from tkinter.messagebox import showwarning
from turtle import title
from plyer import notification
###############

# Emiel 't Lam
# 99067718
# Pizza Calculator GUI UPDATE!!!!

PriceSmallPizza = 5.99
PriceMediumPizza = 6.99
PriceBigPizza = 7.50

window = tkinter.Tk()
NameVar = tkinter.StringVar(value="")
TitlePage1 = tkinter.Label(text="Pizza Calculator",font=("Comic_Sans",20)).pack()

################ Enter name ################
FillName = tkinter.Entry(textvariable=NameVar,font=("Comic_Sans",10))
FillName.insert(0, "Enter your name here.")
FillName.pack()
FillName.bind("<FocusIn>", lambda event: FillName.delete(0,"end") if NameVar.get() == "Enter your name here." else None)
FillName.bind("<FocusOut>", lambda event: FillName.insert(0, "Enter your name here.") if NameVar.get() == "" else None)

################ Enter Location ################
Location = tkinter.StringVar(value="")
EnterLocation = tkinter.Entry(textvariable=Location,font=("Comic_Sans",10))
EnterLocation.pack()
EnterLocation.insert(0, "Enter your adress here")
EnterLocation.bind("<FocusIn>", lambda event: EnterLocation.delete(0,"end") if Location.get() == "Enter your adress here" else None)
EnterLocation.bind("<FocusOut>", lambda event: EnterLocation.insert(0, "Enter your adress here") if Location.get() == "" else None)
ConfirmButton = tkinter.Button(text="Confirm", command=lambda: window.destroy()).pack()
window.mainloop()

############# Second Window Value Check #############
def PizzaValueCheck():
    try:
        int(SmallPizzas.get())
        int(MediumPizzas.get())
        int(BigPizzas.get())
        OrderWindow.destroy()
    except:
        notification.notify(title="Achievement get!",message="\"Why are you such a dumbass? 😀\"")
        showwarning(title="Error",message="Are you sure you entered the right values?")

keepBuying = True
################ Start Second Window ################
while keepBuying:
    OrderWindow = tkinter.Tk()


    # Creating Window with all prices
    ttk.Label(text=f"""    
    -------------------------------
    | Menu                
    |                           
    | Price Small Pizza:  €{PriceSmallPizza}         
    | Price Medium Pizza: €{PriceMediumPizza}        
    | Price Big Pizza:    €{PriceBigPizza}           
                                
    -------------------------------""").grid(column=0,row=9)
    #  Creating Pizza Values #
    SmallPizzas = tkinter.IntVar()
    MediumPizzas = tkinter.IntVar()
    BigPizzas = tkinter.IntVar()

    # Pizza entry's #
    tkinter.Label(OrderWindow, text="Pizza's", font=("Comic_Sans",20)).grid(column=0, row=0)
        #   small
    tkinter.Label(text="How many small Pizza's would you like to order?",font=("Comic_Sans",10)).grid(column=0,row=1)
    SmallOrder = tkinter.Entry(OrderWindow, textvariable=SmallPizzas).grid(column=0,row=2)
        #   medium
    tkinter.Label(text="How many medium Pizza's would you like to order?",font=("Comic_Sans",10)).grid(column=0,row=3)
    MediumOrder = tkinter.Entry(OrderWindow, textvariable=MediumPizzas).grid(column=0,row=4)
        #   big
    tkinter.Label(text="How many big Pizza's would you like to order?",font=("Comic_Sans",10)).grid(column=0,row=5)
    BigOrder = tkinter.Entry(OrderWindow, textvariable=BigPizzas).grid(column=0,row=6)

    # Confirm #
    tkinter.Button(text="Confirm",font=("Comic_Sans",10),bg="green",command=PizzaValueCheck).grid(column=0,row=8)

    OrderWindow.mainloop()

    def FinishOrder():
        global keepBuying
        keepBuying = False
        OrderMoreWindow.destroy()
    OrderMoreWindow = tkinter.Tk()
    tkinter.Label(text="Are you sure you want to continue?", font=("Comic_Sans", 10)).grid(row=0,column=2)
    tkinter.Button(text="no",bg="red", command=lambda: OrderMoreWindow.destroy()).grid(row=1,column=3)
    tkinter.Button(text="yes", command= FinishOrder,bg="green").grid(row=1,column=1)
    OrderMoreWindow.mainloop()
    ##########
finalScreen = tkinter.Tk()
tkinter.Label(text=f"Thanks for your order {NameVar.get()}!").grid(row=0, column=2)
ttk.Label(text=f"""
--------------------------------------
Your Order
Small Pizza's: {SmallPizzas.get()}      price: €{round(float(SmallPizzas.get()) * PriceSmallPizza,2)}
Medium Pizza's: {MediumPizzas.get()}    price: €{round(float(MediumPizzas.get()) * PriceMediumPizza,2)}
Big Pizza's: {BigPizzas.get()}          price: €{round(float(BigPizzas.get()) * PriceBigPizza,2)}

total:          {int(BigPizzas.get()) + int(MediumPizzas.get()) + int(SmallPizzas.get())}
totalPrice: €{round(float(SmallPizzas.get()) * PriceSmallPizza + float(MediumPizzas.get()) * PriceMediumPizza + float(BigPizzas.get()) * PriceBigPizza,2)}
--------------------------------------
""").grid(row=1,rowspan=2,columnspan=2,column=1)
tkinter.Button(text="Exit",bg="red",command=lambda:finalScreen.destroy()).grid(row=3,column=2)
finalScreen.mainloop()


####### Old Non Gui Version ######
# SmallCost = 5.99
# MediumCost = 6.99
# LargeCost = 7.50
# try:
#     print("Hello Costumer, welcome to our pizza-ordering-site")
#     name = input("Please enter your name: ")
#     adress = input(name + " what is your adress?? : ")
#     #Klant krijgt de vraag hoe groot de pizza moet zijn
#     print("""
#     -------------------------------
#     |      Prices                
#     |                            
#     | Small costs  €5.99         
#     | Medium costs €6.99         
#     | Large costs  €7.50           
#     |                             
#     -------------------------------
#     """)
#     small = int(input("how much small pizza's would you like to have?: "))
#     smalltotal = round(float(small) * float(SmallCost),2)
#     print(str(small) + " pizza's with a cost of "+ str(smalltotal))

#     medium = int(input("how much medium pizza's would you like to have?: "))
#     mediumtotal = round(float(medium) * float(MediumCost),2)
#     print(str(medium) + " pizza's with a cost of "+ str(mediumtotal))

#     large = int(input("how much large pizza's would you like?: "))
#     print(str(large) + " pizza's with a cost of "+ str(large * LargeCost))
#     largetotal = round(float(large) * float(LargeCost),2)
#     amo = small + medium + large
#     totalcost = round((small * SmallCost) + (medium * MediumCost) + (largetotal),2)

#     # Asks for completion of purchase
#     print("------------------------------------------------")
#     print("| kosten van bestelling")
#     print("| small: "+ str(small) + " € " + str(SmallCost) + " = €" + str(smalltotal))
#     print("| medium: "+ str(medium) + " € " + str(MediumCost) + " = €" + str(mediumtotal))
#     print("| large: "+ str(large) + " € " +str(LargeCost) + " = €" + str(largetotal))
#     print("|")
#     print("Total:                €" + str(totalcost))
#     print("------------------------------------------------")
#     input("Thanks for your order, would you like to pay now, or will you purchase when delivery arrives? : ")
#     input("The pizza(s) will be delivered at " + adress + " is that correct? ")
#     print("Thanks, "+ name + " you will receive your pizza in " + str(amo * 4) + " minutes.")
# except:
#     print("something went wrong.")
#order completed

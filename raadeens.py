from time import sleep
import sys
from tkinter import messagebox
from tkinter.messagebox import askyesno, askquestion
import random
import tkinter
import threading
WrongValueFails = 0
IsMad = False
MadBotTries = 0
Tries = 0

def Scream():
    global textOfExit
    sleep(0.1)
    exit()
def playAgain():
    global Tries
    if askyesno(title='play again?', message='Do you want to play again?'):
        Tries = 0
        number = random.randint(1,1000)
        try: 
            BotMan.config(fg="black")
            messagebox.showinfo('New number', "A new number has been generated!!!")
        except:
            messagebox.showinfo('E', "A̷̡̧͔͉̝͓̙͈̹͓͋̈́̿ ̷̛̳͔̜̟͔͊̏̒͗̕ͅn̴̜͚̜̮͉̟̈́̀͗̿͝ų̶̼͓̲̣͈͙̳͍̙̠͒̈́̐̓̓̾̊̈͐͜͜ṁ̷̡̧̢͖̌́͊̌̉͂ ̸̝̹̒́́̿̚͠͝b̸͈͉̺̫̪̣͉̭͍͔̒͑͗͂͊̆̓͜͝ȩ̵̜̤̞͕͉͆̈́̓̅̆̿̊̀̐̈́̐͝͠͝r̷͓̤̂̉͗͗̆͝")
    else:
        try: 
            BotMan.config(fg="black")
            messagebox.showinfo('Cool Title', "Thanks for playing!!!")
        except:
            threading.Timer(3, sys.exit).start()
            threading.Timer(0,Scream).start()
        sys.exit()

def checkAnswer():
    global WrongValueFails
    global IsMad
    global MadBotTries
    global Tries
    global number
    try:
        CanContinue = int(EnteredNumber.get()) == number
        if CanContinue:
            textVar.set("Congrats you guessed the number!!!")
            playAgain()
        elif IsMad:
            Tries += 1
            MadBotTries += 1
            if MadBotTries == 7:
                textVar.set("I give you another chance")
                answer = askyesno(title='Confirmation',
                          message='Im sorry for getting mad at you, do you accept my apology?')
                if answer:
                    messagebox.showinfo('yay', "Thanks!!!")
                    IsMad = False
                else:
                    messagebox.showinfo('...', "Oh...")
                    messagebox.showinfo('...', "I might as well just delete myself then...")
                    BotMan.destroy()
                    messagebox.showerror("ERROR","HelpBot.bot has not been found")
                    sleep(1)
                    messagebox.showwarning('YOU FOOL', "You fool, the game is now unplayable...")
                    IsMad = False
            elif MadBotTries == 5:
                textVar.set("I told you I was not going to help you...")
            else:
                textVar.set("...")
        else:
            Tries += 1
            Close = EnteredNumber.get() in MoreOrLess
            if Close == True:
                if int(EnteredNumber.get()) > number:
                    textVar.set("You are very close (the answer is lower)")
                elif int(EnteredNumber.get()) < number:
                    textVar.set("You are very close (the answer is higher")
            elif int(EnteredNumber.get()) > number:
                textVar.set("The answer is lower")
            elif int(EnteredNumber.get()) < number:
                textVar.set("The answer is higher")
            if Tries == 10:
                textVar.set("You didn't guess it in time, wanna try again?")
                playAgain()
    except:
        if WrongValueFails == 2:
            textVar.set("You dumbass, you know what a number is right?")
        elif WrongValueFails <2:
            textVar.set("try entering a number.")
        elif WrongValueFails == 7:
            textVar.set("""You know what, I will stop talking to you.
            You have to figure it out by yourself...""")
            IsMad = True
        elif WrongValueFails > 5:
            textVar.set("...")
        else:
            textVar.set("JUST ENTER A NUMBER!!!")
        WrongValueFails += 1

def loadNewButtons():
    tempButton.destroy()
    textVar.set("Start guessing!")
    tkinter.Entry(textvariable=EnteredNumber).pack()
    CheckButton = tkinter.Button(text="Try",command=checkAnswer).pack()

daEpicWindow = tkinter.Tk()
textOfExit = tkinter.StringVar(value="A")
EnteredNumber = tkinter.IntVar(value="0")
textVar = tkinter.StringVar(value="Welcome to the epic game where you try to guess a number between 1 and 1000.")
BotMan = tkinter.Label(textvariable=textVar)
BotMan.pack()
tempButton = tkinter.Button(text="continue",command=loadNewButtons)
tempButton.pack()
number = random.randint(1,1000) #generates random number between 1 and 1000
MoreOrLess = range(int(number - 20), int(number + 20))
daEpicWindow.mainloop()


# print("""
# Hallo, we spelen vandaag het spel, 'Raad het getal'.
# In dit spel moet je een getal tussen de 1 en 1000 raden
# """)
# while Rounds <= 20:
#     number = random.randint(1, 1000)
#     correctAnswer = False
#     Guesses = 0
#     r = range(int(number - 20), int(number + 20))
#     print("raad het nummer!!!")
#     while Guesses != 10:
#         print("Aantal keer gegokt: ",Guesses)
#         gegoktnummer = int(input("Nummer: "))
#         Guesses = Guesses + 1
#         if gegoktnummer > number:
#             print("Het getal is lager.")
#         if gegoktnummer < number:
#             print("Het getal is hoger.")

#         Close = gegoktnummer in r
#         if Close == True: #checkt of je getal in de buurt ligt#
#             print("Je bent heel dicht in de buurt.")

#         if gegoktnummer == number:
#             print("Goed gedaan, je hebt het juiste antwoord!!!")
#             score = score + 1
#             print("je hebt nu",score, "punt(en)")
#             correctAnswer = True
#             break
#         else:
#             print("")
#     if correctAnswer == False:
#         print("The correct answer was:", number)
#     Rounds = Rounds + 1
#     if Rounds != 20:
#         print("Wilt U verder spelen???")
#         doesContinue = input("typ 'quit' om te stoppen, vul niks in om door te gaan: ").upper()
#     else:
#         print("Bedankt voor het spelen.")
#     if doesContinue == "QUIT":
#         break

# print("Uw eindscore is:", score, "punt(en)")





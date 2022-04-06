#99067718
#Emiel 't Lam
#de prints die leeg zijn, zijn er om het een beetje overzichtelijk te houden tijdens het invullen

import tkinter
from tkinter import ttk
from tkinter import messagebox

##### Values #####

QuestionId = 0
HasDiploma = False
DoesQualify = True

##### Functions #####

def CheckManWoman(*args):
    global ManWoman
    global DoesQualify
    ManOrWoman.destroy()
    if ManWoman.get() == "man":
        ManWomanQuestion = messagebox.askyesno(message="Do you have a mustache longer then 20 cm?")
    else:
        ManWomanQuestion = messagebox.askyesno(message="Do you have red spinhair?")
    if ManWomanQuestion:
        pass
    else:
        DoesQualify = False

def NextQuestion():
    ##### Globals #####
    global ManWoman
    global QuestionId
    global DoesQualify
    global HasDiploma
    global ManOrWoman
    ###################
    QuestionId += 1
    if QuestionId == 1:
        NameQuestion.destroy()
        textValue.set("Have you ever flushed a cat in the toilet?")
        CatFlush = messagebox.askyesno(title="Cat",message="Have you ever flushed a cat in the toilet? (I'm sure you did)")
        if CatFlush:
            messagebox.showinfo(message="Why would you do that?!")
            messagebox.showinfo(message="Without recording it and showing it to me???")
        else:
            messagebox.showerror(message="Alright then... keep your secrets.")
    elif QuestionId == 2:
        textValue.set("Do you have an MBO diploma?")
        hasDiploma = messagebox.askyesno(title="Diploma",message="Do you have an MBO diploma?")
        try:
            whatDiploma = tkinter.IntVar()
            if hasDiploma:
                diplomaQuestion = tkinter.Tk()
                textValue.set("Which MBO diploma do you have?")
                whatdiplomaEntry = ttk.Entry(diplomaQuestion,textvariable=whatDiploma)
                whatdiplomaEntry.pack()
                proceedButton = tkinter.Button(diplomaQuestion,text="Proceed",command=lambda:diplomaQuestion.destroy()).pack()
                diplomaQuestion.mainloop()
                
            else:
                DoesQualify = False
                messagebox.showwarning(message="ok...")
                messagebox.showinfo(message="Lets proceed... (I guess)")
        except:
            messagebox.showerror(message="How in the world did you manage to get this error message?")
            exit()
    elif QuestionId == 3:
        textValue.set("Did you ever play Undertale?")
        Undertale = messagebox.askyesno(title="UNDERTALE",message="Did you ever play Undertale?")
        if Undertale:
            messagebox.showinfo(message="Wow, you are a true man of culture!")
        else:
            messagebox.showerror(message="You have been denied")
            messagebox.showinfo(message="Sorry, that was a glitch in the program, but you should really try playing Undertale tho.")
    elif QuestionId == 4:
        textValue.set("Do you have a truck driving license?")
        TruckLicense = messagebox.askyesno(message="Do you have a truck driving license?")
        if TruckLicense:
            pass
        else:
            DoesQualify = False
    elif QuestionId == 5:
        textValue.set("Do you have a high hat?")
        HasHighHat = messagebox.askyesno(message="Do you have a high hat???")
        if HasHighHat:
            pass
        else:
            DoesQualify = False
    elif QuestionId == 6:
        textValue.set("Did you ever punch a woman?")
        messagebox.askyesno(message="Did you ever punch a woman?")
    elif QuestionId == 7:
        textValue.set("Are you a man or woman?")
        ManWoman = tkinter.StringVar()
        ManOrWoman = ttk.Combobox(values=["man","woman"],textvariable=ManWoman,state="readonly")
        ManOrWoman.pack()
        ManWoman.trace('w',CheckManWoman)

    elif QuestionId == 8:

        textValue.set("What is your weight?")
        WeightWindow = tkinter.Tk()
        tkinter.Label(WeightWindow,text="What is your weight?").pack()
        weight = tkinter.StringVar()
        ttk.Entry(WeightWindow,textvariable=weight).pack()
        ttk.Button(WeightWindow,text="Proceed",command=lambda:WeightWindow.destroy()).pack()
        WeightWindow.mainloop()
    elif QuestionId == 9:
        textValue.set("Do you have a certificate for working with dangerous people?")
        messagebox.showinfo(message="im sure you do, lets skip this question.")
    elif QuestionId == 10:
        if DoesQualify:
            messagebox.showinfo(message="congrats, you are accepted")
        else:
            messagebox.showerror(message="U do be denied.")

#####################

survey = tkinter.Tk()

##### Create Variabeles #####

NameVar = tkinter.StringVar()
textValue = tkinter.StringVar(value="Enter your name.")

##### Create Labels and Entry #####

tkinter.Label(textvariable=textValue).pack()
NameQuestion = ttk.Entry(textvariable=NameVar)
NameQuestion.pack()
ttk.Button(text="Continue",command=NextQuestion).pack()
survey.mainloop()

##### End of Gui #####




# DoesQualify = True
# print("")
# print("Hallo en welkom bij dit sollicitatiegebeuren, vul de vragenlijst eerlijk in.")
# print("")
# naam = input("Wat is uw Naam? : ")
# print("")

#onzinvraag 1
# input("Heeft u wel eens een kat door de wc gespoeld? ")
# print("")
# try:
#     antw = int(input("Hoeveel jaar praktijk ervaring heb je met acrobatiek? "))
#     if antw >= 4:
#         print("")
#     else:
#         print("")
#         DoesQualify = False

#     MBO = input("Heeft u een MBO diploma? y/n: ").upper()
#     if MBO == "Y":
#         antw = int(input("Welke diploma??(Nummer): "))
#         if antw >= 4:
#             print("")
#         else:
#             print("")
#             DoesQualify = False
#     else:
#         print("")
#         DoesQualify = False
# except:
#     raise NameError("Go to horny jail you dumbass.")

#onzinvraag 2
# input("Heeft u wel eens een alien ontmoet, en er een diner mee gehad? ")
# print("")

# antw = input("Heeft u een vrachtwagen rijbewijs? (beantwoord met y/n): ").upper()
# if antw == "Y":
#     print("")
# else:
#     print("")
#     DoesQualify = False


# antw = input("Heeft u een hoge hoed? (beantwoord met y/n): ").upper()
# if antw == "Y":
#     print("")
# else:
#     print("")
#     DoesQualify = False


# #onzinvraag 3
# input("Heeft u ooit sinterklaas geslagen? ")
# print("")

# gen = input("bent u een man of vrouw (antwoord met m/v): ").upper()

# if gen == "M":
#     antw = input("Heeft u een snor breder dan 10 cm? (beantwoord met y/n): ").upper()
# else:
#     antw = input("Heeft u lang rood krulhaar langer dan 20 cm? (beantwoord met y/n): ").upper()
# if antw == "Y":
#     pass
# elif antw == "N":
#     DoesQualify = False
# else:
#     raise NameError("U bent nu als kaal verklaard.")
    


# antw = int(input("Hoe lang bent U? "))
# if antw >= 150:
#     print("")
# else:
#     print("")
#     DoesQualify = False

# #onzinvraag 4
# input("Heeft u kippen onder uw bed?: ")
# print("")

# antw = int(input("Hoeveel weegt U?: "))
# if antw >= int(90):
#     print("")
# else:
#     print("")
# #     DoesQualify = False


# antw = input("Heeft u een certificaat overleven met gevaarlijk personeel?(beantwoord met y/n): ").upper()
# if antw == "Y":
#     print("")
# else:
#     print("")
#     DoesQualify = False

# if DoesQualify == True:
#     print("Gefeliciteerd," + naam + " u voldoet aan al onze eisen!!!")
# else:
#     print("Sorry, "+ naam + " maar u voldoet niet aan onze eisen.")
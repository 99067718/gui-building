import tkinter
from tkinter import ttk
#99067718
#Emiel 't Lam
QuestionID = 0
def disableQuestion(*args):
    global QuestionID
    if QuestionID == 0 and Answer.get() != "":
        if Answer.get() == "Y":
            QuestionID = 10
            DialogueVar.set("zitten er gaten in?")
        else:
            QuestionID = 20
            DialogueVar.set("Heeft de kaas blauwe schimmels?")
        Answer.set("")
 ######################################################################### Path 10's (wel geel)
    elif QuestionID == 10 and Answer.get() != "": #              10
        if Answer.get() == "Y":
            QuestionID = 11
            DialogueVar.set("Is de kaas belachelijk duur?")
        else:
            QuestionID = 12
            DialogueVar.set("Is de kaas hard als steen?")
        Answer.set("")

    elif QuestionID == 11 and Answer.get() != "": #                   11
        if Answer.get() == "Y":
            QuestionID = 15 #                                         15
            DialogueVar.set("De kaas die je in gedachten hebt is: Emmenthaler")
        else:
            QuestionID = 16 #                                         16
            DialogueVar.set("De kaas die je in gedachten hebt is: Leerdammer")
        disableQuestion()

    elif QuestionID == 12 and Answer.get() != "": #                   12
        if Answer.get() == "Y":
            QuestionID = 13 #                                         13
            DialogueVar.set("De kaas die je in gedachten hebt is: Pamniago Reggiano")
        else:
            QuestionID = 14 #                                         14
            DialogueVar.set("De kaas die je in gedachten hebt is: Goudse kaas")
        disableQuestion()
######################################################### path 20's (Niet geel)
    elif QuestionID == 20 and Answer.get() != "": #                   20
        if Answer.get() == "Y":
            QuestionID = 21   
        else:
            QuestionID = 24
        DialogueVar.set("Heeft de kaas een korst?")
        Answer.set("")
    elif QuestionID == 21 and Answer.get() != "": #                   21
        if Answer.get() == "Y":
            QuestionID = 22   #                                       22
            DialogueVar.set("De kaas die je in gedachten hebt is: Bleu de Rochbaron")
        else:
            QuestionID = 23
            DialogueVar.set("De kaas die je in gedachten hebt is: Foumme d'Ambert")
        disableQuestion()
    elif QuestionID == 24 and Answer.get() != "": #                   24
        if Answer.get() == "Y":
            QuestionID = 25   #                                       25
            DialogueVar.set("De kaas die je in gedachten hebt is: camembert")
        else:
            QuestionID = 26 #                                         26
            DialogueVar.set("De kaas die je in gedachten hebt is: Mozzerella") 
        disableQuestion()
    else:
        color1.config(state="disabled")
        color2.config(state="disabled")

root = tkinter.Tk()
DialogueVar =tkinter.StringVar(value="Is de kaas geel?")
Text = tkinter.Label(textvariable=DialogueVar,font=("Comic_Sans",10)).pack()
Answer = tkinter.StringVar()
color1 = ttk.Radiobutton(root, text='Ja', value='Y', variable=Answer)
color1.pack()
color2 = ttk.Radiobutton(root, text='nee', value='N', variable=Answer)
color2.pack()
Answer.trace("w", disableQuestion)
invoer = str(Answer.get())

root.mainloop()






#################################### Oude code ####################################

# if invoer == "Y": ##### Path 10
    
#     invoer = input("zitten er gaten in? y/n: ").upper() #10

#     if invoer == "Y":

#         invoer = input("Is de kaas belachelijk duur? y/n:  ").upper() #11
#         if invoer == "Y":

#             print("De kaas die je in gedachten hebt is: Emmenthaler") #15
#         else:

#             print("De kaas die je in gedachten hebt is: Leerdammer") #16
#     else:

#         invoer = input("Is de kaas hard als steen? y/n: ").upper() #12
#         if invoer == "Y":

#             print("De kaas die je in gedachten hebt is: Pamniago Reggiano") #13
#         else:

#             print("De kaas die je in gedachten hebt is: Goudse kaas") #14

# else: #### Path 20

#     invoer = input("Heeft de kaas blauwe schimmels? y/n: ").upper() #20
#     if invoer == "Y":
        
#         invoer = ("Heeft de kaas een korst? y/n: ").upper() #21
#         if invoer == "Y":

#             print("De kaas die je in gedachten hebt is: Bleu de Rochbaron") #22
#         else:

#             print("De kaas die je in gedachten hebt is: Foumme d'Ambert") #23
#     else:
        
#         invoer = input("Heeft de kaas een korst? y/n: ").upper() #24
#         if invoer == "Y":

#             print("De kaas die je in gedachten hebt is: camembert") #25
#         else:

#             print("De kaas die je in gedachten hebt is: Mozzerella") #26

from tkinter import *
from tkinter import ttk
from coding_functions import *

# ---------------------------------------------------------------------------------- #
## Main application window
root = Tk()
root.title("Chiffrement")
root["bg"]="khaki3"
rootDimension = "650x650+400+50"
root.geometry(rootDimension)


# ---------------------------------------------------------------------------------- #
## Styles for interface
sentenceDisplayLength = 60

style = ttk.Style()
style.configure("Method.TFrame", background="SpringGreen2", border ="True")
style.configure("Method.TRadiobutton", background="SpringGreen3", font="Liberation, 14")
style.configure("Method.TLabel", background="SpringGreen4", font="Liberation, 16", justify=CENTER)
style.configure("Method2.TLabel", background="SpringGreen3", font="Liberation, 14")
style.configure("BufferMethod.TLabel", background="SpringGreen2", font="Liberation, 14")
style.configure("Method.TEntry", background="SpringGreen3", font="Liberation, 12")
style.configure("Method.TMenubutton", background="SpringGreen3", font="Liberation, 14", 
                activebackground="red",relief=FLAT)
style.configure("Sens.TFrame", background="SeaGreen1", border="True")
style.configure("Sens.TLabel", background="SeaGreen3", font="Liberation, 16")
style.configure("Sens.TRadiobutton", background="SeaGreen3", font="Liberation, 14")
style.configure("Sentence.TFrame", background="chartreuse3")
style.configure("Sentence.TLabel", background="chartreuse1", justify=CENTER, font="Liberation, 16", height=2)
style.configure("Sentence2.TLabel", background="White", height= 4, width=60, 
                justify= CENTER, font="Liberation, 12")
style.configure("Sentence.TEntry", background="LemonChiffon2", font="Liberation, 12")
style.configure("Processing.TFrame", background="Aquamarine2")
style.configure("Processing.TButton", background="Aquamarine3", font="Liberation, 14")
style.configure("Warning.TLabel", background="red", font="Liberation bold, 14", foreground="White", 
                justify=CENTER)


# ---------------------------------------------------------------------------------- #
## Events functions
def end_of_warning():
    """ This function erase the warning label, after resolution of the problem
    """
    warningMethod["background"]="SpringGreen2"
    warningMethod['text']="                                             "

def Cesar_shift():
    """ This function manages the widget for the shift choice for the Cesar method.
        It clears the widgets for the Vigenere method and the window for warning, if
        necessary, and make obvious this for Cesar method.
    """
    keyLabel.grid_forget()
    keyEntry.grid_forget()
    end_of_warning()
    shiftLabel.grid(row=1, column=3, sticky="E")
    shiftCesar.grid(row=1, column=4, sticky="W")

 
def Vigenere_key():
    """ This function manages the widget for the key entry for the Vigenere method.
        It clears the widgets for the Cesar method and the window for warning, if
        necessary, and make obvious this for Vigenere method.
    """
    shiftLabel.grid_forget()
    shiftCesar.grid_forget()
    end_of_warning()
    keyLabel.grid(row=3, column=4, pady=3, sticky="E")
    keyEntry.grid(row=3, column=6, columnspan=5, sticky="W")

def remove_widgets():
    """ This function clears the widgets for the Vigenere and Cesar methods and the 
        window for warning, if necessary.
    """
    shiftLabel.grid_forget()
    shiftCesar.grid_forget()
    keyLabel.grid_forget()
    keyEntry.grid_forget()
    end_of_warning()

def display_warning_message(message):
    """ This function makes visible the warning window for the choice of the method
        and it displays the warning message.
        "message" is the warning message to be displayed. It is a string.
    """
    warningMethod["background"] = "red"
    warningMethod["foreground"] = "white"
    warningMethod["text"] = message

def processor():
    """ This function gets the choices (method, sens, sentence to be treated) and
        manages the warning messages, if necessary.
        If all is right, it calls the function coding_manager to do the job. It
        fetchs the result and displays it.
        It is the link between the front-end and the back-end.
    """
    # Fetching of data
    methodChosen = methodChoice.get()
    if shiftChoice.get() == "(_)":
        CesarShift = 0
    else:
        CesarShift = int(shiftChoice.get())
    VigenereKey = Vigenere_key.get()
    coding_sens = sensValue.get()
    initial_sentence = Sentence.get()

    # If data are not compliant, managment of warning messages and go out.
    # For the good compliance, see the comment of the dialogue window, below.
    if not (methodChosen in [1, 2, 3, 4]):
        display_warning_message("Veuillez choisir une méthode de \nchiffrement !")
    elif (methodChosen == 1 and CesarShift==0):
        display_warning_message("Veuillez choisir un décalage !")
    elif (methodChosen == 3 and VigenereKey =="" ):
        display_warning_message("Veuillez saisir une clé \n(mot ou phrase) !")
        
    # If data are compliant, making the job and display of the result.
    else :
        finalSentence = coding_manager(methodChosen, CesarShift, VigenereKey, 
                                        coding_sens, initial_sentence)
        formattedSentence, rowNumber = cutting_long_sentence(finalSentence, sentenceDisplayLength)
        resultLabel.grid(row=0, column=0, columnspan=8, sticky=(W, E))
        resultDisplay.grid(row=1, column=0, columnspan=8, rowspan=4, sticky=(W, E), 
                           padx=5, pady=5 )

        resultDisplay["height"] = rowNumber
        resultDisplay["text"] = formattedSentence
        

def again():
    """ This function reset the entry and the display of previous text
    """
    Sentence.set("")
    resultDisplay["text"]=""
    resultDisplay["height"]= 0

def going_out():
    """ This function manages end of the application
    """
    root.quit()


# ---------------------------------------------------------------------------------- #
## Application's windows

# +++++++++++++++++++++
# Choice of the method of coding window
# In this window, the user chooses the coding method he wants to use.
#   * If he chooses the Cesar method, a widget asks him for shift value of treatment.
#   * If he chooses the Vigenere method, a widget asks him to enter the key for 
#     coding.
#   Those new windows never appear for the other method.
# The methods are numbered in range [1; 4]
# The possibles shift, for Cesar method are in range [1; 25]
# The key for Vigenere method contains at least one alphabetical character.
method = ttk.Frame(root, style="Method.TFrame")
method.pack(padx=5, pady=5) 

methodLabel = ttk.Label(method, text="Méthode de chiffrement", 
                        style="Method.TLabel")
methodLabel.grid(row=0, column=1, columnspan=9, padx=10, pady=10)

methodChoice = IntVar()
methodChoice.set(5)

    # Cesar method. The Cesar_shift method manages the widget for the shift choice.
CesarChoice = ttk.Radiobutton(method, variable=methodChoice, text="Code César", 
                              command=Cesar_shift, value=1, 
                              style="Method.TRadiobutton")
CesarChoice.grid(row=1, column=1, sticky="W", pady=2)

methodBuffer1 = ttk.Label(method, text="   ", style="BufferMethod.TLabel")
methodBuffer1.grid(row=1, column=2)         # This buffer is only for a clear layout

shiftLabel= ttk.Label(method, text="décalage : ", style="Method2.TLabel")

shiftChoice = StringVar()
shiftsList = ["(_)"]
shiftsList += [str(i) for i in range(1,26)]
shiftCesar = ttk.OptionMenu(method, shiftChoice, *shiftsList, 
                             style="Method.TMenubutton")

    # ROT13 method. This method is only a Cesar coding with a shift of 13. 
    # The function remove_widgets is cleaning the screen of not pertinent windows.
ROT13Choice = ttk.Radiobutton(method, variable=methodChoice, text="ROT13", 
                              command = remove_widgets, value=2, 
                              style="Method.TRadiobutton")
ROT13Choice.grid(row=2, column=1, sticky="W", pady=2)

VigenereChoice = ttk.Radiobutton(method, variable=methodChoice, 
                                 text="Chiffre Vigenère", 
                                 command=Vigenere_key, value=3, 
                                 style="Method.TRadiobutton")
VigenereChoice.grid(row=3, column=1, sticky="W", pady=2)

methodBuffer2 = ttk.Label(method, text="   ", style="BufferMethod.TLabel")
methodBuffer2.grid(row=3, column=2)         # This buffer is only for a clear layout

keyLabel = ttk.Label(method, text="clé : ", style="Method2.TLabel")
Vigenere_key = StringVar()
keyEntry = ttk.Entry(method, textvariable=Vigenere_key, style="Method.TEntry")

    # Polybe's square method. 
    # The function remove_widgets is cleaning the screen of not pertinent windows.
PolybeSquareChoice = ttk.Radiobutton(method, variable=methodChoice, 
                                    text="Carré de Polybe", command = remove_widgets, 
                                    value=4, style="Method.TRadiobutton")
PolybeSquareChoice.grid(row=4, column=1, sticky="W", pady=2)

    # Warning windows for wrong (or missing) data, if necessary.
warningMethod = ttk.Label(method, 
                          text="                                             ",
                          style="BufferMethod.TLabel") 
        # The blank line is for a good layout
warningMethod.grid(row=5, column=1, columnspan=9)

# +++++++++++++++++++++
# Choice of the sens of treatment. 0 is for coding, 1 for uncoding.
sens = ttk.Frame(root, style="Sens.TFrame")
sens.pack(padx=10, pady=10)

sensLabel = ttk.Label(sens, text="Sens du traitement", style="Sens.TLabel", 
                      justify=CENTER)
sensLabel.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

sensValue = IntVar()
sensValue.set(0)

codingSens = ttk.Radiobutton(sens, variable=sensValue, text="Chiffrement", 
                             value=0,
                             style="Sens.TRadiobutton")
codingSens.grid(row=1, column=0, sticky="W", padx=5, pady=5)

uncodingSens = ttk.Radiobutton(sens, variable=sensValue, text="Déchiffrement", 
                               value=1,
                               style="Sens.TRadiobutton")
uncodingSens.grid(row=1, column=3, padx=5, pady=5)

# +++++++++++++++++++++
# Entry of the sentence to be treated.
sentence = ttk.Frame(root, style="Sentence.TFrame")
sentence.pack(padx=10, pady=10)

entrySentenceLabel = ttk.Label(sentence, 
                        text="Veuillez saisir une phrase à traiter ci-dessous : ",
                        style="Sentence.TLabel")
entrySentenceLabel.grid(column=0, row= 0, columnspan=8, sticky="NS")

Sentence = StringVar()
sentenceEntry = ttk.Entry(sentence, textvariable=Sentence, style="Sentence.TEntry")
sentenceEntry.grid(column=0, row = 1, columnspan= 8, sticky=(W, E), padx=5, pady=5)

# +++++++++++++++++++++
# Display of the treated entence.
results = ttk.Frame(root, style="Sentence.TFrame")
results.pack(padx=10, pady=10)

resultLabel = ttk.Label(results, 
                        text="Voici le résultat du traitement de la phrase : ",
                        style="Sentence.TLabel")

resultDisplay = Label(results, text = "", background="ivory", height= 1, width=sentenceDisplayLength, 
                font="Liberation, 12")

# +++++++++++++++++++++
# Dashboard of the application.
processing = ttk.Frame(root, style="Processing.TFrame")
processing.pack(padx=5,pady=5)
    # Button to launch the treatment
processingButton= ttk.Button(processing, text="Traitement",
                               style="Processing.TButton", command=processor) 
processingButton.grid(row=0, column=0, padx=10, pady=10) 
    # Button to initialize the entry (remove existing text)
againButton= ttk.Button(processing, text="Nouvelle phrase", 
                        style="Processing.TButton", command=again)
againButton.grid(row=0, column=3, padx=10, pady=10)
    # Button to quit the application. Good bye !
quitButton = ttk.Button(processing, text="Quitter", 
                        style="Processing.TButton", command=going_out)
quitButton.grid(row=0, column=5, padx=10, pady=10)

root.mainloop()
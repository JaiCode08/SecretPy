import customtkinter # A module which makes tkinter look better and more customizeable
import tkinter as tk # A built-in python module used to create guis
import random, pyperclip # The "random" module is a built-in module that is used to include random events. The "pyperclip" module is used to copy the "key".
from toolTip import CreateToolTip

# These variables handle the generation of key.
symbols = list("abcdefghijklmnopqrstuvwxyz") # This var contains the symbols used in the key
changer = symbols.copy() # This var is used to play around and change the symbols in the "symbols" var.
key = "" # Initlizaing Key

# Screen variables
screenWidth = 600
screenHeight = 400
scene = "main" # Depending on this variable frames are shown and deleted

# Basic setup for tkinter & customtkinter
customtkinter.set_appearance_mode("System")
app = customtkinter.CTk()
app.geometry(f'{screenWidth}x{screenHeight}')
app.title("SecretPy")
app.iconbitmap("images/detective.ico")

"""
Here we create customtkinter frames.
Think of each frame as a scene and the widgets are different components(ex: buttons, pictures) of the frame.
"""
main = customtkinter.CTkFrame(app, width = screenWidth, height = screenHeight)
gen = customtkinter.CTkFrame(app, width = screenWidth, height = screenHeight)
enterKey = customtkinter.CTkFrame(app, width = screenWidth, height = screenHeight)
encodeDecode = customtkinter.CTkFrame(app, width = screenWidth, height = screenHeight)
settings = customtkinter.CTkFrame(app, width = screenWidth, height = screenHeight)

# All of the code is put into functions since customtkinter/tkinter only runs functions when buttons are pressed

#
def keyLabelFunc(master):
    keyLabel = customtkinter.CTkLabel(master = master, text = key, font = ("Lucida Sans", 13), width = 250)
    keyLabel.place(x = screenWidth / 2 - 125, y = screenHeight / 2 - 80)    

def backButtonFunc(master):
    backButton = customtkinter.CTkButton(master = master, text = "", image = tk.PhotoImage(file = "images/back-button.png"), command = switchBack, width = 35)
    backButton.place(x = 10, y = 10)

# Button functions
def goToGen():
    global key, scene
    changer = symbols.copy()
    key = ""
    key = list(key)
    while (len(changer) != 0):
        pos = random.randint(0, len(changer) - 1)
        key.append(changer[pos])
        changer.pop(pos)
    key = "".join(key)
    main.forget()
    keyLabelFunc(gen)
    backButtonFunc(gen)
    gen.pack()
    scene = "generate"

def goToEnterKey():
    global scene
    main.forget()
    enterKey.pack()
    backButtonFunc(enterKey)
    scene = "enter key"

def goToSettings():
    global scene
    settings.pack()
    scene = "settings"
    passFile = open("data/pass.txt", "r")
    boolFile = open("data/passBool.txt", "r")
    setFrame = customtkinter.CTkFrame(settings, width = screenWidth, height = screenHeight, fg_color = "#2a2d2e")
    passFrame = customtkinter.CTkFrame(settings, width = screenWidth, height = screenHeight, fg_color = "#2a2d2e")

    def showHide(widget):
        widget.configure(show = "")
        widget.after(750, lambda: widget.configure(show = "*"))
    
    def eraseAllData():
        global passFile, boolFile
        passFile = open("data/pass.txt", "r")
        userPass = erasePass.get()
        if (passFile.read() == userPass):
            passFile.close()
            passFile = open("data/pass.txt", "w")
            passFile.close
            boolFile = open("data/passBool.txt", "w")
            boolFile.write("false")
            boolFile.close()
            keyFile = open("data/key.txt", "w")
            keyFile.close()
            msgFile = open("data/saved_msg.txt", "w")
            msgFile.close()
            passFrame.forget()
            setFrame.pack()
        else:
            eraseWarning = customtkinter.CTkLabel(master = passFrame, text = "Wrong Password!", font = ("Lucida Sans", 11), text_color = "#ff0000")
            eraseWarning.place(x = screenWidth / 2 - 80, y = screenHeight / 2 + 35)
            eraseWarning.after(1500, lambda: eraseWarning.destroy())

    def changePass():
        global passFile
        passFile = open("data/pass.txt", "r")
        oldPass = passFile.read()
        passFile.close()
        if (oldPass == currentPass.get()):
            passFile = open("data/pass.txt", "w")
            passFile.write(newPass.get())
            passFile.close()
            warningPassLabel = customtkinter.CTkLabel(master = passFrame, text = "Password set!", font = ("Lucida Sans", 11), text_color = "#0dd127")
            warningPassLabel.place(x = screenWidth / 2 - 70, y = screenHeight / 2 - 140)
            warningPassLabel.after(1500, lambda: warningPassLabel.destroy())
        else:
            warningPassLabel = customtkinter.CTkLabel(master = passFrame, text = "Password entered does not match current password!", font = ("Lucida Sans", 11), text_color = "#ff0000")
            warningPassLabel.place(x = screenWidth / 2 - 205, y = screenHeight / 2 - 140)
            warningPassLabel.after(1500, lambda: warningPassLabel.destroy())

    def setPass():
        global passFile, boolFile
        passFile = open("data/pass.txt", "w")
        boolFile = open("data/passBool.txt", "w")
        passFile.write(setPassInput.get())
        boolFile.write("true")
        passFile.close()
        boolFile.close()
        setFrame.forget()
        passFrame.pack()

    setPassLabel = customtkinter.CTkLabel(master = setFrame, text = "Set Password", font = ("Lucida Sans", 13))
    setPassLabel.place(x = screenWidth / 2 - 80, y = screenHeight / 2 - 90)
    setPassInput = customtkinter.CTkEntry(master = setFrame, width = 208, height = 30, font = ("Lucida Sans", 10))
    setPassInput.insert(0, "Set password here...")
    def clearKey(event):
        setPassInput.delete(0, tk.END)
        setPassInput.configure(show = "*")
    setPassInput.bind("<FocusIn>", clearKey)
    setPassInput.place(x = screenWidth / 2 - 125, y = screenHeight / 2 - 50)
    setPassButton = customtkinter.CTkButton(master = setFrame, text = "Set Password", width = 170, command = setPass)
    setPassButton.place(x = screenWidth / 2 - 85, y = screenHeight / 2 - 10)
    setView = customtkinter.CTkButton(master = setFrame, text = "", image = tk.PhotoImage(file = "images/view.png"), width = 29, height = 29, command = lambda: showHide(setPassInput))
    setView.place(x = screenWidth / 2 + 90, y = screenHeight / 2 - 50)

    passHeading = customtkinter.CTkLabel(master = passFrame, text = "Reset Password", font = ("Lucida Sans", 13))
    passHeading.place(x = screenWidth / 2 - 70, y = screenHeight / 2 - 135)
    currentPass = customtkinter.CTkEntry(master = passFrame, width = 208, height = 30, font = ("Lucida Sans", 10))
    currentPass.insert(0, "Type current password here...")
    def clearKey(event):
        currentPass.delete(0, tk.END)
        currentPass.configure(show = "*")
    currentPass.bind("<FocusIn>", clearKey)
    currentPass.place(x = screenWidth / 2 - 125, y = screenHeight / 2 - 100)
    setView1 = customtkinter.CTkButton(master = passFrame, text = "", image = tk.PhotoImage(file = "images/view.png"), width = 29, height = 29, command = lambda: showHide(currentPass))
    setView1.place(x = screenWidth / 2 + 90, y = screenHeight / 2 - 100)
    newPass = customtkinter.CTkEntry(master = passFrame, width = 208, height = 30, font = ("Lucida Sans", 10))
    newPass.insert(0, "Type new password here...")
    def clearKey(event):
        newPass.delete(0, tk.END)
        newPass.configure(show = "*")
    newPass.bind("<FocusIn>", clearKey)
    newPass.place(x = screenWidth / 2 - 125, y = screenHeight / 2 - 70)
    setView2 = customtkinter.CTkButton(master = passFrame, text = "", image = tk.PhotoImage(file = "images/view.png"), width = 29, height = 29, command = lambda: showHide(newPass))
    setView2.place(x = screenWidth / 2 + 90, y = screenHeight / 2 - 70)
    changePassButton = customtkinter.CTkButton(master = passFrame, text = "Change password", width = 170, command = changePass)
    changePassButton.place(x = screenWidth / 2 - 85, y = screenHeight / 2 - 30)
    line = customtkinter.CTkLabel(master = passFrame, text = "-------------------------------------------", font = ("Lucida Sans", 21))
    line.place(x = screenWidth / 2 - 200, y = screenHeight / 2)
    eraseHeading = customtkinter.CTkLabel(master = passFrame, text = "Erase all data", font = ("Lucida Sans", 13))
    eraseHeading.place(x = screenWidth / 2 - 70, y = screenHeight / 2 + 35)
    erasePass = customtkinter.CTkEntry(master = passFrame, width = 208, height = 30, font = ("Lucida Sans", 10))
    erasePass.insert(0, "Enter password here...")
    def clearKey(event):
        erasePass.delete(0, tk.END)
        erasePass.configure(show = "*")
    erasePass.bind("<FocusIn>", clearKey)
    erasePass.place(x = screenWidth / 2 - 125, y = screenHeight / 2 + 70)
    setView3 = customtkinter.CTkButton(master = passFrame, text = "", image = tk.PhotoImage(file = "images/view.png"), width = 29, height = 29, command = lambda: showHide(erasePass))
    setView3.place(x = screenWidth / 2 + 90, y = screenHeight / 2 + 70)
    eraseButton = customtkinter.CTkButton(master = passFrame, text = "Erase Data", width = 170, command = eraseAllData)
    eraseButton.place(x = screenWidth / 2 - 85, y = screenHeight / 2 + 110)
 
    if (boolFile.read() == "false"):
        boolFile.close()
        passFrame.forget()
        setFrame.pack()

    else:
        setFrame.forget()
        passFrame.pack()

    backButtonFunc(settings)
    setHeading = customtkinter.CTkLabel(master = settings, text = "Settings", font = ("Lucida Sans", 25))
    setHeading.place(x = screenWidth / 2 - 70, y = screenHeight / 2 - 190)
    main.forget()
    settings.pack()

def genNewKey():
    global key, keyLabel
    changer = symbols.copy()
    key = ""
    key = list(key)
    while (len(changer) != 0):
        pos = random.randint(0, len(changer) - 1)
        key.append(changer[pos])
        changer.pop(pos)
    key = "".join(key)
    keyLabelFunc(gen)

def copyKey():
    pyperclip.copy(key)

def submitKey():
    global key, scene
    invalid = False
    input = keyInput.get()
    input = list(input)

    for i in range(len(input)):
        if (input[i] not in symbols):
            invalid = True
            break
    input = keyInput.get()
    input = list(input)

    # for i in range(len(input)):
    #     if (input[i].isupper()):
    #         upper = True
    #         break
    
    input = keyInput.get()
    input = list(input)
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if (input[i] == input[j]):
                invalid = True
                break
            
    if (len(input) != len(symbols) or invalid == True):
        warningLabel = customtkinter.CTkLabel(master = enterKey, text = "Invalid key format!", font = ("Lucida Sans", 13), text_color = "#ff0000", width = 250)
        warningLabel.place( x = screenWidth / 2 - 125, y = screenHeight / 2 - 80)
    else:
        input = keyInput.get()
        key = input
        enterKey.forget()
        encodeDecode.pack()
        scene = "encode/decode"

def verify(button):
    boolFile = open("data/passBool.txt", "r")
    if (boolFile.read() == "false"):
        match(button):
            case "save":
                warningLabel = customtkinter.CTkLabel(master = gen, text = "Please set password in settings to use this feature!", font = ("Lucida Sans", 11), text_color = "#ff0000", width = 250)
                warningLabel.place(x = screenWidth / 2 - 190, y = screenHeight / 2 + 50)
                warningLabel.after(1500, lambda: warningLabel.destroy())
            case "load":
                warningLabel = customtkinter.CTkLabel(master = enterKey, text = "Please set password in settings to use this feature!", font = ("Lucida Sans", 11), text_color = "#ff0000", width = 250)
                warningLabel.place(x = screenWidth / 2 - 190, y = screenHeight / 2 - 75)
                warningLabel.after(1500, lambda: warningLabel.destroy())
        return
    boolFile.close()

    passWin = customtkinter.CTkToplevel()
    veriWidth = 400
    veriHeight = 200
    passWin.geometry(f'{veriWidth}x{veriHeight}')
    passWin.title("Verification")
    passWin.iconphoto(False, tk.PhotoImage(file = "images/verify.png"))
    passWin.grab_set()

    passWin.protocol("WM_DELETE_WINDOW", lambda: [passWin.destroy(), verify(button)])

    def showHide(widget):
        widget.configure(show = "")
        widget.after(750, lambda: widget.configure(show = "*"))

    def checkPass():
        global scene, key
        passFile = open("data/pass.txt", "r")
        if (passFile.read() == veriPassInput.get()):
            passFile.close()
            passWin.destroy()
            passWin.grab_release()
            match(button):
                case "save":
                    keyFile = open("data/key.txt", "w")
                    keyFile.write(key)
                    successLabel = customtkinter.CTkLabel(master = gen, text = "Key saved successfully!", font = ("Lucida Sans", 11), text_color = "#00ff00", width = 250)
                    successLabel.place(x = screenWidth / 2 - 120, y = screenHeight / 2 + 50)
                    successLabel.after(1500, lambda: successLabel.destroy())
                case "load":
                    keyFile = open("data/key.txt", "r")
                    key = keyFile.read()
                    keyFile.close()
                    backButtonFunc(encodeDecode)
                    enterKey.forget()
                    encodeDecode.pack()
                    scene = "encode/decode"

        else: 
            veriWarning = customtkinter.CTkLabel(master = passWin, text = "Wrong Password!", font = ("Lucida Sans", 11), text_color = "#ff0000")
            veriWarning.place(x = veriWidth / 2 - 80, y = veriHeight / 2 - 100)
            veriWarning.after(1500, lambda: veriWarning.destroy())

    verifyLabel = customtkinter.CTkLabel(master = passWin, text = "Verify Password", font = ("Lucida Sans", 13))
    verifyLabel.place(x = veriWidth / 2 - 90, y = veriHeight / 2 - 60)
    veriPassInput = customtkinter.CTkEntry(master = passWin, width = 208, height = 30, font = ("Lucida Sans", 10))
    veriPassInput.insert(0, "Enter password here...")
    def clearKey(event):
        veriPassInput.delete(0, tk.END)
        veriPassInput.configure(show = "*")
    veriPassInput.bind("<FocusIn>", clearKey)
    veriPassInput.place(x = veriWidth / 2 - 125, y = veriHeight / 2 - 10)
    veriButton = customtkinter.CTkButton(master = passWin, text = "Verify", width = 170, command = checkPass)
    veriButton.place(x = veriWidth / 2 - 85, y = veriHeight / 2 + 30)
    setView = customtkinter.CTkButton(master = passWin, text = "", image = tk.PhotoImage(file = "images/view.png"), width = 29, height = 29, command = lambda: showHide(veriPassInput))
    setView.place(x = veriWidth / 2 + 90, y = veriHeight / 2 - 10)

def getOption(choice):
    global option
    if (choice == "Encode"):
        label2 = customtkinter.CTkLabel(master = encodeDecode, text = "Encoded Message", font = ("Lucida Sans", 12))
        label2.place(x = screenWidth / 2 + 110, y = screenHeight / 2 - 145)
        encodeDecode.forget()
        encodeDecode.pack()
    elif (choice == "Decode"):
        label2 = customtkinter.CTkLabel(master = encodeDecode, text = "Decoded Message", font = ("Lucida Sans", 12))
        label2.place(x = screenWidth / 2 + 110, y = screenHeight / 2 - 145)
        encodeDecode.forget()
        encodeDecode.pack()
    option = choice

def copyEncrypt():
    val = rightTextbox.get("1.0", "end-1c")
    pyperclip.copy(val)

def convertMsg():
    if (option == None or option == "Select"):
        warningLabel = customtkinter.CTkLabel(master = encodeDecode, text = "Please select an option first!", font = ("Lucida Sans", 11), text_color = "#ff0000", width = 250)
        warningLabel.place(x = screenWidth / 2 - 130, y = screenHeight / 2 - 145)
        warningLabel.after(1500, lambda: warningLabel.destroy())
    elif (option == "Encode"):
        plainText = leftTextbox.get("1.0", "end-1c")
        encryptedText = []
        for i in range(len(plainText)):
            if (plainText[i].lower() in symbols):
                if (plainText[i].isupper()):
                    orgPos = symbols.index(plainText[i].lower())
                    encryptedText.append(key[orgPos].upper())        
                else:
                    orgPos = symbols.index(plainText[i].lower())
                    encryptedText.append(key[orgPos])
            else:
                encryptedText.append(plainText[i])
        rightTextbox.delete("1.0", "end-1c")
        rightTextbox.insert("1.0", "".join(encryptedText))
    elif (option == "Decode"):
        plainText = []
        encryptedText = leftTextbox.get("1.0", "end-1c")
        for i in range(len(encryptedText)):
            if (encryptedText[i].lower() in key):
                if (encryptedText[i].isupper()):            
                    orgPos = key.index(encryptedText[i].lower())
                    plainText.append(symbols[orgPos].upper())
                else:
                    orgPos = key.index(encryptedText[i].lower())
                    plainText.append(symbols[orgPos])
            else:
                plainText.append(encryptedText[i])
        rightTextbox.delete("1.0", "end-1c")
        rightTextbox.insert("1.0", "".join(plainText))

def loadMsg():
    msgFile = open("data/saved_msg.txt", "r")
    leftTextbox.delete("1.0", "end-1c")
    leftTextbox.insert("1.0", msgFile.read())
    successLabel = customtkinter.CTkLabel(master = encodeDecode, text = "Message Loaded", font = ("Lucida Sans", 11), text_color = "#00ff00", width = 250)
    successLabel.place(x = screenWidth / 2 - 120, y = screenHeight / 2 - 145)
    successLabel.after(1500, lambda: successLabel.destroy())
    msgFile.close()

def saveMsg():
    msgFile = open("data/saved_msg.txt", "w")
    msgFile.write(rightTextbox.get("1.0", "end-1c"))
    successLabel = customtkinter.CTkLabel(master = encodeDecode, text = "Message Saved", font = ("Lucida Sans", 11), text_color = "#00ff00", width = 250)
    successLabel.place(x = screenWidth / 2 - 120, y = screenHeight / 2 - 145)
    successLabel.after(1500, lambda: successLabel.destroy())
    msgFile.close()

def switchBack():
    global scene
    match (scene):
        case "generate":
            gen.forget()
            main.pack()
            scene = "main"
        case "enter key":
            enterKey.forget()
            main.pack()
            scene = "main"
        case "encode/decode":
            encodeDecode.forget()
            enterKey.pack()
            scene = "enter key"
        case "settings":
            settings.forget()
            main.pack()
            scene = "main"

# Main page
headingLabel = customtkinter.CTkLabel(master = main, text = "SecretPy", font = ("Freestyle Script", 50), width = 250, height = 75)
headingLabel.place(x = screenWidth / 2 - 125, y = screenHeight / 2 - 175)
infoLabel = customtkinter.CTkLabel(master = main, text = "A MONO-ALPHABETIC CIPHER TOOL", font = ("Bahnschrift SemiBold", 13), width = 300)
infoLabel.place(x = screenWidth / 2 - 150, y = screenHeight / 2 - 100)
genKeyButton = customtkinter.CTkButton(master = main, text = "Generate Key", command = goToGen, width = 170)
genKeyButton.place(x = screenWidth / 2 - 70, y = screenHeight / 2 - 20)
enterKeyButton = customtkinter.CTkButton(master = main, text = "Enter Key", command = goToEnterKey, width = 170)
enterKeyButton.place(x = screenWidth / 2 - 70, y = screenHeight / 2 + 25)
settingsButton = customtkinter.CTkButton(master = main, text = "", image = tk.PhotoImage(file = "images/settings.png"), command = goToSettings, width = 35)
settingsButton.place(x = 555, y = 10)
main.pack()

# Generation page
genKeyLabel = customtkinter.CTkLabel(master = gen, text = "GENERATED KEY", font = ("Lucida Sans", 18), width = 250, height = 50)
genKeyLabel.place(x = screenWidth / 2 - 125,  y = screenHeight / 2 - 195)
genNewKeyButton = customtkinter.CTkButton(master = gen, text = "Generate New Key", command = genNewKey, width = 170)
genNewKeyButton.place(x = screenWidth / 2 - 85, y = screenHeight / 2)
genCopyButton = customtkinter.CTkButton(master = gen, text = "", image = tk.PhotoImage(file = "images/copy-button.png"), command = copyKey, width = 50)
genCopyButton.place(x = screenWidth / 2 - 55, y = screenHeight / 2 - 50)
CreateToolTip(genCopyButton, "Copy Key")
genSaveButton = customtkinter.CTkButton(master = gen, text = "", image = tk.PhotoImage(file = "images/save-button.png"), command = lambda: [verify("save")], width = 50)
genSaveButton.place(x = screenWidth / 2 + 5, y = screenHeight / 2 - 50)
CreateToolTip(genSaveButton, "Save Key")

# Enter key
keyInput = customtkinter.CTkEntry(master = enterKey, width = 250, height = 30, font = ("Lucida Sans", 10))
keyInput.insert(0, "Enter key here...")
def clearKey(event):
    keyInput.delete(0, tk.END)
keyInput.bind("<FocusIn>", clearKey)
keyInput.place(x = screenWidth / 2 - 125, y = screenHeight / 2 - 40)
submitButton = customtkinter.CTkButton(master = enterKey, text = "Submit", command = submitKey, width = 75)
submitButton.place(x = screenWidth / 2 - 90, y = screenHeight / 2)
loadKeyButton = customtkinter.CTkButton(master = enterKey, text = "Load Key", command = lambda: [verify("load")], width = 75)
loadKeyButton.place(x = screenWidth / 2, y = screenHeight / 2)

# Encode/Decode
backButtonFunc(encodeDecode)
encodeDecodeOption = customtkinter.CTkOptionMenu(master = encodeDecode, values = ["Select", "Encode", "Decode"], width = 150, command = getOption)
encodeDecodeOption.place(x = screenWidth / 2 - 75, y = screenHeight / 2 - 185)
leftTextbox = customtkinter.CTkTextbox(master = encodeDecode, width = 200, height = 270, font = ("Lucida Sans", 9), fg_color = "#474747")
leftTextbox.place(x = screenWidth / 2 - 280, y = screenHeight / 2 - 110)
rightTextbox = customtkinter.CTkTextbox(master = encodeDecode, width = 200, height = 270, font = ("Lucida Sans", 9), fg_color = "#474747")
rightTextbox.place(x = screenWidth / 2 + 80, y = screenHeight / 2 - 110)
label1 = customtkinter.CTkLabel(master = encodeDecode, text = "Enter text", font = ("Lucida Sans", 12))
label1.place(x = screenWidth / 2 - 250, y = screenHeight / 2 - 145)
convertButton = customtkinter.CTkButton(master = encodeDecode, text = "Convert", command = convertMsg, width = 100)
convertButton.place(x = screenWidth / 2 - 50, y = screenHeight / 2 + 10)
loadMsg = customtkinter.CTkButton(master = encodeDecode, text = "Load", command = loadMsg, width = 100)
loadMsg.place(x = screenWidth / 2 - 230, y = screenHeight / 2 + 167)
copyMsg = customtkinter.CTkButton(master = encodeDecode, text = "Copy", command = lambda: [copyEncrypt()], width = 70)
copyMsg.place(x = screenWidth / 2 + 100, y = screenHeight / 2 + 167)
saveMsg = customtkinter.CTkButton(master = encodeDecode, text = "Save", command = saveMsg, width = 70)
saveMsg.place(x = screenWidth / 2 + 190, y = screenHeight / 2 + 167)

app.mainloop()
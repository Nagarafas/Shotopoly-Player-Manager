import customtkinter as ctk
import platform
if platform.system() == "Windows": import Bitmap_Image_Create as windowImage
else: import Image_Create as windowImage

class ExchangeManager(ctk.CTkToplevel):
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = window
        self.gridSize = window.gridSize
        self.font = window.font
        
        self.mainFrame = ctk.CTkFrame(self)
        self.players = self.window.players
        
    def drawWindow(self):
        self.gridInit()
        self.windowInit()
        self.main()

    def gridInit(self):
        for i in range(self.gridSize):
            self.grid_rowconfigure(i, weight = 1)
            self.grid_columnconfigure(i, weight = 1)
            
            self.mainFrame.grid_rowconfigure(i, weight = 1)
            self.mainFrame.grid_columnconfigure(i, weight = 1)
    
    def windowInit(self):
        self.geometry("600x200")
        self.resizable(True, True)
        self.title("Exchange Manager")
        
        windowImage.Apply(self)
        
        self.mainFrame.grid(row = 0, column = 0, columnspan = 20, rowspan= 20, sticky = "nsew")  
 
    def playerNames(self):
        players = []
        for player in self.window.players:
            players.append(player.name)
        return players
 
    def transferFunds(self):
        for player in self.players:
            if player.name == self.senderPicker.get():
                sender = player
            if player.name == self.receiverPicker.get():
                receiver = player
        try:
            funds = int(self.amountEntry.get())
        except:
            self.statusLbl.configure(text = "Please enter a number")
        else:
            if funds > sender.money and sender.name.lower() == "center":
                self.statusLbl.configure(text = "Insufficient Funds")
            else:
                sender.decrMoney(funds)
                receiver.incrMoney(funds)
                
                sender.updateLabels()
                receiver.updateLabels()
                self.statusLbl.configure(text = f"Successfully Tranfered €{funds}")
                self.after(10000, lambda : self.window.saveProgress(auto=1))
        
        self.updateMoneyLbl()        
    
    def getFunds(self, isSender = True):
        for player in self.players:
            if player.name == self.senderPicker.get():
                sender = player
            if player.name == self.receiverPicker.get():
                receiver = player
                
        if isSender:
            if sender.name == "Bank":
                return "∞"
            return sender.getMoney()
        else:
            if receiver.name == "Bank":
                return "∞"
            return receiver.getMoney()
        
    def swap(self):
        temp = self.senderPicker.get()
        self.senderPicker.set(self.receiverPicker.get())
        self.receiverPicker.set(temp)
        
        self.updateMoneyLbl()
    
    def send2Bank(self):
        self.senderPicker.set("Bank")
        self.updateMoneyLbl()
    
    def rec2Bank(self):
        self.receiverPicker.set("Bank")
        self.updateMoneyLbl()
        
    def updateMoneyLbl(self):
        self.senderMoneyLbl.configure(text = self.getFunds())
        self.receiverMoneyLbl.configure(text = self.getFunds(False))
        
    def main(self):
        playerNamesList = self.playerNames()
        self.senderLbl = ctk.CTkLabel(master = self.mainFrame, text= "SENDER", font = (self.font, 26, "bold"))
        self.amountLbl = ctk.CTkLabel(master = self.mainFrame, text= "AMOUNT", font = (self.font, 26, "bold"))
        self.receiverLbl = ctk.CTkLabel(master = self.mainFrame, text= "RECEIVER", font = (self.font, 26, "bold"))
        
        self.senderLbl.grid( row = 0, column = 1,  columnspan = 4, pady = (5, 5), padx = (5, 5), sticky = "ew")
        self.amountLbl.grid(row = 0, column = 8,  columnspan = 4, pady = (5, 5), padx = (5, 5), sticky = "ew")
        self.receiverLbl.grid(row = 0, column = 16,  columnspan = 4, pady = (5, 5), padx = (5, 5), sticky = "ew")
        
        self.senderPicker = ctk.CTkOptionMenu(master = self.mainFrame, values = playerNamesList, width=200, fg_color="#9F1133", font = (self.font, 20), dropdown_font = (self.font, 18), command = lambda _: self.updateMoneyLbl())
        self.amountEntry = ctk.CTkEntry(master = self.mainFrame, font = (self.font, 20))
        self.receiverPicker = ctk.CTkOptionMenu(master = self.mainFrame, values = playerNamesList, width=200, fg_color="#119F33", font = (self.font, 20), dropdown_font = (self.font, 18), command = lambda _: self.updateMoneyLbl())
        
        self.senderPicker.grid(row = 2, column = 1,  columnspan = 4, pady = (5, 5), padx = (5, 5))
        self.amountEntry.grid(row = 2, column = 8,  columnspan = 4, pady = (5, 5), padx = (5, 5), sticky = "ew")
        self.receiverPicker.grid(row = 2, column = 16,  columnspan = 4, pady = (5, 5), padx = (5, 5))
        
        self.swapButton = ctk.CTkButton(master = self.mainFrame, text = "↺", font = (self.font, 16), width=10, command = self.swap)
        self.setSendBank = ctk.CTkButton(master = self.mainFrame, text = "🏦", font = (self.font, 16), width=10, command = self.send2Bank)
        self.setRecBank = ctk.CTkButton(master = self.mainFrame, text = "🏦", font = (self.font, 16), width=10, command = self.rec2Bank)
        
        self.swapButton.grid(row = 3, column = 8,  columnspan = 4, pady = (0, 0), padx = (0, 0))
        self.setSendBank.grid(row = 2, column = 0,  columnspan = 1, pady = (0, 0), padx = (5, 0))
        self.setRecBank.grid(row = 2, column = 20,  columnspan = 1, pady = (0, 0), padx = (0, 5))
        
        self.senderMoneyLbl = ctk.CTkLabel(master = self.mainFrame, font=(self.font, 18), text=self.getFunds())
        self.receiverMoneyLbl = ctk.CTkLabel(master = self.mainFrame, font=(self.font, 18), text=self.getFunds(False))
        
        self.senderMoneyLbl.grid(row = 3, column = 1,  columnspan = 4, pady = (0, 0), padx = (5, 5))
        self.receiverMoneyLbl.grid(row = 3, column = 16,  columnspan = 4, pady = (0, 0), padx = (5, 5))
        
        self.transferButton = ctk.CTkButton(master = self.mainFrame, text = "Transfer", font = (self.font, 20),  fg_color="#0011AA", hover_color="#00118F", command = self.transferFunds)
        self.transferButton.grid(row = 20, column = 7,  columnspan = 5, pady = (5, 5), padx = (5, 5), sticky = "ew")
        
        self.statusLbl = ctk.CTkLabel(master = self.mainFrame, text= "", font = (self.font, 20))
        self.statusLbl.grid(row = 10, column = 0,  columnspan = 20, pady = (5, 5), padx = (5, 5), sticky = "ew")
        
        self.bind("<Return>", lambda _: self.transferFunds())
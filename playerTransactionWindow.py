import customtkinter as ctk
import platform
if platform.system() == "Windows": import Bitmap_Image_Create as windowImage
else: import Image_Create as windowImage

class ExhangeManager(ctk.CTkToplevel):
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = window
        self.gridSize = window.gridSize
        self.font = window.font
        
        self.mainFrame = ctk.CTkFrame(self)
        self.players = self.window.players
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
        self.geometry("500x200")
        self.resizable(True, True)
        self.title("Exchange Manager")
        
        windowImage.Apply(self)
        
        self.mainFrame.grid(row = 0, column = 0, columnspan = 20, rowspan= 20, pady = (5, 5), padx = (5, 5), sticky = "nsew")  
 
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
            if funds > sender.money:
                self.statusLbl.configure(text = "Insufficient Funds")
            else:
                sender.money -= funds
                receiver.money += funds
                
                sender.updateLabels()
                receiver.updateLabels()
                self.statusLbl.configure(text = "Transfer Successful")
                self.after(10000, lambda : self.saveProgress(auto=1))
                
            
 
    def main(self):
        playerNamesList = self.playerNames()
        self.senderLbl = ctk.CTkLabel(master = self.mainFrame, text= "SENDER", font = (self.font, 26, "bold"))
        self.amountLbl = ctk.CTkLabel(master = self.mainFrame, text= "AMOUNT", font = (self.font, 26, "bold"))
        self.receiverLbl = ctk.CTkLabel(master = self.mainFrame, text= "RECEIVER", font = (self.font, 26, "bold"))
        
        self.senderLbl.grid( row = 0, column = 0,  columnspan = 5, pady = (5, 5), padx = (5, 5), sticky = "ew")
        self.amountLbl.grid(row = 0, column = 7,  columnspan = 5, pady = (5, 5), padx = (5, 5), sticky = "ew")
        self.receiverLbl.grid(row = 0, column = 15,  columnspan = 5, pady = (5, 5), padx = (5, 5), sticky = "ew")
        
        self.senderPicker = ctk.CTkOptionMenu(master = self.mainFrame, values = playerNamesList,  fg_color="#9F1133", font = (self.font, 20))
        self.amountEntry = ctk.CTkEntry(master = self.mainFrame, font = (self.font, 20))
        self.receiverPicker = ctk.CTkOptionMenu(master = self.mainFrame, values = playerNamesList,  fg_color="#119F33", font = (self.font, 20))
        
        self.senderPicker.grid(row = 2, column = 0,  columnspan = 5, pady = (5, 5), padx = (5, 5), sticky = "ew")
        self.amountEntry.grid(row = 2, column = 7,  columnspan = 5, pady = (5, 5), padx = (5, 5), sticky = "ew")
        self.receiverPicker.grid(row = 2, column = 15,  columnspan = 5, pady = (5, 5), padx = (5, 5), sticky = "ew")
        
        self.transferButton = ctk.CTkButton(master = self.mainFrame, text = "Transfer", font = (self.font, 20),  fg_color="#0011AA", hover_color="#00118F", command = self.transferFunds)
        self.transferButton.grid(row = 20, column = 7,  columnspan = 5, pady = (5, 5), padx = (5, 5), sticky = "ew")
        
        self.statusLbl = ctk.CTkLabel(master = self.mainFrame, text= "", font = (self.font, 20))
        self.statusLbl.grid(row = 10, column = 0,  columnspan = 20, pady = (5, 5), padx = (5, 5), sticky = "ew")
        
        self.bind("<Return>", lambda _: self.transferFunds())
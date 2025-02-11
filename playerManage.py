import customtkinter as ctk
import platform
if platform.system() == "Windows": import Bitmap_Image_Create as windowImage
else: import Image_Create as windowImage

class Manage(ctk.CTkToplevel):
    def __init__(self, playerData, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.playerData = playerData
        self.gridSize = 20
        
        self.window = playerData.window
        self.font = playerData.font
        
        self.tempPlayerName = playerData.name
        self.tempPlayerMoney = playerData.money
        
        self.mainFrame = ctk.CTkFrame(self)
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
        self.geometry("420x300")
        self.resizable(True, True)
        self.title("Player Manager")
        
        windowImage.Apply(self)
        
        self.mainFrame.grid(row = 1, column = 0, columnspan = 20, rowspan= 20, pady = (5, 5), padx = (5, 5), sticky = "nsew")  
    
    def newNameEntry(self):
        self.tempPlayerName = ctk.CTkInputDialog(text = "Enter player name", title = "Player name entry").get_input()
        self.newPlayerNameLbl.configure(text = f"{self.tempPlayerName}")
    
    def incMoney(self):
        value = int(ctk.CTkInputDialog(text = "Add Money Amount", title = "Increasing Players Money").get_input())
        self.tempPlayerMoney += value
        
        self.newMoneyLbl.configure(text = f"{self.tempPlayerMoney}")
    
    def decMoney(self):
        value = int(ctk.CTkInputDialog(text = "Remove Money Amount", title = "Decreasing Players Money").get_input())
        self.tempPlayerMoney -= value
        
        self.newMoneyLbl.configure(text = f"{self.tempPlayerMoney}")
    
    def applyChanges(self):
        self.playerData.money = self.tempPlayerMoney
        self.playerData.name = self.tempPlayerName
        
        self.playerData.window.errorLbl.configure(text = "-Settings Applied")
        
        self.playerData.updateLabels()
        self.destroy()
    
    def main(self):        
        self.label = ctk.CTkLabel(self, text=f"Managing player: {self.playerData.name}", font = (self.font, 26, "bold"), text_color="#ff0000")
        self.label.grid(row = 0, column = 0, columnspan = 20, pady = 0, padx = 0, sticky = "ew")
        
        self.nameLbl = ctk.CTkLabel(master = self.mainFrame, text= "NAME", font = (self.font, 24, "bold"))
        self.moneyLbl = ctk.CTkLabel(master = self.mainFrame, text= "MONEY", font = (self.font, 24, "bold"))
        self.nameLbl.grid( row = 0, column = 0,  columnspan = 10, pady = (5, 5), padx = (5, 5), sticky = "ew")
        self.moneyLbl.grid(row = 0, column = 10, columnspan = 10, pady = (5, 5), padx = (5, 5), sticky = "ew")
        
        self.newPlayerNameLbl = ctk.CTkLabel(master = self.mainFrame, text=f"{self.tempPlayerName}", font = (self.font, 18))
        self.newNameButton = ctk.CTkButton(master = self.mainFrame, text = "Edit", font = (self.font, 18), command = self.newNameEntry)
        self.newPlayerNameLbl.grid(row = 2, column = 0, columnspan = 10, pady = (5, 5), padx = (5, 5), sticky = "ew")
        self.newNameButton.grid(row = 3, column = 0, columnspan = 10, pady = (5, 5), padx = (5, 5), sticky = "ew")
        
        self.newMoneyLbl = ctk.CTkLabel(master = self.mainFrame, text=f"{self.tempPlayerMoney}", font = (self.font, 18))
        self.addMoneyButton = ctk.CTkButton(master = self.mainFrame, text = "+", font = (self.font, 18), command = self.incMoney)
        self.remMoneyButton = ctk.CTkButton(master = self.mainFrame, text = "-", font = (self.font, 18), command = self.decMoney)
        self.newMoneyLbl.grid(row = 2, column = 10, columnspan = 10, pady = (5, 5), padx = (5, 5), sticky = "ew")
        self.addMoneyButton.grid(row = 3, column = 10, columnspan = 10, pady = (5, 5), padx = (5, 5), sticky = "ew")
        self.remMoneyButton.grid(row = 4, column = 10, columnspan = 10, pady = (5, 5), padx = (5, 5), sticky = "ew")
        
        
        
        self.applyButton = ctk.CTkButton(master = self.mainFrame, text = "APPLY", font = (self.font, 20, "bold"), fg_color = "#22FF22", text_color = "#222222", hover_color = "#1f881f", command = self.applyChanges)
        self.applyButton.grid(row = 20, column = 0, columnspan = 20, pady = (5, 5), padx = 0)
        
        self.bind("<Return>", lambda _:self.applyChanges())
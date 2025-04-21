import customtkinter as ctk
import playerManage
import deletePlayerConfirmation
from playerTransactionWindow import ExchangeManager


class Player:
    def __init__(self, window, name = "player", shots = 0, totalShots = 0, money = 1500):
        self.number = len(window.players)
        self.name = name
        self.shots = shots
        self.totalShots = totalShots
        self.money = money
        
        self.font = window.font
        self.window = window
        self.interface()
        
    def interface(self):
        self.namelbl = ctk.CTkLabel(master=self.window.mainFrame, text = f"{self.name}: ", font = (self.font, 18, "bold"))
        self.shotslbl = ctk.CTkLabel(master=self.window.mainFrame, text = f"[{self.totalShots}] {self.shots}", font = (self.font, 18, "bold"))
        self.moneylbl = ctk.CTkLabel(master=self.window.mainFrame, text = f"{self.money}", font = (self.font, 18, "bold"))
        
        self.namelbl.grid(row = self.number, column = 0,  columnspan = 5, pady = 0, padx = (0, 5), sticky = "ew")
        self.shotslbl.grid(row = self.number, column = 5,  columnspan = 5, pady = 0, padx = (0, 5), sticky = "ew")
        self.moneylbl.grid(row = self.number, column = 10,  columnspan = 5, pady = 0, padx = (0, 5), sticky = "ew")
        
        self.addShotButton = ctk.CTkButton(master = self.window.mainFrame, text="+", width=35, font = (self.font, 20), command=self.addShot)
        self.remShotButton = ctk.CTkButton(master = self.window.mainFrame, text="-", width=35, font = (self.font, 20), command=self.remShot)
        self.resetShotsButton = ctk.CTkButton(master = self.window.mainFrame, text="↺", width=35, font = (self.font, 20), command=self.resetShots)
        self.managePlayerButton = ctk.CTkButton(master = self.window.mainFrame, text="⚙", width=35, font = (self.font, 20), fg_color="#fc6f03", hover_color="#ca4c01",  command=self.managePlayer)
        self.remPlayer = ctk.CTkButton(master = self.window.mainFrame, text="✕", width=35, font = (self.font, 20), fg_color = "#C21212", text_color = "#121212", hover_color = "#8C1212", command=self.delPlayerConfirm)
        
        self.addShotButton.grid(row = self.number, column = 15,  columnspan = 1, sticky = "ew", pady = 0, padx = (0, 5))
        self.remShotButton.grid(row = self.number, column = 16,  columnspan = 1, sticky = "ew", pady = 0, padx = (0, 5))
        self.resetShotsButton.grid(row = self.number, column = 17,  columnspan = 1, sticky = "ew", pady = 0, padx = (0, 5))
        self.managePlayerButton.grid(row = self.number, column = 18,  columnspan = 1, sticky = "ew", pady = 0, padx = (0, 5))
        self.remPlayer.grid(row = self.number, column = 19,  columnspan = 1, sticky = "ew", pady = 0, padx = (0, 5))
        
    def updateLabels(self):
        self.namelbl.configure(text = f"{self.name}: ")
        self.shotslbl.configure(text = f"[{self.totalShots}] {self.shots}")
        self.moneylbl.configure(text = f"{self.money}")
        # print("-1-")
        self.window.after(1000, lambda : self.window.saveProgress(auto=True))
        
    def addShot(self):
        if self.shots != 3:
            self.shots+=1
            self.totalShots+=1
            self.shotslbl.configure(text = f"[{self.totalShots}] {self.shots}")
            # print("-2-")
            self.window.after(1000, lambda : self.window.saveProgress(auto=True))
        else:
            self.window.errorLbl.configure(text = "-Maximum shots reached")
            
    def remShot(self):
        if (self.shots > 0 and self.shots < 3):
            self.shots-=1
            self.shotslbl.configure(text = f"[{self.totalShots}] {self.shots}")
            # print("-3-")
            self.window.after(1000, lambda : self.window.saveProgress(auto=True))
        else:
            if self.shots == 0: 
                self.window.errorLbl.configure(text = "-Minimum shots reached") 
            else:
                self.window.errorLbl.configure(text = "-Shots locked please reset when allowed")
                

    def resetShots(self):
        self.shots = 0
        
        self.shotslbl.configure(text = f"[{self.totalShots}] {self.shots}")
        self.window.errorLbl.configure(text = "-Shot counter reset")
        # print("-4-")
        self.window.after(1000, lambda : self.window.saveProgress(auto=True))
        self.passGoTransaction()
        
        
    def passGoTransaction(self):
        self.window.players[0].decrMoney(200)
        self.window.players[self.number].incrMoney(200)
        self.updateLabels()
        self.window.after(10000, lambda : self.window.saveProgress(auto=1))
    
    def __str__(self):
        self.updateRow()
        return f"- Name: {self.name}, Shots: {self.shots}, Money: {self.money}"
    
    def managePlayer(self):
        playerManage.Manage(self)
    
    def updateRow(self):
        self.namelbl.grid(row = self.number)
        self.shotslbl.grid(row = self.number)
        self.moneylbl.grid(row = self.number)
        self.addShotButton.grid(row = self.number)
        self.remShotButton.grid(row = self.number)
        self.resetShotsButton.grid(row = self.number)
        self.managePlayerButton.grid(row = self.number)
        self.remPlayer.grid(row = self.number)
    
    
    def delPlayerConfirm(self):
        deletePlayerConfirmation.DelelePlayerConfirm(self)

    def delPlayer(self, auto = False):
        self.namelbl.destroy()
        self.shotslbl.destroy()
        self.moneylbl.destroy()
        self.addShotButton.destroy()
        self.remShotButton.destroy()
        self.resetShotsButton.destroy()
        self.managePlayerButton.destroy()
        self.remPlayer.destroy()
        self.window.remPlayer(self.number, auto)
    
    def incrMoney(self, newMoney):
        self.money += newMoney
        
    def decrMoney(self, newMoney):
        self.money -= newMoney
    
    def getMoney(self):
        return self.money
        

class Bank():
    def __init__(self):
        self.number = 0
        self.money = 15140
        self.name = "Bank"
    
    def updateLabels(self):
        print("No Labels to update")

    def __str__(self):
        return f"- Name: {self.name}, Money: {self.money}"
    
    def incrMoney(self, newMoney):
        self.money += newMoney
        
    def decrMoney(self, newMoney):
        self.money -= newMoney
    
    def getMoney(self):
        return self.money
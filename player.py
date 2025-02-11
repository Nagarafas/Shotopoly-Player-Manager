import customtkinter as ctk
import playerManage
import deletePlayerConfirmation

class Player:
    def __init__(self, window, name = "player", shots = 0, money = 1500):        
        self.number = len(window.players)+1
        self.name = name
        self.shots = shots
        self.money = money
        
        self.font = window.font
        self.window = window
        self.interface()
        
    def interface(self):
        self.namelbl = ctk.CTkLabel(master=self.window.mainFrame, text = f"{self.name}: ", font = (self.font, 18, "bold"))
        self.shotslbl = ctk.CTkLabel(master=self.window.mainFrame, text = f"{self.shots}", font = (self.font, 18, "bold"))
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
        self.shotslbl.configure(text = f"{self.shots}")
        self.moneylbl.configure(text = f"{self.money}")
        # print("-1-")
        self.window.after(1000, lambda : self.window.saveProgress(auto=True))
        
    def addShot(self):
        if self.shots != 3:
            self.shots+=1
            self.shotslbl.configure(text = f"{self.shots}")
            # print("-2-")
            self.window.after(1000, lambda : self.window.saveProgress(auto=True))
        else:
            self.window.errorLbl.configure(text = "-Maximum shots reached")
            
    def remShot(self):
        if (self.shots > 0 and self.shots < 3):
            self.shots-=1
            self.shotslbl.configure(text = f"{self.shots}")
            # print("-3-")
            self.window.after(1000, lambda : self.window.saveProgress(auto=True))
        else:
            if self.shots == 0: 
                self.window.errorLbl.configure(text = "-Minimum shots reached") 
            else:
                self.window.errorLbl.configure(text = "-Shots locked please reset when allowed")
                

    def resetShots(self):
        self.shots = 0
        self.shotslbl.configure(text = f"{self.shots}")
        self.window.errorLbl.configure(text = "-Shot counter reset")
        # print("-4-")
        self.window.after(1000, lambda : self.window.saveProgress(auto=True))
        
    
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
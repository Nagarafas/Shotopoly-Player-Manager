from tkinter import filedialog as fd
import customtkinter as ctk
import platform
if platform.system() == "Windows": import Bitmap_Image_Create as windowImage
else: import Image_Create as windowImage
import player as pl
import playerTransactionWindow
import json

class Application(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.gridSize = 20
        self.font = "Roboto_Condensed"
        self.isDark = bool(ctk.AppearanceModeTracker.detect_appearance_mode())
        
        self.players = []
        self.saveName = "defaultautosave"
        
        self.mainFrame = ctk.CTkFrame(self)
        
        self.windowInit()
        self.gridInit()
        self.main()
        
    def gridInit(self):
        for i in range(self.gridSize):
            self.grid_rowconfigure(i, weight = 1)
            self.grid_columnconfigure(i, weight = 1)
            
            self.mainFrame.grid_rowconfigure(i, weight = 1)
            self.mainFrame.grid_columnconfigure(i, weight = 1)
    
    def windowInit(self):
        ctk.set_appearance_mode("system")
        
        ctk.set_default_color_theme("dark-blue")
        self.geometry("600x350")
        self.resizable(True, True)
        self.title("Shotopoly Player Manager")
        ctk.CTkFont(family='Roboto_Condensed', size=18)
        
        windowImage.Apply(self)
        
        self.mainFrame.grid(row = 1, column = 0, columnspan = 21, rowspan= 19, pady = (5, 5), padx = (5, 5), sticky = "nsew")   
        
    def changeTheme(self):
        if self.isDark:
            self.themeButton.configure(text = "🌙", font = (self.font, 16))
            ctk.set_appearance_mode("light")
            self.isDark = False
        else:
            self.themeButton.configure(text = "🔆", font = (self.font, 16))
            ctk.set_appearance_mode("Dark")
            self.isDark = True
    
    def addPlayer(self):
        name = str(ctk.CTkInputDialog(text = "Enter player name", title = "Player name entry").get_input())
        if name == "":
            name = f"player {len(self.players)+1}"
        elif name == "None":
            return    
        self.players.append(pl.Player(self, name)) 
        self.errorLbl.configure(text = f"-Added player '{name}'")
        self.after(1000, lambda : self.saveProgress(auto=True))
        
        print("---------------------------\nplayers: ")
        for player in self.players:
            print("    ", player)
        print("---------------------------")
        
        self.addPlayerButton.grid(row = len(self.players)+1)
        self.exchageButton.grid(row = len(self.players)+1)
    
    def remPlayer(self, pNumber, auto = False):
        pname = self.players[pNumber-1].name
        del self.players[pNumber-1]
        self.updatePlayerNumber()
        self.errorLbl.configure(text = f"-Removed player '{pname}'")
        if not auto:
            self.after(1000, lambda : self.saveProgress(auto=True))
        
        print("---------------------------\nplayers: ")
        for player in self.players:
            print("    ", player)
        print("---------------------------")
        
        self.addPlayerButton.grid(row = len(self.players)+1)
        self.exchageButton.grid(row = len(self.players)+1)
    
    def playerExchange(self):
        playerTransactionWindow.ExhangeManager(self)
     
    def updatePlayerNumber(self):
        for x, player in enumerate(self.players):
            player.number = x+1

#Saves
    def saveProgress(self, auto = False):
        if not(auto):   
            fileName = str(ctk.CTkInputDialog(text = "Enter Save name", title = "Save Name Entry").get_input())
            if fileName == "None":
                return
        else:
            fileName = f"{self.saveName}"
            if not("autosave" in fileName):
                fileName+="(autosave)"
        
        playerDicts = []
        for player in self.players:
            playerDicts.append({"number": player.number, "name": player.name, "shots": player.shots, "money": player.money})
        jsonString = json.dumps(playerDicts)    
        with open(f"{fileName}.json", "w") as fw:
            fw.write(jsonString)
        
        self.saveName = fileName
        if auto:
            self.errorLbl.configure(f"-Autoaved game: {fileName}.json")
            print("Progress Autosaved")
        else:
            self.errorLbl.configure(f"-Saved game: {fileName}.json")
            print("Progress Saved")
            
    def loadProgress(self):
        fileName = str(ctk.CTkInputDialog(text = "Enter Save name", title = "Save Name Entry").get_input())
        if (fileName != "") and not(fileName == "None"):
            self.saveName = fileName
            try:
                for player in self.players:
                    player.delPlayer(auto = True)
                for player in self.players:
                    player.delPlayer(auto = True)
                for player in self.players:
                    player.delPlayer(auto = True)
            except:
                print("no players detected")
                
                
            with open(f"{fileName}.json", "r") as fr:
                pDictsString = fr.read()
            playerDicts = json.loads(pDictsString)
            
            for pDat in playerDicts:
                self.players.append(pl.Player(self, pDat["name"], pDat["shots"], pDat["money"]))
            
            self.addPlayerButton.grid(row = len(self.players)+1)
            self.exchageButton.grid(row = len(self.players)+1)
            self.errorLbl.configure(f"-Loaded savefile: {fileName}")
            
            self.saveName = fileName
            
    
    def main(self):        
        self.themeButton = ctk.CTkButton(master = self, width=6, font = (self.font, 16), command=self.changeTheme)
        if self.isDark:
            self.themeButton.configure(text = "🔆")
        else: self.themeButton.configure(text = "🌙")
        
        self.themeButton.grid(row = 0, column = 0,  columnspan = 1, pady = 0, padx = (5, 0), sticky = "w")
        
        self.SaveButton = ctk.CTkButton(master = self, text="💾", font = (self.font, 16), width=36, command=self.saveProgress)
        self.SaveButton.grid(row = 0, column = 19, columnspan = 1, pady = 0, padx = (0, 5), sticky = "e")
        
        self.loadButton = ctk.CTkButton(master = self, text="📁", font = (self.font, 16), width=36, command=self.loadProgress)
        self.loadButton.grid(row = 0, column = 20, columnspan = 1, pady = 0, padx = (0, 5), sticky = "ew")
        
        self.errorLbl = ctk.CTkLabel(master = self, text = "", font = (self.font, 16, "bold"), text_color="#ff0000") 
        self.errorLbl.grid(row = 20, column = 0, columnspan = 20, pady = (0, 5), padx = (0,0))
        
        
        self.nameLbl = ctk.CTkLabel(master = self.mainFrame, text= "NAME", font = (self.font, 26, "bold"))
        self.shotsLbl = ctk.CTkLabel(master = self.mainFrame, text= "SHOTS", font = (self.font, 26, "bold"))
        self.moneyLbl = ctk.CTkLabel(master = self.mainFrame, text= "FUNDS", font = (self.font, 26, "bold"))
        
        self.nameLbl.grid( row = 0, column = 0,  columnspan = 5, pady = (5, 5), padx = (5, 5), sticky = "ew")
        self.shotsLbl.grid(row = 0, column = 5,  columnspan = 5, pady = (5, 5), padx = (5, 5), sticky = "ew")
        self.moneyLbl.grid(row = 0, column = 10, columnspan = 5, pady = (5, 5), padx = (5, 5), sticky = "ew")
        
        self.exchageButton = ctk.CTkButton(master = self.mainFrame, text="⇄", font = (self.font, 22), fg_color="#0011AA", hover_color="#00118F", command=self.playerExchange)
        self.exchageButton.grid(row = 1, column = 11, columnspan = 9, pady = (5, 5), padx = (5, 5), sticky = "ew")
        
        self.addPlayerButton = ctk.CTkButton(master = self.mainFrame, text="+", font = (self.font, 22), command=self.addPlayer)
        self.addPlayerButton.grid(row = 1, column = 0, columnspan = 11, pady = (5, 5), padx = (5, 0), sticky = "ew")
        

if __name__ == "__main__":
    app = Application()
    app.mainloop()
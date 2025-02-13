import customtkinter as ctk
import platform
if platform.system() == "Windows": import Bitmap_Image_Create as windowImage
else: import Image_Create as windowImage
import os
import json
import player as pl

class SelectDialog(ctk.CTkToplevel):
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root
        
        self.gridSize = root.gridSize
        self.font = root.font
        self.savesList = []
        
        self.mainFrame = ctk.CTkFrame(self)
        self.gridInit()
        self.windowInit()
        
        self.saveFileLookup()
        self.main()
        
    def gridInit(self):
        for i in range(self.gridSize):
            self.grid_rowconfigure(i, weight = 1)
            self.grid_columnconfigure(i, weight = 1)
            
            self.mainFrame.grid_rowconfigure(i, weight = 1)
            self.mainFrame.grid_columnconfigure(i, weight = 1)
    
    def windowInit(self):
        self.geometry("250x100")
        self.resizable(True, True)
        self.title("Save File Selector")
        
        windowImage.Apply(self)
        
        self.mainFrame.grid(row = 1, column = 0, columnspan = 20, rowspan= 20, pady = (5, 5), padx = (5, 5), sticky = "nsew") 
        
    def saveFileLookup(self):
        workingDir=os.getcwd()
        if platform.system() == "Windows":
            savesFolder=f"{workingDir}\\Saves"
        else:
            savesFolder=f"{workingDir}/Saves"
        
        files_in_folder=os.listdir(savesFolder)
        jsonFiles=[]
        for file in files_in_folder:
            if file.endswith(".json"):
                jsonFiles.append(file[:-5])
        self.savesList = jsonFiles
    
    def loadSave(self):
        # fileName = str(ctk.CTkInputDialog(text = "Enter Save name", title = "Save Name Entry").get_input())
        fileName = self.selectBox.get()
        if (fileName != "") and not(fileName == "None"):
            self.root.saveName = fileName
            try:
                for player in self.root.players:
                    if player.name != "Bank":
                        player.delPlayer(auto = True)
                        print("DONE1")
                for player in self.root.players:
                    if player.name != "Bank":
                        player.delPlayer(auto = True)
                        print("DONE2")
                for player in self.root.players:
                    if player.name != "Bank":
                        player.delPlayer(auto = True)
                        print("DONE2")
            except:
                print("no players detected")
                
                
            with open(f"Saves/{fileName}.json", "r") as fr:
                pDictsString = fr.read()
            playerDicts = json.loads(pDictsString)
            
            for pDat in playerDicts:
                self.root.players.append(pl.Player(self.root, pDat["name"], pDat["shots"], pDat["money"]))
                self.root.players[0].decrMoney(pDat["money"])
            
            self.root.addPlayerButton.grid(row = len(self.root.players))
            self.root.exchageButton.grid(row = len(self.root.players))
            self.root.errorLbl.configure(f"-Loaded savefile: {fileName}")
            
            self.root.saveName = fileName
    
    def main(self):
        self.selectBox = ctk.CTkOptionMenu(master= self.mainFrame, values = self.savesList,  fg_color="#9F1133", font = (self.font, 20))
        self.selectBox.grid(row = 5, column = 5, columnspan = 10, pady = (0, 0), padx = (5, 5), sticky = "ew")
        
        self.loadSaveButton = ctk.CTkButton(master= self.mainFrame, text = "Load", fg_color="#9F1133", font = (self.font, 20), command = self.loadSave)
        self.loadSaveButton.grid(row = 10, column = 5, columnspan = 10, pady = (0, 0), padx = (5, 5), sticky = "ew")
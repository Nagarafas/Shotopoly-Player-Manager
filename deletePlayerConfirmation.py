import customtkinter as ctk
import platform
if platform.system() == "Windows": import Bitmap_Image_Create as windowImage
else: import Image_Create as windowImage

class DelelePlayerConfirm(ctk.CTkToplevel):
    def __init__(self, player, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player = player
        self.gridSize = player.window.gridSize
        self.font = player.font
        
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
        self.geometry("350x150")
        self.resizable(True, True)
        self.title("Player Deletion Confirmation")
        
        windowImage.Apply(self)
        
        self.mainFrame.grid(row = 0, column = 0, columnspan = 20, rowspan= 20, pady = (5, 5), padx = (5, 5), sticky = "nsew")
    
    def confirm(self):
        self.player.delPlayer()
        self.destroy()

    def cancel(self):
        self.destroy()
    
    def main(self):
        self.confirmLbl = ctk.CTkLabel(master = self.mainFrame, text= f"Are you sure\nyou want to delete player:\n{self.player.name}", font = (self.font, 20, "bold"), text_color = "#A81212")
        self.confirmLbl.grid( row = 10, column = 0,  columnspan = 20, pady = (5, 5), padx = (5, 5), sticky = "nsew")

        self.yesButton =  ctk.CTkButton(master = self.mainFrame, text="yes", font = (self.font, 22), fg_color = "#22FF22", text_color = "#222222", hover_color = "#1f881f", command=self.confirm)
        self.noButton =  ctk.CTkButton(master = self.mainFrame, text="calcel", font = (self.font, 22), fg_color = "#ff2222", text_color = "#222222", hover_color = "#881f1f", command=self.cancel)
        
        self.yesButton.grid(row = 15, column = 0,  columnspan = 10, pady = (5, 5), padx = (5, 5), sticky = "nsew")
        self.noButton.grid(row = 15, column = 10,  columnspan = 10, pady = (5, 5), padx = (5, 5), sticky = "nsew")

import tkinter as tkinter
from tkinter import ttk

class SpecialTabFunctions:

    def extend_window(self):

        self.parent_root.geometry("800x400")
        self.parent_root.minsize(800, 400)
        self.parent_root.maxsize(800, 400)


    def create_and_layout_buttons(self):
        
        BUTTONS = dict()
        for text in range(11, 19):
            BUTTONS[f"{text}"] = ttk.Button(self.main_button_frame, text=f"{text}", command=lambda: print(text.title()))

        def layout_buttons():
            Position_Map = {
                0: [BUTTONS[f"{i}"] for i in range(11, 13)],
                1: [BUTTONS[f"{i}"] for i in range(13, 15)],
                2: [BUTTONS[f"{i}"] for i in range(15, 17)],
                3: [BUTTONS[f"{i}"] for i in range(17, 18)],
            }
            for i in range(4):
                for j, btn in enumerate(Position_Map[i], 5):
                    self.parent_root.configure(index=j, weight=1)
                    btn.grid(row=i, column=j, sticky="nsew")
    
    
    def main(self):
        self.extend_window()
        self.create_and_layout_buttons()
                
        

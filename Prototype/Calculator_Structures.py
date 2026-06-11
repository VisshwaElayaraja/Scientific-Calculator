
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from Classes_and_Functions import *
from Modules._customfunctions import *


# ===================================================================================================================== #


class RootStructure(tk.Tk, UIFunctions):
    
    def __init__(self, parent):
        
        super().__init__()
        self.parent = parent
        self.parent_root = self
  
        self.title("MyCalculator")
        
        self.initialize_base_geometry()
        
        self.create_structures()
        self.configure_structures()
        self.layout_structures()
        
        self.initialize_functions()
        
    
    def initialize_base_geometry(self):
        
        self.geometry("600x400")  # x:y ratio is 1.5.
        self.minsize(600, 400)    # 
        self.maxsize(600, 400)    # 
        
        self.columnconfigure(0, weight=1)  # 
        self.rowconfigure(0, weight=1)     # 
        self.columnconfigure(1, weight=1)  # 
        self.rowconfigure(1, weight=1)     # for setting correct size for the display(entry) widget and main button frame.

    def create_structures(self):
        
        # Basic frames;
        self.display_screen = ctk.CTkTextbox(self)
        self.main_button_frame = MainButtonFrame(self)
        self.top_button_frame = TopButtonFrame(self)
        
        # Advanced frames;
        self.sin_cos_advanced_frame = self.top_button_frame.SinCosAdvancedFrame(self)
        self.main_advanced_frame = self.top_button_frame.MainAdvancedFrame(self)
        
    def configure_structures(self):
        
        self.display_screen.configure(width=350, height=125, font=("Arial", 28), corner_radius=5, fg_color="black")
        
    def layout_structures(self):
        
        self.display_screen.place(x=6, y=5)
        self.main_button_frame.place(x=5, y=135, width=590, height=260)
        self.top_button_frame.place(x=359, y=5, width=235, height=125)
    
    def initialize_functions(self):
        
        self.bind_all("<Button-1>", self.Focus_On_Display_Screen)
        
        self.display_screen.bind("<Key>", self.restrict_keys_for_window)
        self.display_screen.bind("<Return>", self.Calculate_Expression)
        self.display_screen.bind("<BackSpace>", self.Delete_Text_In_Display)




class MainButtonFrame(tk.Frame, UIFunctions):
    
    def __init__(self, parent_root):
        
        self.parent_root = parent_root  # parent class is the root.
        super().__init__(parent_root)
        
        self.initialize_buttons()
        self.layout_buttons_and_config_weights()
        

    def initialize_buttons(self):
        
        self.MAIN_BUTTONS = dict()
        Buttons_List = list(range(10)) + ['+', '_', 'x', '/', '(', ')', '^', '%', "."]
        
        for text in Buttons_List:
            self.MAIN_BUTTONS[f"{text}"] = DisplayButton(self, text=f"{text}")

        self.MAIN_BUTTONS['#'] = ttk.Button(self, text="ESC", command=lambda:exit())
        
    def layout_buttons_and_config_weights(self):
        
        Position_Map = {
            0:(self.MAIN_BUTTONS['1'], self.MAIN_BUTTONS['2'], self.MAIN_BUTTONS['3'],  self.MAIN_BUTTONS['('], self.MAIN_BUTTONS[')']), 
            1:(self.MAIN_BUTTONS['4'], self.MAIN_BUTTONS['5'], self.MAIN_BUTTONS['6'],  self.MAIN_BUTTONS['+'], self.MAIN_BUTTONS['_']),
            2:(self.MAIN_BUTTONS['7'], self.MAIN_BUTTONS['8'], self.MAIN_BUTTONS['9'],  self.MAIN_BUTTONS['x'], self.MAIN_BUTTONS['/']),
            3:(self.MAIN_BUTTONS['#'], self.MAIN_BUTTONS['0'], self.MAIN_BUTTONS['.'],  self.MAIN_BUTTONS['^'], self.MAIN_BUTTONS['%']),
        }
        for i in range(4):
            self.rowconfigure(index=i, weight=1)
            for j, btn in enumerate(Position_Map[i], 0):
                self.columnconfigure(index=j, weight=1)
                btn.grid(row=i, column=j, sticky="nsew")
        



class TopButtonFrame(tk.Frame, UIFunctions, ModeSwitchFunctions):

    def __init__(self, parent_root):
        
        self.parent_root = parent_root  # parent class is the root.
        super().__init__(parent_root)
        
        self.initialize_buttons()
        self.layout_buttons_and_config_weights()
        
        
    def initialize_buttons(self):
        
        self.TOP_BUTTONS = dict()
        Buttons_List = [('enter', '=', self.Calculate_Expression), ('delete', 'DELETE', self.Delete_Text_In_Display),
                        ('clear', 'CLEAR',self.Clear_Display), ('mode', '   MODE\n'+'(advance)', self.Run_ModeSwitch_Main)]

        for (name, text, func) in Buttons_List:
            self.TOP_BUTTONS[f"{name}"] = ttk.Button(self, text=f"{text}", command=func)
                    
    def layout_buttons_and_config_weights(self):
        
        Position_Map = {
            0: (self.TOP_BUTTONS['enter'],  self.TOP_BUTTONS['mode']),
            1: (self.TOP_BUTTONS['delete'], self.TOP_BUTTONS['clear']),
        }
        
        for i in range(2):
            self.rowconfigure(i, weight=1)
            for j, btn in enumerate(Position_Map[i], 0):
                self.columnconfigure(j, weight=1)
                btn.grid(row=i, column=j, sticky="nsew")


    # Creating frame sub_classes buttons in advanced section;
    
    class MainAdvancedFrame(tk.Frame):
        
        def __init__(self, parent_root):
            self.parent_root = parent_root  # parent class is the root.
            super().__init__(parent_root)
            self.create_buttons()
            self.layout_buttons()
            
        def create_buttons(self):
            self.ADV_BUTTONS = dict()
            self.Buttons_List = ['√', 'Tan', "Log", 'Ln', 'e', '#', 'π', '*']
            for text in self.Buttons_List:
                self.ADV_BUTTONS[f"{text}"] = DisplayButton(self, text=f"{text}")
        
        def layout_buttons(self):
            Position_Map = {
                0: [self.ADV_BUTTONS[f"{text}"] for text in self.Buttons_List[0:2]],
                1: [self.ADV_BUTTONS[f"{text}"] for text in self.Buttons_List[2:4]],
                2: [self.ADV_BUTTONS[f"{text}"] for text in self.Buttons_List[4:6]],
                3: [self.ADV_BUTTONS[f"{text}"] for text in self.Buttons_List[6:8]],
            }
            for i in range(4):
                self.rowconfigure(index=i, weight=1)
                for j, btn in enumerate(Position_Map[i], 0):
                    self.columnconfigure(index=j, weight=1)
                    btn.grid(row=i, column=j, sticky="nsew")
    
    
    class SinCosAdvancedFrame(tk.Frame):
        
        def __init__(self, parent_root):
            self.parent_root = parent_root  # parent class is the root.
            super().__init__(parent_root)
            self.create_buttons()
            self.layout_buttons()
            
        def create_buttons(self):
            self.ADV_BUTTONS = dict()
            self.Buttons_List = ['Sin', 'Cos']
            for text in self.Buttons_List:
                self.ADV_BUTTONS[f"{text}"] = DisplayButton(self, text=f"{text}")
        
        def layout_buttons(self):
            Position_Map = {
                0: [self.ADV_BUTTONS[self.Buttons_List[0]]],
                1: [self.ADV_BUTTONS[self.Buttons_List[1]]]
            }
            for i in range(2):
                self.rowconfigure(index=i, weight=1)
                for j, btn in enumerate(Position_Map[i], 0):
                    self.columnconfigure(index=j, weight=1)
                    btn.grid(row=i, column=j, sticky="nsew") 



    
# ===================================================================================================================== #

import math
import tkinter as tk
from tkinter import ttk

def main():
    calc_app = CalculatorApp()
    calc_app.mainloop()


# =====================================================================================================================


class CalculatorApp(tk.Tk):
    
    def __init__(self, FuncObj=None):
        
        super().__init__()
        self.title("MyCalculator")
        
        self.geometry("600x400")  # 
        self.minsize(600, 400)    # x:y ratio is 1.5
        self.maxsize(600, 400)    # 

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=2)
        
        self.display_screen = tk.Text(self, height=1, width=29,font=("Arial", 20), bg="white")
        self.display_screen.grid(row=0, column=0, columnspan=5, sticky="nsw", padx=3, pady=2)
        
        self.display_screen.bind("<Key>", self.restrict_keys_for_display)
        self.display_screen.bind("<Return>", self.calculate_expression)
        self.display_screen.bind("<BackSpace>", self.delete_text_in_display)

        num_button_frame = NumberButtonFrame(self)
        num_button_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=4, pady=2)
        
        side_button_frame = SideButtonFrame(self)
        side_button_frame.grid(row=0, column=2, rowspan=2 ,sticky="nsew", padx=2, pady=2)
    
    
    def restrict_keys_for_display(self, event):
        
        if event.keysym in ["Return", "BackSpace"]:  # keys mentioned in the list alone will work.
            return None
        return "break"  # prevents default behavior of the key pressed.
    
    
    def delete_text_in_display(self, event=None):
        
        current_cursor_pos = self.display_screen.index(tk.INSERT)
        self.display_screen.delete(f"{current_cursor_pos} - 1c", current_cursor_pos)  # deletes one char. to the left of cursor.
        return "break"  
      
               
    def clear_display(self, event=None):
        
        self.display_screen.delete("1.0", tk.END)
        return "break"


    def calculate_expression(self, event=None):  # //TODO
        
        pass
    
        return "break"
  


class NumberButtonFrame(ttk.Frame):
    
    def __init__(self, parent_root):
        
        self.parent_root = parent_root
        super().__init__(parent_root, height=20, width=20)

        # Numbers and brackets
        num_1_BTN, num_2_BTN, num_3_BTN = DisplayButton(self, text="1"), DisplayButton(self, text="2"), DisplayButton(self, text="3")
        num_4_BTN, num_5_BTN, num_6_BTN = DisplayButton(self, text="4"), DisplayButton(self, text="5"), DisplayButton(self, text="6")
        num_7_BTN, num_8_BTN, num_9_BTN = DisplayButton(self, text="7"), DisplayButton(self, text="8"), DisplayButton(self, text="9")
        num_0_BTN, openbrac_BTN,closebrac_BTN = DisplayButton(self, text="0"), DisplayButton(self, text="("), DisplayButton(self, text=")")

        Positioning_List = [num_1_BTN, num_2_BTN, num_3_BTN,
                            num_7_BTN, num_8_BTN, num_9_BTN,
                            num_4_BTN, num_5_BTN, num_6_BTN,
                            openbrac_BTN,num_0_BTN,closebrac_BTN,]
        
        btn_index = 0
        for i in range(4):
            for j in range(3):
                self.rowconfigure(index=i, weight=1)
                self.columnconfigure(index=j, weight=1)
                Positioning_List[btn_index].grid(row=i, column=j, sticky="nsew")
                btn_index += 1
        del Positioning_List



class SideButtonFrame(tk.Frame):
    
    def __init__(self, parent_root):
        
        self.parent_root = parent_root
        super().__init__(parent_root)
        
        # Symbols
        addition_BTN, subtract_BTN = DisplayButton(self, text="+"), DisplayButton(self, text="_")
        multiply_BTN, division_BTN = DisplayButton(self, text="x"), DisplayButton(self, text="/")
        
        # Functions
        enter_BTN  = ttk.Button(self, text="ENTER", command=self.parent_root.calculate_expression)
        delete_BTN  = ttk.Button(self, text="DEL", command=self.parent_root.delete_text_in_display)
        clear_BTN  = ttk.Button(self, text="CLR", command=self.parent_root.clear_display)
        blank_BTN = ttk.Button(self, text="~", command=lambda:print("U pressed the empty button lol"))
        
        Positioning_List = [addition_BTN, enter_BTN,
                            subtract_BTN, delete_BTN,
                            multiply_BTN, clear_BTN,
                            division_BTN, blank_BTN]
        
        btn_index = 0
        for i in range(2, 6):
            for j in range(2):
                self.rowconfigure(index=i, weight=1)
                self.columnconfigure(index=j, weight=1)
                Positioning_List[btn_index].grid(row=i, column=j, sticky="nsew")
                btn_index += 1
        del Positioning_List
        
        advanced_tab_BTN = ttk.Button(self, text="Tab", command=lambda:print("U pressed the tab button lol"))
        advanced_tab_BTN.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")
        self.rowconfigure(0, weight=2)
        self.columnconfigure(0, weight=2)



class DisplayButton(ttk.Button):
    
    def __init__(self, parent, text):
        
        self.parent = parent  # parent class is frame.
        super().__init__(parent, text=text, command=self.add_to_display)
    
    
    def add_to_display(self):
        
        item = self.cget("text")
        if item == "_": item = "-"  # using _ instead of - for button text for visibility.
            
        current_cursor_pos = self.parent.parent_root.display_screen.index(tk.INSERT)
        self.parent.parent_root.display_screen.insert(current_cursor_pos, item)


# =====================================================================================================================


if __name__ == "__main__":
    main()

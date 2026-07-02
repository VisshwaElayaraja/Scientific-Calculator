# MODULES :

import math, os
import tkinter as tk
import customtkinter as ctk # type: ignore
from tkinter import ttk


# ===================================================================================================================== # 
# ===================================================================================================================== # 


# CLASSES AND FUNCTIONS :


 # Functional Classes:-

class UIFunctions:
    
    def __init__(self):
        
        pass
    
    def Focus_On_Display_Screen(self, event=None):
        
        self.parent_root.display_screen.focus_set()

    def restrict_keys_for_window(self, event=None):
        
        unrestricted_keys = {'Return', 'BackSpace', 'Left', 'Right'}
        if event.keysym in unrestricted_keys:  # keys mentioned in the list alone will work.
            return None
        return "break"  # prevents default behavior of the key pressed.
    
    def Delete_Text_In_Display(self, event=None):
        
        current_cursor_pos = self.parent_root.display_screen.index(tk.INSERT)
        self.parent_root.display_screen.delete(f"{current_cursor_pos} - 1c", current_cursor_pos)  # deletes one char. to the left of cursor.
        return "break"  

    def Clear_Display(self, event=None):
        
        self.parent_root.display_screen.delete("1.0", tk.END)
        return "break"
    
    def Calculate_Expression(self, event=None):
        
        def _acquire_and_clear_text_from_screen():
                    
            text = self.parent_root.display_screen.get('1.0', tk.END)
            self.string = text.strip()  # initializing in class for permitting broader usage.
            string = text.strip()
            
            self.Clear_Display()  # removing the text from screen to display result after calculation.
            
            script_dir = os.path.dirname(os.path.abspath(__file__))
            history_file_path = os.path.join(script_dir, "History.txt")
            with open(history_file_path, "a", encoding="utf-8") as file:
                file.write(string)
                file.write("\n")
        
        def _alter_text_string():
            
            replace_map = {" ":"",
                           "x":"*",
                           "^":"**",
                           "π":str(math.pi),
                           "e":"("+str(math.e)+")",
                           "√":"math.sqrt",
                           "Log":"math.log10",
                           "Ln" :"math.log",
                           "Sin":"math.sin",
                           "Cos":"math.cos",
                           "Tan":"math.tan"}
            
            for replacing_item, replacement_item in replace_map.items():
                self.string = self.string.replace(replacing_item, replacement_item)
            
            self.string_list = list(self.string)         # working with list for its mutability.

        def _correct_minor_errors():
            
            def repeat(func, reps:int) -> None: # Helper Function
                if reps == 0: return
                func()
                repeat(func, reps-1)
                
            # Removing of empty parenthesis.
            while True:
                index_of_empty_bracs = "".join(self.string_list).find("()")
                if index_of_empty_bracs != -1:
                    repeat(lambda: self.string_list.pop(index_of_empty_bracs), 2)
                    continue
                break
            
            while "(" in self.string_list:
                
                ## removing unnecessary parenthesis:
                while self.string_list[-1] == "(":
                    self.string_list.pop()
                
                no_of_cls_bracs, no_of_open_bracs = self.string_list.count(")"), self.string_list.count("(")
                if no_of_cls_bracs == no_of_open_bracs: break
                
                while (no_of_cls_bracs > no_of_open_bracs) and (self.string_list[-1] == ")"):
                    self.string_list.pop()
                    no_of_cls_bracs -= 1
                            
                ## auto-filling close brackets (if its missed out):
                if no_of_open_bracs > no_of_cls_bracs:
                    no_of_bracs_to_append = no_of_open_bracs - no_of_cls_bracs
                    repeat(lambda: self.string_list.append(")"), no_of_bracs_to_append)

        def _calculate_result():
            
            try:
                if "Error!" in self.string_list:
                    raise Exception
                if not self.string_list:
                    self.result = ""
                else:
                    self.string = "".join(self.string_list)
                    self.result = str(float(eval(self.string)))
            except Exception as EXC:
                self.result = "Error!"

        def _display_result_in_screen():
            
            current_cursor_position = self.parent_root.display_screen.index(tk.INSERT)
            self.parent_root.display_screen.insert(current_cursor_position, self.result)

        def main_run():
            
            _acquire_and_clear_text_from_screen()
            _alter_text_string()
            _correct_minor_errors()
            _calculate_result()
            _display_result_in_screen()
            
            return self.result
        
        main_run()
    
    def Show_Previous_Entry(self, event=None):
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        history_file_path = os.path.join(script_dir, "History.txt")
        
        with open(history_file_path, "r", encoding="utf-8") as file:
            entries = file.readlines()
            if len(entries) == 0: entry = ""
            else: entry = entries[-1]
            
            self.Clear_Display()
            current_cursor_position = self.parent_root.display_screen.index(tk.INSERT)
            self.parent_root.display_screen.insert(current_cursor_position, entry)
            
            with open(history_file_path, "w", encoding="utf-8") as file:
                file.writelines(entries[0:-1])


class ModeSwitchFunctions():
    
    Tab_Is_Open = False
    
    def _advance(self):
        
        def __layout_frames():
            
            self.parent_root.sin_cos_advanced_frame.place(x=682, y=3, width=116, height=132)
            self.parent_root.main_advanced_frame.place(x=566, y=135, width=232, height=260)
        
        def __extend_and_adjust_window():
            
            self.TOP_BUTTONS['mode'].config(text='SHIFT\n'+'(Basic)')
            
            self.parent_root.display_screen.configure(width=445)
            self.parent_root.main_button_frame.place(width=561)
            self.parent_root.top_button_frame.place(x=455, y=4,width=223, height=127)
            
            self.parent_root.geometry("800x400") # x:y ratio is 2.
            self.parent_root.minsize(800, 400)   # 
            self.parent_root.maxsize(800, 400)   # 
        
        def run_advance():
            
            __extend_and_adjust_window()
            __layout_frames()
            ModeSwitchFunctions.Tab_Is_Open = True
        
        run_advance() 
    
    def _revert(self):
        
        def __remove_frames():
            
            self.parent_root.sin_cos_advanced_frame.place_forget()
            self.parent_root.main_advanced_frame.place_forget()

        def __regularize_window():
            
            self.TOP_BUTTONS['mode'].config(text='    SHIFT\n'+'(Scientific)')

            self.parent_root.configure_structures()
            self.parent_root.layout_structures()
            
            self.parent_root.initialize_base_geometry()

        def run_revert():
            
            __regularize_window()
            __remove_frames()
            ModeSwitchFunctions.Tab_Is_Open = False
        
        run_revert()
     
    def Run_ModeSwitch_Main(self):
        
        if ModeSwitchFunctions.Tab_Is_Open:
            self._revert()
        else:
            self._advance()


 # Structural Classes:-

set_of_sci_functions = {'Sin', 'Cos', '√', 'Tan', "Log", 'Ln'}

class DisplayButton(ttk.Button):
    
    def __init__(self, parent_frame, text):
        
        self.parent_frame = parent_frame  # parent class is the frame.
        if text in {'+', '_', 'x', '/', "(", ")"}:           self.style_name = "basic.TButton"
        elif text in {'√', '^', 'Log', 'π', 'Ln', 'e',
                      '%', 'Sin', 'Cos', 'Tan'}:             self.style_name = "advance.TButton"
        else:                                                self.style_name = "TButton"
        super().__init__(parent_frame, text=text, command=self.add_to_display, style=self.style_name)
        
    def add_to_display(self):
        
        item = self.cget("text")
        if item == "_":
            item = "-"  # using _ instead of - in button text alone (for visibility.)
        elif item in set_of_sci_functions:
            item = item + "()"
        
        current_cursor_position = self.parent_frame.parent_root.display_screen.index(tk.INSERT)
        self.parent_frame.parent_root.display_screen.insert(current_cursor_position, item)
        if item in set(map(lambda text: text + "()", set_of_sci_functions)):
            current_cursor_position = self.parent_frame.parent_root.display_screen.index(tk.INSERT)
            self.parent_frame.parent_root.display_screen.mark_set("insert", f"{current_cursor_position}-1c")


class CursorButton(ttk.Button):
    
    def __init__(self, parent_frame, text):
        
        self.parent_frame = parent_frame  # parent class is the frame.
        super().__init__(parent_frame, text=text, command=self.move_cursor)
        self.direction = text
        
    def move_cursor(self, event=None):
        
        display = self.parent_frame.parent_root.display_screen
        current_index = display.index(tk.INSERT)
        if self.direction.lower() == "🡠": display.mark_set("insert", f"{current_index}-1c")
        elif self.direction.lower() == "🡢": display.mark_set("insert", f"{current_index}+1c")
        return "break" # Prevent default key behavior




# ===================================================================================================================== # 
# ===================================================================================================================== # 




# CALCULATOR STRUCTURE :

 # Root Structure:-

class RootStructure(tk.Tk, UIFunctions, ModeSwitchFunctions):
    
    def __init__(self, parent):
        
        super().__init__()
        self.parent = parent
        self.parent_root = self
  
        self.title("Basic & Scientific Calculator")
        
        self.initialize_base_geometry()
        
        self.create_structures()
        self.configure_structures()
        self.configure_styles()
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
    
    def configure_styles(self):
        
        self.style = ttk.Style(self)
        try: self.style.theme_use('clam')
        except: pass
        self.style.configure("enter.TButton", background="#9FCAFC", foreground="black", font=("Arial", 12, "bold"))
        self.style.configure("delete.TButton", background="#D45050", foreground="black", font=("Arial", 12, "bold"))
        self.style.configure("clear.TButton", background="#D45050", foreground="black", font=("Arial", 12, "bold"))
        self.style.configure("mode.TButton", background="#94F3D7", foreground="black", font=("Arial", 12, "bold"))
        self.style.configure("basic.TButton", background="#D8BC83", foreground="black", font=("Arial", 12, "bold"))
        self.style.map("basic.TButton", background=[('active', "#E09704")], relief=[('active', 'flat')])
        self.style.configure("advance.TButton", background="#C0B1DA", foreground="black", font=("Arial", 12, "bold"))
        self.style.map("advance.TButton", background=[('active', "#6634C2")], relief=[('active', 'flat')])
        self.style.configure("TButton", background="#E0E0E0", foreground="black", font=("Arial", 12, "bold"))
        
    def layout_structures(self):
        
        self.display_screen.place(x=6, y=5)
        self.main_button_frame.place(x=5, y=135, width=590, height=260)
        self.top_button_frame.place(x=359, y=5, width=235, height=125)
    
    def initialize_functions(self):
        
        self.bind_all("<Button-1>", self.Focus_On_Display_Screen)
        
        self.display_screen.bind("<Key>", self.restrict_keys_for_window)
        self.display_screen.bind("<Return>", self.Calculate_Expression)
        self.display_screen.bind("<BackSpace>", self.Delete_Text_In_Display)


 # Frame Structures:-

class MainButtonFrame(tk.Frame, UIFunctions):
    
    def __init__(self, parent_root):
        
        self.parent_root = parent_root  # parent class is the root.
        super().__init__(parent_root)
        
        self.initialize_buttons()
        self.layout_buttons_and_config_weights()
        

    def initialize_buttons(self):
        
        self.MAIN_BUTTONS = dict()
        Buttons_List = list(range(10)) + ['+', '_', 'x', '/', '(', ')', '🡠', '🡢', "."]
        
        for text in Buttons_List:
            # self.MAIN_BUTTONS[f"{text}"] = DisplayButton(self, text=f"{text}")
                if text in {'🡠', '🡢'}: self.MAIN_BUTTONS[f"{text}"] = CursorButton(self, text=f"{text}")
                else:                   self.MAIN_BUTTONS[f"{text}"] = DisplayButton(self, text=f"{text}")

        self.MAIN_BUTTONS['#'] = ttk.Button(self, text="↺", command=self.Show_Previous_Entry)
        
    def layout_buttons_and_config_weights(self):
        
        Position_Map = {
            0:(self.MAIN_BUTTONS['1'], self.MAIN_BUTTONS['2'], self.MAIN_BUTTONS['3'],  self.MAIN_BUTTONS['('], self.MAIN_BUTTONS[')']), 
            1:(self.MAIN_BUTTONS['4'], self.MAIN_BUTTONS['5'], self.MAIN_BUTTONS['6'],  self.MAIN_BUTTONS['+'], self.MAIN_BUTTONS['_']),
            2:(self.MAIN_BUTTONS['7'], self.MAIN_BUTTONS['8'], self.MAIN_BUTTONS['9'],  self.MAIN_BUTTONS['x'], self.MAIN_BUTTONS['/']),
            3:(self.MAIN_BUTTONS['#'], self.MAIN_BUTTONS['0'], self.MAIN_BUTTONS['.'],  self.MAIN_BUTTONS['🡠'], self.MAIN_BUTTONS['🡢']),
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
        Buttons_List = [('enter', 'EQUATE', self.Calculate_Expression), ('delete', 'DELETE', self.Delete_Text_In_Display),
                        ('clear', 'CLEAR',self.Clear_Display), ('mode', '    SHIFT\n'+'(Scientific)', self.Run_ModeSwitch_Main)]
        for (name, text, func) in Buttons_List:
            
            self.TOP_BUTTONS[f"{name}"] = ttk.Button(self, text=f"{text}", command=func, style=f"{name}.TButton")
                    
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

    # Sub_Frames for Top Frame :-
    
    class MainAdvancedFrame(tk.Frame):
        
        def __init__(self, parent_root):
            self.parent_root = parent_root  # parent class is the root.
            super().__init__(parent_root)
            self.create_buttons()
            self.layout_buttons()
            
        def create_buttons(self):
            self.ADV_BUTTONS = dict()
            self.Buttons_List = ['√', 'Tan', '^', 'Log', 'π', 'Ln', 'e', '%']
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
# ===================================================================================================================== # 




# MAIN :

class Main():
    
    def __init__(self):
        
        self.application = RootStructure(self)
    
    def run(self):
        
        self.application.mainloop()


if __name__ == '__main__':
    
    MAIN = Main()
    MAIN.run()




# X--------X----------X----------X----------X----------X----------X----------X----------X----------X----------X--------X #
#          X          X          X          X          X          X          X          X          X          X        X #
# X--------X----------X----------X----------X----------X----------X----------X----------X----------X----------X--------X # 

                                                                                                        # ~~ Visshwa Elayaraja
                                                                                                        #    School: Bala Vidya Mandir Sr. Sec School
                                                                                                        #    Class:  XII A (2025-26)
                                                                                                        #    Batch:  BVM 26'
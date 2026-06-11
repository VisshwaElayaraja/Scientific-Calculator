
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import math
import tkinter as tk
from tkinter import ttk

from Modules._customfunctions import *



# ===================================================================================================================== #



# Functional Classes :-

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
            self.string = text  # initializing in class for permitting broader usage.
            
            self.Clear_Display()  # removing the text from screen to display result after calculation.
        
        def _alter_text_string():
            
            replace_map = {" ":"", "x": "*", "^":"**", "π":str(math.pi), "e":"("+str(math.e)+")"}
            for replacing_item, replacement_item in replace_map.items():
                self.string = self.string.replace(replacing_item, replacement_item)
            
            self.string_list = list(self.string)         # working with list for its mutability.

        def _correct_minor_errors():
            
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
                            
                ## auto filling close brackets (if its missed out):
                if no_of_open_bracs > no_of_cls_bracs:
                    no_of_bracs_to_append = no_of_open_bracs - no_of_cls_bracs
                    repeat(lambda: self.string_list.append(")"), no_of_bracs_to_append)
        
        def _evaluate_advanced_functions():
            
            # joining characters of function name as word.
            func_char_holder = list()
            for char in self.string_list:
                if (char.isalpha()) and (len(char)==1):
                    func_char_holder.append(char)
                elif (func_char_holder) and (not char.isalpha()):
                    func_name = "".join(func_char_holder)
                    self.string_list = replace_sequence_in_list(self.string_list, func_char_holder, func_name)
                    func_char_holder.clear()
            
            def add_func_result_to_list(start, end, result):  # helper function for evaluate function.
                del self.string_list[start:end+1]
                self.string_list.insert(start, str(result))
                         
            def evaluate_function(func_sym, func):
                while func_sym in self.string_list:
                    start_index_of_func = self.string_list.index(func_sym)
                    try:
                        if (self.string_list[start_index_of_func+1] != "("):  #  -> if (function contains brackets)
                            raise Exception
                        end_index_of_func = self.string_list[start_index_of_func:].index(")")
                        evaluation_slice = self.string_list[start_index_of_func+2:end_index_of_func]
                        
                        func_input = eval("".join(evaluation_slice))
                        func_result = (eval(func))(func_input)
                        if func in {'math.sin', 'math.cos', 'math.tan'}:
                            func_result = round(func_result, 5)
                    except Exception:
                        func_result = "Error!"
                        return
                    end_index_for_original_list = end_index_of_func + start_index_of_func
                    add_func_result_to_list(start_index_of_func, end_index_for_original_list, func_result)
                    return
                        
            evaluate_function("√"  ,    "math.sqrt")     # checking and running functions.
            evaluate_function("Log",    "math.log10")
            evaluate_function("Ln" ,    "math.log")
            evaluate_function("Sin",    "math.sin")
            evaluate_function("Cos",    "math.cos")
            evaluate_function("Tan",    "math.tan")

        def _calculate_result():
            
            try:
                if "Error!" in self.string_list:
                    raise Exception
                self.string = "".join(self.string_list)                
                self.result = str(float(eval(self.string)))
                
            except Exception as Exc:
                self.result = "Error!"

        def _display_result_in_screen():
            
            current_cursor_position = self.parent_root.display_screen.index(tk.INSERT)
            self.parent_root.display_screen.insert(current_cursor_position, self.result)

        def main_run():
            
            _acquire_and_clear_text_from_screen()
            _alter_text_string()
            _correct_minor_errors()
            _evaluate_advanced_functions()
            _calculate_result()
            _display_result_in_screen()
            
            return self.result
        main_run()



class ModeSwitchFunctions():
    
    Tab_Is_Open = False
    
    def _advance(self):
        
        def __layout_frames():
            
            self.parent_root.sin_cos_advanced_frame.place(x=682, y=3, width=116, height=132)
            self.parent_root.main_advanced_frame.place(x=566, y=135, width=232, height=260)
        
        def __extend_and_adjust_window():
            
            self.TOP_BUTTONS['mode'].config(text='MODE\n'+'(basic)')
            
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
            
            self.TOP_BUTTONS['mode'].config(text='   MODE\n'+'(advance)')

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
    


# ===================================================================================================================== #



# Structural Classes :-

set_of_adv_functions = {'Sin', 'Cos', '√', 'Tan', "Log", 'Ln', '#', '*'}


class DisplayButton(ttk.Button):
    
    def __init__(self, parent_frame, text):
        
        self.parent_frame = parent_frame  # parent class is the frame.
        super().__init__(parent_frame, text=text, command=self.add_to_display)
    
    def add_to_display(self):
        
        item = self.cget("text")
        if item == "_":
            item = "-"  # using _ instead of - in button text alone (for visibility.)
        elif item in set_of_adv_functions:
            if item in {'#', '*'}: item = ""
            else: item = item + "()"
        
        
        current_cursor_position = self.parent_frame.parent_root.display_screen.index(tk.INSERT)
        self.parent_frame.parent_root.display_screen.insert(current_cursor_position, item)
        if item in set(map(lambda text: text + "()", set_of_adv_functions)):
            current_cursor_position = self.parent_frame.parent_root.display_screen.index(tk.INSERT)
            self.parent_frame.parent_root.display_screen.mark_set("insert", f"{current_cursor_position}-1c")



# ===================================================================================================================== #


# class History(tk.Tk):
    
#     def __init__(self):
        
#         super().__init__()
#         self.title("History")
#         self.power_status = "OFF"
#         self.initialize_base_geometry()

#     def initialize_base_geometry(self):
        
#         self.geometry("300x150")  # x:y ratio is 1.5.
#         self.minsize(600, 400)    # 
#         self.maxsize(600, 400)    # 
        
#         self.columnconfigure(0, weight=1)  # 
#         self.rowconfigure(0, weight=1)     # 
#         self.columnconfigure(1, weight=1)  # 
#         self.rowconfigure(1, weight=1)     # for setting correct size for the display(entry) widget and main button frame.

# def open_HistoryTab():
#     HistoryTab = History()
#     HistoryTab.mainloop()

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import math
from Modules._customfunctions import *


# ===================================================================================================================== #


class ExpressionCalculator():

    def acquire_and_clear_text_from_screen(self, string):
        
        self.string = string
        
        # text = self.parent_root.display_screen.get()
        # self.string = text  # initializing in class for permitting broader usage.
        # UI_Functions.clear_display()  # removing the text from screen to display result after calculation.

    
    def alter_text_string(self):
        
        self.string = self.string.replace(" ", "")  # removing blank spaces (as it may produce unexpected result while iterating lists).
        self.string_list = list(self.string)        # working with list for its mutability.


    def correct_minor_errors(self):
        
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
                no_of_appending_bracs = no_of_open_bracs - no_of_cls_bracs
                repeat(lambda: self.string_list.append(")"), no_of_appending_bracs)
        
        
    def validate_expression(self):
        
        self.ErrorStatus = {"Status": "False",
                            "ErrorName": None}
        
        ## checking for valid placement of arithmetic operators:
        arithmetic_operators = {'+', '-', '*', '/', "%"}
        for i in range(len(self.string_list)):
            if (((self.string_list[i] == "(") and (self.string_list[i+1] in arithmetic_operators)) or
                ((self.string_list[i] == ")") and (self.string_list[i-1] in arithmetic_operators))):
                self.ErrorStatus["Status"] = "True"
                self.ErrorStatus["ErrorName"] = "InvalidArithmeticOperatorError"
                return
                
        brac_array = list()        
        ## checking for valid parenthesis:
        for char in self.string_list:
            print(char, end=" ")
            
            if char == ")":

                if brac_array:
                    brac_array.pop()
                    print("matched")
                else:
                    self.ErrorStatus["Status"], self.ErrorStatus["ErrorName"] = "True", "InvalidParenthesisError"
                    print("unmatched")
                    break

            elif char == "(":
                brac_array.append(char)
                
        else:
            self.ErrorStatus["Status"], self.ErrorStatus["ErrorName"] = f"{bool(brac_array)}", "InvalidParenthesisError"
    
    
    def calculate_result(self):  # Result Calculation
        
        self.string = "".join(self.string_list)
        
        if self.ErrorStatus["Status"] == "True":
            self.result = self.ErrorStatus.get("ErrorName")
                
        elif self.ErrorStatus["Status"] == "False":
            self.result = eval(self.string)


    def display_result_in_screen(self):
        
        print(f"\n{self.result = }")
        

    def main_run(self, string):
        
        self.acquire_and_clear_text_from_screen(string)
        self.alter_text_string()
        self.correct_minor_errors()
        self.validate_expression()
        self.calculate_result()
        self.display_result_in_screen()
        
        return self.result


# ===================================================================================================================== #


# Test Run
print("\n// Test_Run:\n")

string1 = "(1+2*3+4) / 12**(1+2))))(("
string2 = "(((123 + 456) * (789 - 123)) / ((456 + 123) * (789 - 123))) + (((123 * 456) / (789 - 123)) - ((789 * 123) % (456 + 123))) * (((123 + 456) * (789 - 123)) / ((456 + 123) * (789 - 123))))"
string3 = "(98 + 125 - 77 ) * 23 / 5 + ()(101 - 63 + 22) * 4 - 17 + 88 / 2 + (55 + 33 * 2 - 11 * 7 + 99 / 3 * 2 - (42 + 18 - 5"

expression_calculator = ExpressionCalculator()
result = expression_calculator.main_run(string3)




import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Calculator_Structures import *


# ===================================================================================================================== #


class Main():
    
    def __init__(self):
        
        self.application = RootStructure(self)
    
    def run(self):
        
        self.application.mainloop()


# ===================================================================================================================== #


if __name__ == '__main__':
    
    MAIN = Main()
    MAIN.run()
    


 #  MODULES & SET-UP:

from math import *

__all__ = ["get_valid_int","get_valid_float", "repeat", "replace_sequence_in_list"]

# ------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #

 #  FUNCTIONS

def repeat(func, reps:int) -> None: 
    if reps == 0: return
    func()
    repeat(func, reps-1)


def replace_sequence_in_list(lst, seq, rep) -> list:
    n = len(seq)
    i = 0
    result = []
    
    while i < len(lst):
        if lst[i:i + n] == seq:
            result.append(rep)
            i += n
        else:
            result.append(lst[i])
            i += 1
    
    return result


def get_valid_int(prompt: str, range_start:int=1, range_end:int=100000) -> int:
    while True:
        try:
            value: int = int(input(prompt))
            if (value < range_start) or (value > range_end):
                raise ValueError
        except ValueError:
            print("Enter a valid number")
        else:
            return value


def get_valid_float(prompt: str, range_start:float=1, range_end:float=100000) -> float:
    while True:
        try:
            value: float = float(input(prompt))
            if (value < range_start) or (value > range_end):
                raise ValueError
        except ValueError:
            print("Enter a valid number")
        else:
            return value


# ------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #


if __name__ == "__main__":

    def no_using() -> None:

        def get_original_index(entered_index: int, operation: str, number: int) -> int:
            if operation in ["sum", "s", "+"]:
                original_index = entered_index + number
                return original_index
            elif operation in ["subtract", "sub", "difference", "diff", "-"]:
                original_index = entered_index - number
                return original_index

        def avail_check_int(start, end, value, false_prompt):
            if value not in range(start, end):
                print(false_prompt)
                return

        def get_str_in_array(prompt: str, array: list) -> str:
            while True:
                value = input(prompt)
                if value not in array:
                    print(f"Item doesn't exist")
                    continue
                break
            return value

        return None
    

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #



if __name__ == '__main__':
    # Test Code:
    pass

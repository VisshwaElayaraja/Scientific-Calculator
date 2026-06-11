
# MODULES & SET-UP:

from math import *
__all__ = ["StaticArray", "Search", "Sort"]


# ------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #


# DATA STRUCTURES

class StaticArray:

    def __init__(self, elements: tuple = (), capacity: int = 10):
        self.capacity = capacity
        self.size = len(elements)

        if self.size > self.capacity:
            raise OverflowError("Not Enough Capacity To Store All Items.")

        self.array = list(elements) + ([None] * abs(self.capacity - self.size))

    def __len__(self):
        return len(self.array)

    def __getitem__(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            return IndexError("Index Out Of Bounds")

    def __setitem__(self, index, value):

        if 0 <= index < len(self.array):
            self.array[index] = value
        else:
            return IndexError("Index Out Of Bounds")

    def __repr__(self):
        return f"{self.array}"

    def __str__(self):
        return f"{self.array}"

    def display(self, mod=False, sep: str = " ", end: str = "\n"):

        if mod:
            print(*self.array, sep=sep, end=end)
        else:
            print(self.array)

    def add(self, item):

        if self.size == self.capacity:
            raise OverflowError("Cannot Add Item. Capacity Reached For Array.")

        self.array[self.size] = item
        self.size += 1

    def pop(self):

        self.array[self.size - 1] = None
        self.size -= 1

    def insert(self, item, index: int):

        if self.size == self.capacity:
            raise OverflowError("Cannot Insert Item. Capacity Reached For Array.")

        for i in reversed(range(index + 1, self.size + 1)):
            self.array[i] = self.array[i - 1]

        self.array[index] = item
        self.size += 1

    def delete(self, item):

        if item == self.array[self.size - 1]:
            self.array[self.size - 1] = None
            self.size -= 1
            return

        item_exists = False
        for i in range(self.size - 1):
            if self.array[i] == item:
                item_exists = True
                for j in range(self.size - i - 1):
                    self.array[i + j] = self.array[i + j + 1]

        if item_exists:
            self.array[self.size - 1] = None
            self.size -= 1


# ALGORITHMS

class Search:

    @staticmethod
    def BinarySearch(array:list, target):

        array = sorted(array)
        low_ptr = 0
        high_ptr = len(array) - 1

        while low_ptr <= high_ptr:

            mid_ptr = int(low_ptr + (high_ptr - low_ptr) / 2)
            mid_value = array[mid_ptr]

            if target < mid_value:
                high_ptr = mid_ptr - 1
            elif target > mid_value:
                low_ptr = mid_ptr + 1
            else:
                return mid_ptr

        return -1

    @staticmethod
    def interpolationSearch(array:list, target):

        low = 0
        high = len(array) - 1

        while (array[low] <= target <= array[high]) and (low <= high):

            probe = int(low + (((high - low) / (array[high] - array[low])) * (target - array[low])))

            if target < array[probe]:
                high = probe - 1
            elif target > array[probe]:
                low = probe + 1
            else:
                return probe

        return -1


class Sort:

    @staticmethod
    def bubbleSort(array:list):

        l = len(array)
        for m in range(l-1):
            for n in range(l-m-1):
                if array[n] > array[n+1]:
                    temp = array[n]
                    array[n] = array[n+1]
                    array[n+1] = temp

    @staticmethod
    def selectionSort(array:list):

        l = len(array)
        for i in range(l - 1):
            low = i
            for j in range(i + 1, l):
                if array[j] < array[low]:
                    low = j
            temp = array[low]
            array[low] = array[i]
            array[i] = temp

    @staticmethod
    def insertionSort(array):

        for i in range(1, len(array)):
            low = i
            while low > 0 and array[low-1] > array[low]:
                temp = array[low]
                array[low] = array[low-1]
                array[low-1] = temp
                low -= 1
            array[low] = temp
    
    @staticmethod
    def mergeSort(array):
        
        # Helper Method
        def merge(left_array, right_array, array):
        
            length = len(array)
            left_length = len(left_array)
            right_length = len(right_array)
            
            l = r = i = 0
            while (l < left_length) and (r < right_length):
                if left_array[l] < right_array[r]:
                    array[i] = left_array[l]
                    i += 1
                    l += 1
                else:
                    array[i] = right_array[r]
                    i += 1
                    r += 1
            # The above loop will terminate with one element unseen, as it ends with either of the conditions returning false.       
            while l < left_length:
                array[i] = left_array[l]
                i += 1
                l += 1
            while r < right_length:
                array[i] = right_array[r]
                i += 1
                r += 1
                    
            return array
        
        # Main Method  
        def split():
        
            if len(array) <= 1: return  # Base case.
            
            mid = len(array) // 2
            left_array = array[:mid]
            right_array = array[mid:]
            
            Sort.mergeSort(left_array)  # Recursive case.
            Sort.mergeSort(right_array) #
            merge(left_array, right_array, array)  # Starts to function from teh top of the call stack.
                                                # (i.e. when base case of a recursion is true and the recursion terminates)
        
        split() # makes the whole function run.


# ------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #


if __name__ == "__main__":

    def private():

        class DynamicArray:

            def __init__(self, capacity: int = 10, arguments: tuple = ()):

                self.size = len(arguments)
                self.capacity = capacity

                if self.size >= self.capacity:
                    self.capacity = self.size

                self.array = list(arguments) + ([None] * abs(self.capacity - self.size))

            def display(self, mod: bool = False, sep: str = " ", end: str = "\n"):

                if mod:
                    print(*self.array, sep=sep, end=end)
                else:
                    print(self.array)

            def add(self, item):

                if self.size == self.capacity:
                    self.grow()

                self.array[self.size] = item
                self.size += 1

            def pop(self):

                self.array[self.size - 1] = None
                self.size -= 1

                if self.size <= (1 / 3) * self.capacity:
                    self.shrink()

            def insert(self, item, index: int):

                if index <= self.size:

                    if self.size == self.capacity:
                        self.grow()

                    i = self.size
                    while i > index:
                        self.array[i] = self.array[i - 1]
                        i -= 1

                    self.array[index] = item
                    self.size += 1

            def delete(self, item):

                index = 0
                for i in range(self.size):
                    if self.array[i] == item:
                        index = i
                        break

                if item in self.array:
                    for i in range(index, self.size - 1):
                        self.array[i] = self.array[i + 1]
                    self.array[self.size - 1] = None
                    self.size -= 1

                if self.size <= (1 / 3) * self.capacity:
                    self.shrink()

            def grow(self):

                self.capacity = int(ceil(self.capacity * 1.5))
                self.array.extend([None] * int(ceil(self.capacity) - self.size))

            def shrink(self):

                self.capacity = int(ceil(self.capacity * 0.5))
                self.array = self.array[0:self.capacity]


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx #

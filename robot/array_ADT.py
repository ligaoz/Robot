'''
Created on 9 Mar 2017

@author: liga
'''
import time
import matplotlib.pyplot as plt


class array_ADT:
    def __init__(self):
        self.array = []
        self.size = 0 
#--------------------------methods---------------------------------------
    
    def is_empty(self):
        "Return True if the stack is empty"
        return self.size == 0
        
    def len(self):
        "Return size of the stack"
        return self.size
        
    def push(self,elem):
        "Ads element elem in the array"
        self.array += [elem,] #save element in array
        self.size += 1 #increment the size counter
        
    def indexAt(self,index):
        "Returns element at index value"
        if index<self.size:
            return self.array[index]
        else:
            return False
    
    def pop(self):
        "Removes and returns the last element from the stack"
        if self.is_empty(): # check if stack is not empty
            print("Stack is empty")
            return False
        else:
            answer = self.array[self.size-1]
            self.size -= 1 # decrease the size counter
            del self.array[self.size] # delete last  entry from array
            return answer
    
    def __str__(self):
        result = "" 
        if not self.is_empty():
            for i in range(self.size):
                result += "%s " % str(" -> "+str(self.array[i]))
            return result
        else:
            return "Empty stack"
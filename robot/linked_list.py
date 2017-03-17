'''
Created on 9 Mar 2017

@author: liga
'''
import time
import matplotlib.pyplot as plt
class linked_list:
    "Linked list LIFO Stack implementation "
#-------------------------- nested Node class --------------------------
    class _Node(object):
        """ A Node in a Linked List
        Lightweight, not public class for storing a singly linked node
        """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._next = next #reference to next node
            self._element = element #reference to element itself
        
        
    def __init__(self):
        """Create empty stack"""
        self._head = None #reference to the head node
        self._size = 0 #number of elements in linked list
        
#--------------------------methods---------------------------------------
        
    def __len__(self):
        "Return number of elements in the list"
        return self.__size
    
    def is_empty(self):
        "Return True if the stack is empty"
        return self._size == 0
    
    def size(self):
        "Return size of the stack"
        return self._size
    
    def push(self,elem):
        "Ads element elem to the tail of the stack"
        self._head = self._Node(elem, self._head) # create and link a new node self
        self._size += 1 #increment the size counter
    
    def head(self):
        "Return the last element in the stack"
        if self.is_empty():
            raise print( "Stack is empty ")
        return self._head._element  
    
    def pop(self):
        "Removes and returns the last element from the stack"
        if self.is_empty(): # check if stack is not empty
            raise print( "Stack is empty" )
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1 # decrease the size counter
        del self.array[self._size] # delete last  entry from array
        return answer
    
    def remove(self):
        if self.is_empty(): # check if stack is not empty
            raise print( "Stack is empty" )
        else:
            self._size -= 1 # decrease the size counter
            del self.array[self._size]
    
    def __str__(self):
        result = "-> " 
        if not self.is_empty():
            for i in range(self._size):
                result += "%s " % str(str(self.array[i])+" -> ")
            return result
        else:
            return "Empty stack"

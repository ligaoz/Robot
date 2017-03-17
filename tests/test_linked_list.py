'''
Created on 14 Mar 2017

@author: liga
'''
from linked_list import linked_list
from nose.tools import *


def test_stack():
    s = linked_list()
    s.push("elem 1")
    s.push("elem 2")
    s.push("2")
    s.pop() #test method on lists
    s.remove() #test method on array 
    print(s)
    eq_(s._size,1, print("test ok"))
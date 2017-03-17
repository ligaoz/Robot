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
    eq_(s.head(),"2", print("head method test passed"))
    s.pop() #test method on lists
    eq_(s.size(),2, print("push and pop test passed"))
    s.pop()
    s.pop() 
    eq_(s.is_empty(),True,print("is_empty method test passed"))
    print(s)
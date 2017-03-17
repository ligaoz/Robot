'''
Created on 17 Mar 2017

@author: liga
'''
from  array_ADT import array_ADT
from nose.tools import *

def test_array():
    arr = array_ADT()
    arr.push(1)
    arr.push(2)
    arr.push(3)
    eq_(arr.size,3, print("array size test passed"))
    arr.pop()
    eq_(arr.size,2,print("array pop method test passed"))
    arr.pop()
    eq_(arr.is_empty(),False, print("Is_empty test passed"))
    eq_(arr.pop(),1,print("array pop return value test passed"))
    eq_(arr.len(),0,print("array length method test passed"))
    eq_(arr.pop(),False, print("array pop exception test passed"))
    eq_(arr.is_empty(),True, print("Is_empty test passed"))
    print(arr)
    arr.push(1)
    arr.push(2)
    arr.push(3)
    print(arr)
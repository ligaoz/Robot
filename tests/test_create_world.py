'''
Created on 12 Mar 2017

@author: liga
'''
from nose.tools import *
from world import *

def test_create_world():
    data = [["w", 1, 2],["w", 1, 3],["w", 1, 4],["w",1, 5]]
    new = create_world(8, data,[5,2],[7,7])
    msg = print("Add wall passed")
    eq_(new.matrix[1][2],1,msg)
    eq_(new.matrix[1][3],1,msg)
    eq_(new.matrix[1][4],1,msg)
    eq_(new.matrix[1][5],1,msg)
    eq_(create_world(8, data,[1,5],[1,3]), False, print("Robot and goal check passed"))
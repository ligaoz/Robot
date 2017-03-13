'''
Created on 10 Mar 2017

@author: liga
'''
from nose.tools import *
from robot.world import world

def test_world():
    #data,size = parseLine("/Users/liga/Documents/robot_data.txt")
    newWorld = world(8)
    for i in range(0,8):
        newWorld.wall(0,i)
    eq_(newWorld.matrix[0][1], 1)
    eq_(newWorld.matrix[0][5], 1)
    eq_(newWorld.matrix[0][7], 1)
    
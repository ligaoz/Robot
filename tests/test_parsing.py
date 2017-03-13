'''
Created on 12 Mar 2017

@author: liga
'''
from nose.tools import *
from robot.world import parseLine
def test_parse():
    data, size, goal,robot = parseLine("8x8 \nw 1,2\nw 1,3\nw 1,4\nw 1,5\n robot 0,7\ngoal 7,0")
    eq_(size, 8, print("Size test passed"))
    eq_(goal, [0,7], print("Goal test passed"))
    eq_(robot, [7,0], print("Robot test passed"))
    
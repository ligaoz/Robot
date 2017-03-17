'''
Created on 16 Mar 2017

@author: liga
'''
from search import search
from nose.tools import *
from robot.robot import robot
from world import parseLine, create_world
from linked_list import linked_list

def test_search():
    
    data, size, goal,r = parseLine("8x8 \nw 1,2\nw 1,3\nw 1,4\nw 1,5\n robot 4,2\ngoal 7,0")
    world = create_world(size, data, r, goal)
    world.print_world()
    stack = linked_list()
    r2d2 = robot(r)
    search(r2d2.x,r2d2.y,world,stack)

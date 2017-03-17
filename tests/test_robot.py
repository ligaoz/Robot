'''
Created on 13 Mar 2017

@author: liga
'''
from robot.robot import robot
from nose.tools import *

def test_robot():
    r2d2 = robot([1,2])
    r2d2.where_is_robot()
    print(r2d2.y)
    x = r2d2.move_up()
    print(x.x)
    print(r2d2.y)
    eq_(r2d2.robot[0],1, print("move up OK"))
    robot.move_down(r2d2)
    eq_(r2d2.robot[1],2, print("move down OK"))
    robot.move_right(r2d2)
    eq_(r2d2.robot[0],2, print("move right OK"))
    robot.move_left(r2d2)
    eq_(r2d2.robot[0],1, print("move left OK"))
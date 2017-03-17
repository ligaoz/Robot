'''
Created on 9 Mar 2017

@author: liga
'''
import argparse
from robot.world import parseLine, create_world
from array_ADT import array_ADT
from robot import robot
from search import search

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    arguments = parser.parse_args()
    fileHandle = open(arguments.input).read()
    data, size, goal, rob = parseLine(fileHandle)
    if create_world != False:
        world = create_world(size, data, rob, goal)
        world.print_world()
        stack = array_ADT()
        r2d2 = robot(rob)
        search(r2d2.x,r2d2.y,world,stack)
        print(stack)
    else:
        print("World couldn't be created")
        
if __name__ == '__main__':
    main()

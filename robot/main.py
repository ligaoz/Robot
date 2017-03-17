'''
Created on 9 Mar 2017

@author: liga
'''
import argparse
from world import parseLine, create_world
from linked_list import linked_list
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
        stack = linked_list()
        r2d2 = robot(rob)
        search(r2d2.x,r2d2.y,world, size,stack)
        
if __name__ == '__main__':
    main()

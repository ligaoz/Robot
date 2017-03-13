'''
Created on 9 Mar 2017

@author: liga
'''
import argparse
from world import parseLine, create_world

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    arguments = parser.parse_args()
    fileHandle = open(arguments.input).read()
    data, size, goal, robot = parseLine(fileHandle)
    if create_world != False:
        x = create_world(size, data, robot, goal)
        x.print_world()

if __name__ == '__main__':
    main()

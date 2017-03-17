'''
Created on 16 Mar 2017

@author: liga
'''
from robot import robot
from linked_list import linked_list
from world import parseLine, create_world

def search(x,y,world,size,stack):
    coordin = [x,y]
    if world.matrix[x][y] == 2:
        print ('found at %d,%d' % (x, y))
        return True
    elif world.matrix[x][y] == 1:
        print ('wall at %d,%d' % (x, y))
        return False
    elif world.matrix[x][y] == 3:
        print ('visited at %d,%d' % (x, y))
        return False
        
    print ('visiting %d,%d' % (x, y))
    # mark as visited
    stack.push(coordin)
    world.robotX = x
    world.robotY = y
    world.matrix[x][y] = 3
    world.print_world()
    
        # explore neighbors clockwise starting by the one on the right
    if ((x < size-1 and search(x+1,y,world, size,stack))
        or (y > 0 and search(x,y-1,world, size,stack))
        or (x > 0 and search(x-1,y,world, size,stack))
        or (y < size-1 and search(x,y+1,world, size,stack))):
        return True
    return False

'''
Created on 16 Mar 2017

@author: liga
'''



"""def alghorithm(world):
    "Function to choose sequence to visit neighboring cells "
    rX = world.robotX
    rY = world.robotY
    gX = world.goalX
    gY = world.goalY
    
    if rX < gX and rY < gY:
        x < size-1 and search(x+1,y,world, size,stack)
        y > 0 and search(x,y+1,world, size,stack
        """
    
def search(x,y,world,stack):
    "Recursive function to find the goal"
    coordin = [x,y]
    if world.matrix[x][y] == 2:
        print ('Goal found at %d,%d' % (x, y))
        stack.push(coordin)
        return True
    elif world.matrix[x][y] == 1:
        print ('Wall at %d,%d' % (x, y))
        return False
    elif world.matrix[x][y] == 3:
        print ('Cell visited at %d,%d' % (x, y))
        return False
        
    print ('visiting %d,%d' % (x, y))
    # mark as visited
    stack.push(coordin)
    world.robotX = x
    world.robotY = y
    world.matrix[x][y] = 3
    world.print_world()
    
        # explore neighbors clockwise 
    if ((x < world.size-1 and search(x+1,y,world,stack))
        or (y > 0 and search(x,y-1,world,stack))
        or (x > 0 and search(x-1,y,world,stack))
        or (y < world.size-1 and search(x,y+1,world,stack))):
        return True
    return False

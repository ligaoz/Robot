'''
Created on 9 Mar 2017

@author: liga
'''

class world:

    def __init__(self,size,robot,goal):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]
        self.robotX = robot[0]
        self.robotY = robot[1]
        self.goalX = goal[0]
        self.goalY = goal[1]
        
        

    def wall(self,x,y):
        self.matrix[x][y] = 1
    
    def print_world(self):
        for i in range(self.size):
            print ()
            for j in range(self.size):
                if i == self.robotX and j == self.robotY:
                    print("r2d2", end="")
                elif i == self.goalX and j == self.goalY:
                    print("goal",end=" ")
                else:
                    print (" ",self.matrix[i][j]," ",end='')
            print()
    

def create_world(size, data, robot, goal):
    newWorld = world(size,robot,goal)
    for line in data:
        x = int(line[1])
        y = int(line[2])
        newWorld.wall(x, y)
    def add_robot(robot):
        x = robot[0]
        y = robot[1]
        if newWorld.matrix[x][y] == 1:
            print("Robot can't be in the wall")
            return False
        else:
            return True
        
    def add_goal(goal):
        x = goal[0]
        y = goal[1]
        if newWorld.matrix[x][y] == 1:
            print("Goal can't be in the wall")
            return False
        else:
            return True
    
    if add_robot(robot) and add_goal(goal):
        return newWorld
    else:
        return False


def parseLine(data):
        """Function to parse data file"""
        data = data.split("\n")
        x = data[0].split("x")
        size = int(x[0])
        data.pop(0)
        p = data[-1].replace(",", " ").split()
        robot = [int(p[1]),int(p[2])]
        data.pop()
        p = data[-1].replace(",", " ").split()
        goal = [int(p[1]),int(p[2])]
        data.pop()
        
        if size>0: 
            cleanData = []
            for line in data:
                line = line.strip()
                line = line.replace(",", " ")
                cleanData += [line.split(), ]
            return cleanData, size, goal, robot
        else:
            return False


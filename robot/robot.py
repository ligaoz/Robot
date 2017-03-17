'''
Created on 9 Mar 2017

@author: liga
'''
class robot:
    def __init__(self,xy):
        self.x = xy[0]
        self.y = xy[1]
        self.robot = [self.x,self.y]
    
    def robot(self):
        return self.robot
    
    def move_up(self):
        self.y -= 1
        self.robot[1] = self.y
        return self.robot
    
    def move_down(self):
        self.y += 1
        self.robot[1] = self.y
        return self.robot
    
    def move_left(self):
        self.x -= 1
        self.robot[0] = self.x
        return self.robot
    
    def move_right(self):
        self.x += 1
        self.robot[0] = self.x
        return self.robot
    
    def where_is_robot(self):
        print(self.robot)

'''
Created on 9 Mar 2017

@author: liga
'''
class robot:
    def __init__(self,x,y):
        self.robot = [self.x,self.y]
        
    def move_up(self,robot):
        return self.robot[self.x,self.y-1]
    
    def move_down(self,robot):
        return self.robot[self.x,self.y+1]
    
    def move_left(self,robot):
        return self.robot[self.x-1,self.y]
    
    def move_right(self,robot):
        return self.robot[self.x+1,self.y]
    
    def where_is_robot(self):
        print(self.robot)
        
'''
Created on 9 Mar 2017

@author: liga
'''
from __builtin__ import file

    
def create_world(data,size):
    """Function to create multidimensional array to represent world
     Function also checks if size input is valid which is size>0"""
    def parseLine(data):
        """Function to parse data file"""
        cleanData = []
        for line in data:
            line = line.strip()
            line = line.replace(",", " ")
            cleanData += [line.split(), ]
            print(line)
        return cleanData
    
    def add_walls(x,y,matrix):
        """function to add the walls in the world"""
        matrix[x][y] = 1
        return matrix
     
    if size > 0:
        matrix = [[0 for x in range(size)] for x in range(size)]
        for line in file:
            x = line[1]
            y = line[2]
            matrix = add_walls(x,y,matrix)
        return matrix
    else:
        return False
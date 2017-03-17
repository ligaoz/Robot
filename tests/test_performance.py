'''
Created on 14 Mar 2017

@author: liga
'''
from linked_list import linked_list
import time 
import matplotlib.pyplot as plt

def test_perf():
    
    # Create an array that will contain running times.
    running_times = []

    for n in range (0,3000, 10):
    # Create set object named s.
        s = linked_list()

        for i in range(n):
            s.push(i)
    
        start = time.time()

        #s.is_empty()
        #s.size()
        #s.push('a')
        #s.remove()

        end = time.time()

        run_time = end - start
        running_times.append(run_time)
        
    # Plot the running times
    plt.plot(running_times, 'bx')
    plt.xlabel('Size of N (x 1000)')
    plt.ylabel('Time')
    
    
    
    plt.show()
    





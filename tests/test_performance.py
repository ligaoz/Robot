'''
Created on 14 Mar 2017

@author: liga
'''
from linked_list import linked_list
import time 
import matplotlib.pyplot as plt
from array_ADT import array_ADT

def test_perf():
    "Uncomment performance test for array or linked list to run it"
#----------------------------Linked list performance test-------------------------
    """# Create an array that will contain running times.
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
        #s.pop()

        end = time.time()

        run_time = end - start
        running_times.append(run_time)
        
    # Plot the running times
    plt.plot(running_times, 'bx')
    plt.xlabel('Size of N (x 1000)')
    plt.ylabel('Time')
    plt.show()
    """
#--------------------------Array performance test----------------------

    # Create an array that will contain running times.
    running_times_arr = []

    for n in range (0,3000, 10):
    # Create array object named a.
        a = array_ADT()
        for i in range(n):
            a.push(i)
    
        start = time.time()
        #uncomment one feature at a time to test it
        #a.is_empty()
        #a.sizes
        
        #a.push('a')
        #a.pop()

        end = time.time()

        run_time = end - start
        running_times_arr.append(run_time)
        
    # Plot the running times
    plt.plot(running_times_arr, 'bx')
    plt.xlabel('Size of N (x 1000)')
    plt.ylabel('Time')
    plt.show()
    





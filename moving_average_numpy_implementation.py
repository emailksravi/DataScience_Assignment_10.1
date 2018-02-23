"""
Write a function to find moving average in an array over a window:
Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.
"""
import numpy as np

input_array = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
window = 3
moving_average_list = list()

for start_index in range(0,len(input_array)):
    
    ## Set Start and End of windowed array 
    end_index = start_index + window
    
    ## Stop looping once end_index reaches input_array length
    if end_index > len(input_array):
        break
    
    ## Get windowed array from the input array
    windowed_array = np.take(input_array, range(start_index, end_index))
    
    
    ## On windowed array, take average of all individual elements
    print ("Calculating average for windowed array " + windowed_array )
    result_avg = np.average(windowed_array)
    
    ## Append result_average for this window elements to the final list
    moving_average_list.append(result)


## print final list of moving averages
print ("Final list of moving avg =>  " + moving_average_list)
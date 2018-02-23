"""
Write a function to find moving average in an array over a window:
Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.
"""
import numpy as np

input_array = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
window = 3
moving_average_list = list()

# Implementation of moving_averages based on convolution technique.
# This is highlighted in https://stackoverflow.com/questions/20036663/understanding-numpys-convolve

weights = np.repeat(1.0, window)/window
moving_average_list = np.convolve(input_array, weights, 'valid')

## print final list of moving averages
print ("Final list of moving avg =>  " + str(moving_average_list))

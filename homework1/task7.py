"""
task7.py - Shows the use of the NumPy package in Python.
Includes a function to calculate the mean of a list of numbers using NumPy.
"""

import numpy as np

def calculate_array_mean(numbers):
    """
    Calculates the average of a list of numbers using NumPy.

    Parameters:
    - numbers (list of int/float): A list of numbers.

    Returns:
    - float: The mean of the numbers.
    """
    array = np.array(numbers)  # Convert list to NumPy array
    return np.mean(array)  # Compute mean using NumPy

# Run this block only if the script is executed directly
if __name__ == "__main__":
    sample_data = [10, 20, 30, 40, 50]
    print(f"Mean of {sample_data} is {calculate_array_mean(sample_data)}")

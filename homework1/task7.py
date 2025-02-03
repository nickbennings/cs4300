import numpy as np

def calculate_array_mean(numbers):
    array = np.array(numbers)
    return np.mean(array)

# Run only when executed directly
if __name__ == "__main__":
    sample_data = [10, 20, 30, 40, 50]
    print(f"Mean of {sample_data} is {calculate_array_mean(sample_data)}")

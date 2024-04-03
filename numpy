import numpy as np

#Median
def median(numbers):
    return np.median(numbers)
numbers = [5, 2, 9, 1, 7, 3, 8, 4, 6]
print("List of numbers:", numbers)
print("Median:", median(numbers))

#MEAN 
number=[1,2,3,4,5,6,7,8]
mean = np.mean(number)
print("Mean:", mean)

#Mode
mode = np.mode(numbers)
print("Mode:", mode)

#Standard Deviation
std_dev = np.std(numbers)
print("Standard Deviation:", std_dev)

# Addition
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])
addition = np.add(array1 , array2)
print("Result of Addition:", addition)

#Subtraction
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])
subtraction = np.subtract(array1 , array2)
print("Result of subtraction:", subtraction)

#Multiplication
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])
multiplication = np.multiply(array1 , array2)
print("Result of Multiplication:",multiplication)


array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])
matrix_multiplication = np.malmul(array1 , array2)


# Transpose an array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

transposed_arr = np.transpose(arr)
print("Original array:")
print(arr)
print("\nTransposed array:")
print(transposed_arr)

#Ones
ones_array = np.ones((4, 4))
print(ones_array)

# Zeros
zeros_array = np.zeros((4, 3))
print(zeros_array)

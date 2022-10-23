import numpy as np

# The zeros() function inside numpy creates an array with n number of zeroes inside it.
a = np.zeros(10)
print(a)

# The full() function creates a two-dimensional matrix of dimensions 2 x 10 consisting only of the values 0.7.
b = np.full((2, 8), 0.8)
print(b)

# linspace() function divides the values between 0 and 25 in 7 equal parts. The resultant matrix is in the output.
c = np.linspace(0, 25, 7)
print(c)

# return object type
print(type(c))

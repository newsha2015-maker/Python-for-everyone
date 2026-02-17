import numpy as np

a = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

print(a[1:3])
print(a[1:-2])
print(a[-4:3])
print(a[-5:-2])

# # omitting indices
print(a[:3])

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(a[0, 1:4])  # Frist row, 2nd to 4th column
print(a[0:2, 2])  # First two rows, 3rd column
print(a[0:2, 1:4]) # First two row, 2nd to 4th colum

a = np.arange(25).reshape( 5, 5)
print(a)

print(a[1, -1])  # we can count backwards

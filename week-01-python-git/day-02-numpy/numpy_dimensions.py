import numpy as np

# Level 1: Different dimensions

a = np.array([1, 2, 3, 4])

b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

c = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("Array A:")
print(a)

print("\nArray B:")
print(b)

print("\nArray C:")
print(c)

print("\nDimensions:")
print(a.ndim)
print(b.ndim)
print(c.ndim)

print("\nShapes:")
print(a.shape)
print(b.shape)
print(c.shape)
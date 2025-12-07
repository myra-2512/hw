import numpy as np

num=np.array([1,2,3,4,5,6,7,8,9,0])

num_modified = np.where(num % 2 != 0, -1, num)

num_2d = num.reshape(2, 5)

for i in range(num_2d.shape[0]):
    for j in range(num_2d.shape[1]):
        num_2d[i, j] += num[j]

print("original array:")
print(num)
print("modified array:")
print(num_modified)
print("2D array after addition:")
print(num_2d)
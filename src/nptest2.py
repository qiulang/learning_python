import numpy as np
a = np.array([[[1, 2, 3], [2, 1, 3]]])
b = np.array([[[2, 1, 1], [2, 4, 0]]])
b1 = b.reshape(1, 3, 2)
#c = a @ b
print(b1)
c = np.dot(a,b1)
print(c)
print("----")
d= a @ b1
print(d,d.shape)

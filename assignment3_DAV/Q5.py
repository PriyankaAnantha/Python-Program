import numpy as np
A = np.random.randint(1, 20, (3, 5))
B = np.random.randint(1, 20, (3, 5))
B_t=B.T

C=np.dot(A, B_t)
print(C)
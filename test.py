import numpy as np
import numpy.linalg as alg
ar=np.array([[36,1,13],[1,25,15],[13,15,-1]])
L=alg.cholesky(ar)
print("L:\n", L)
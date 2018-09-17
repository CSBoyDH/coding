import numpy as np
k=-5
x = np.asarray([[k,0,0,1],[1,2,0,-1],[k+2,-1,0,1],[2,1,3,k]])
print(np.linalg.det(x))
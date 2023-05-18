import numpy as np
from numpy.linalg import eig

if __name__ == '__main__':
    arr=np.array([[1, 2], [3, 4]])

    eigenvalues,eigenvectors=eig(arr)
    det = np.linalg.det(arr)
    print("eigenvalues:\n",eigenvalues)
    print("eigenvectors:\n",eigenvectors)
    print("determinant:",det)

    vec1=[1,2,3]
    vec2=[4,5,6]
    result = np.cross(vec1, vec2)
    print("cross product: ",result)

    mat_A=np.array([[1, 2,-2], [2, 1,-5],[1,-4,1]])
    mat_B=np.array([-15,-21,18])
    x = np.linalg.inv(mat_A).dot(mat_B)
    print("solution:",x)

    matrix = np.array([[1, 2], [3, 4]])

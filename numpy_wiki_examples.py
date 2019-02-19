#Array creation
import numpy as np
from numpy.random import rand
from numpy.linalg import solve, inv
import cv2

x = np.array([1, 2, 3])
print(x)

y = np.arange(10)  # like Python's range, but returns an array
print(y)

#Basic operations
a = np.array([1, 2, 3, 6])
b = np.linspace(0, 2, 4)  # create an array with four equally spaced points starting with 0 and ending with 2.
c=a-b
print(c)
print(a**2)

#Universal functions
a = np.linspace(-np.pi, np.pi, 100)
b = np.sin(a)
c=np.cos(a)
print(c)

#Linear algebra
a = np.array([[1, 2, 3], [3, 4, 6.7], [5, 9.0, 5]])
print(a.transpose())
print(inv(a))
b =  np.array([3, 2, 1])
print(solve(a,b))
c = rand(3, 3) * 20  # create a 3x3 random matrix of values within [0,1] scaled by 20
print(c)
print(np.dot(a, c))  # matrix multiplication
print(a @ c ) # Starting with Python 3.5 and NumPy 1.10

#Incorporation with OpenCV
r = np.reshape(np.arange(256*256)%256,(256,256))  # 256x256 pixel array with a horizontal gradient from 0 to 255 for the red color channel
g = np.zeros_like(r)  # array of same size and type as r but filled with 0s for the green color channel
b = r.T # transposed r will give a vertical gradient for the blue color channel
print(cv2.imwrite('gradients.png', np.dstack([b,g,r])))  # OpenCV images are interpreted as BGR, the depth-stacked array will be written to an 8bit RGB PNG-file called 'gradients.png'
        

#Nearest Neighbor Search - Iterative Python algorithm and vectorized NumPy version
# # # Pure iterative Python # # #
points = [[9,2,8],[4,7,2],[3,4,4],[5,6,9],[5,0,7],[8,2,7],[0,3,2],[7,3,0],[6,1,1],[2,9,6]]
qPoint = [4,5,3]
minIdx = -1
minDist = -1
for idx, point in enumerate(points):  # iterate over all points
    dist = sum([(dp-dq)**2 for dp,dq in zip(point,qPoint)])**0.5  # compute the euclidean distance for each point to q
    if dist < minDist or minDist < 0:  # if necessary, update minimum distance and index of the corresponding point
        minDist = dist
        minIdx = idx



print('Nearest point to q: ', points[minIdx])
# # # Equivalent NumPy vectorization # # #
points = np.array([[9,2,8],[4,7,2],[3,4,4],[5,6,9],[5,0,7],[8,2,7],[0,3,2],[7,3,0],[6,1,1],[2,9,6]])
qPoint = np.array([4,5,3])
minIdx = np.argmin(np.linalg.norm(points-qPoint,axis=1))  # compute all euclidean distances at once and return the index of the smallest one
print('Nearest point to q: ', points[minIdx])














































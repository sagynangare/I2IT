import numpy as np
import csv
f=open('winequality-red.csv', 'r')

wines=list(csv.reader(f, delimiter=";"))
#print(wines[:3])
qualities = [float(item[-1]) for item in wines[1:]]

#print(sum(qualities) / len(qualities))
a=np.array(wines)
#print(a.shape)

wines = np.genfromtxt("winequality-red.csv", delimiter=";", skip_header=1)
'''
Load data from a text file, with missing values handled as specified.
Each line past the first skip_header lines is split at the delimiter character
'''
#print(wines[2,3])
#print(wines[0:3])
#print(wines[0:3,3])
#print(wines[:,:])

earnings = [
            [
                [500,505,490],
                [810,450,678],
                [234,897,430],
                [560,1023,640]
            ],
            [
                [600,605,490],
                [345,900,1000],
                [780,730,710],
                [670,540,324]
            ]
          ]
earnings = np.array(earnings)
#print(earnings[1,0,0])
#print(earnings)
rand_array = np.random.rand(12)
#print(wines + rand_array)
#print(rand_array)

high_quality = wines[:,11] > 7
#print(wines[high_quality,:][:3,:])

high_quality_and_alcohol = (wines[:,10] > 10) & (wines[:,11] > 7)
#print(wines[high_quality_and_alcohol,10:])

high_quality_and_alcohol = (wines[:,10] > 10) & (wines[:,11] > 7)
wines[high_quality_and_alcohol,10:] = 20

#Reshaping NumPy Arrays
#print(np.transpose(wines).shape)
#print(wines.ravel())
'''
 the numpy.ravel function to turn an array into a one-dimensional
 representation. It will essentially flatten an array into a long sequence
 of values
'''
array_one = np.array(
    [
        [1, 2, 3, 4], 
        [5, 6, 7, 8]
    ]
)

#print(array_one.ravel())
#print(wines[1,:].reshape((2,6)))

# Combining NumPy Arrays
white_wines = np.genfromtxt("winequality-white.csv", delimiter=";", skip_header=1)
#print(white_wines.shape)

all_wines = np.vstack((wines, white_wines))
'''
vstack function to combine wines and white_wines
'''
print(all_wines.shape)
print(np.concatenate((wines, white_wines), axis=0))
'''
link=> https://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html#numpy.concatenate
 numpy.concatenate as a general purpose version of hstack and vstack.
 If we want to concatenate two arrays, we pass them into concatenate,
 then specify the axis keyword argument that we want to concatenate along.
 Concatenating along the first axis is similar to vstack, and concatenating
 along the second axis is similar to hstack
'''

















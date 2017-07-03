#-*- coding : utf-8 -*-

import numpy as np
import abc

'''
Kabsch algorithm is a method for calculating the optimal rotation matrix
that minimize the RMSD(Root Mean Square Deviation) between two paired set of points.
@ref : https://www.revolvy.com/main/index.php?s=Kabsch%20algorithm&item_type=topic
'''

'''
@brief  normalize abstract class
'''
class Normalize:
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def normalize(self, landmarks):
        pass

'''
@ Kabsch algorithm
'''
class kabsch2D(Normalize):
    def __init__(self):
        pass

    def normalize(self, landmarks):
        '''
        landmarks is M x D matrix (M is number of data, D is dimension)
        '''
        if type(landmarks) is np.matrix:

            # 1. translation (move to centroid)
            translated = landmarks - landmarks.mean(1)

            # 2. compute covariance matrix
            #cov = np.cov(np.transpose(translated))
            #print(cov.shape)

            #. compute optimal rotation matrix
            #u, s, v = np.linalg.svd(cov, full_matrices=True)
            #print(u.shape, s.shape, v.shape)
            #det = np.linalg.det(np.transpose(v)*np.transpose(u))
            #c = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, det]])
            #rot = np.transpose(v)*c*np.transpose(u)

            return translated
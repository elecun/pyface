# -*- coding:utf-8 -*-

import numpy as np

def rmse(v, w):
    '''
    Root Mean Square Error from two set of matrix v, w (equal to RMSD)
    :param v: vector or matrix
    :param w: vector or matrix
    :return: error value or vector
    '''
    if type(v) is np.matrix and type(w) is np.matrix:
        rmse = []
        for vn, wn in zip(v, w):
            mse = np.sum(np.subtract(np.array(vn), np.array(wn)))
            rmse.append(np.sqrt(mse/vn.shape[1]))
        return rmse
    elif type(v) is list and type(w) is list:
        rmse = 0.0
        return rmse
    return None


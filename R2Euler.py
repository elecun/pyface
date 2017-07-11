# -*- coding:utf-8 -*-

'''
3 X 3 Rotation Matrix to Euler Angle
R = Rz * Ry * Rx
'''

import math
import numpy as np
from os import listdir
from os.path import isfile, join
import re
import matplotlib.pyplot as plt

'''
Convert Radian to Degree
'''
def Rad2Deg(valuelist):
    return [value*180/math.pi for value in valuelist]

'''
Convert Rotation matrix to Euler Angles (Roll, Pitch, Yaw)
'''
def R2Euler(datafiles):

    EulerDeg = []

    # 1. load data from files
    for data in datafiles:
        f = open(data, "r")
        data = []
        for i in range(3):
            line_split = re.split(' |\n|\t', f.readline())
            data.append([float(d) for d in line_split[0:3]])
        R = np.matrix(data)
        f.close()

        q0 = math.sqrt(1 + R[0, 0] + R[1, 1] + R[2, 2]) / 2 #angle
        q1 = (R[2, 1] - R[1, 2]) / (4 * q0)
        q2 = (R[0, 2] - R[2, 0]) / (4 * q0)
        q3 = (R[1, 0] - R[0, 1]) / (4 * q0)

        # 2. if inverse matrix exists
        if (1 - np.linalg.det(R)) < 1e-5:
            yaw = math.asin(2 * (q0 * q2 + q1 * q3))
            pitch = math.atan2(2 * (q0 * q1 - q2 * q3), q0 * q0 - q1 * q1 - q2 * q2 + q3 * q3)
            roll = math.atan2(2 * (q0 * q3 - q1 * q2), q0 * q0 + q1 * q1 - q2 * q2 - q3 * q3)
            EulerDeg.append(Rad2Deg([roll, pitch, yaw]))
    return EulerDeg


if __name__ == "__main__":

    # 1. find files
    path = "H:/Experiment/OFace Head pose accuracy/dataset/"
    files = []
    filelist = [f for f in listdir(path) if isfile(join(path, f))]
    for file in filelist:
        if file.endswith(".txt"):
            files.append(join(path, file))

    print("Found ", len(files), " Files")

    # 2. Convert Rotation matrix to Euler Angle
    Euler = R2Euler(files)
    plt.plot(Euler)
    plt.show()
    plt.close()
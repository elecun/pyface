# -*- coding:utf-8 -*-

from pyFaceAlign.filereader import ptsReader
import pyFaceAlign.plot as plot
import matplotlib.pyplot as plt
from pyFaceAlign.normalization import kabsch2D

if __name__ == "__main__":
    # 1. read all pts file to create shape model
    filereader = ptsReader("./dataset")
    landmarks = filereader.read()
    print("Read ", landmarks.shape, " dimension of landmark data files.")

    # 2. display the raw landmark data
    plot.matplot2D(landmarks)

    # 3. normalization using kabsch
    kabsch = kabsch2D()
    normalized_landmarks = kabsch.normalize(landmarks)

    # 4. show the normalized landmark data
    plot.matplot2D(normalized_landmarks)

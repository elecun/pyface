# -*- coding:utf-8 -*-

from pyFaceAlign.filereader import ptsReader
import pyFaceAlign.plot as plot
from pyFaceAlign.normalization import kabsch2D
import numpy as np

if __name__ == "__main__":
    # 1. read all pts file to create shape model
    filereader = ptsReader("./dataset")
    landmarks = filereader.read()
    print("Read ", landmarks.shape, " dimension of landmark data files.")

    # 1.1 display the raw landmark data
    plot.landmark_plot2D(landmarks)

    # 2. normalization using kabsch
    normalize_process = kabsch2D()
    normalized_landmarks = normalize_process.normalize(landmarks)

    # 2.1 show the normalized landmark data
    plot.landmark_plot2D(normalized_landmarks)

#-*- coding : utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def landmark_plot2D(landmarks):
    '''
    :param landmarks: landmark matrix [x1;,,,xn;y1;...yn]
    :return: plot
    '''
    if type(landmarks) is np.matrix:
        plt.gca().invert_yaxis()
        num_dataset = int(landmarks.shape[0]/2)
        plt.plot(np.array(landmarks[:num_dataset]), np.array(landmarks[num_dataset:]), 'ro')
        plt.show()
        plt.close()

    elif type(landmarks) is list:
        plt.gca().invert_yaxis()  # y axis is needed to invert
        plt.plot([data[0] for data in landmarks], [data[1] for data in landmarks], 'ro')
        plt.show()
        plt.close()
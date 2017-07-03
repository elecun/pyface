# -*- coding : utf-8 -*-

from os import listdir
from os.path import isfile, join
import re
import numpy as np

class ptsReader:

    def __init__(self, path):
        self.path = path    # search path
        self.rawdata = []     # landmark data [[[x11...x1n],[y11...y1n]][[x21...x2n],[y21...y2n]]]
        self.files = []     # file list

    '''
    @brief  file files
    '''
    def __private_findfiles(self, ext):
        filelist = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        for file in filelist:
            if file.endswith(ext):
                self.files.append(join(self.path, file))

    '''
    @brief  read in matrix
    @param  matrix type [x1;...xn;y1;...yn;]
    '''
    def read(self):
        self.rawdata.clear()
        self.files.clear()

        self.__private_findfiles(".pts")

        x = []
        y = []
        for file in self.files:
            f = open(file, 'r')

            f.readline()
            info = re.split(':|\n| ', f.readline())
            f.readline()

            # read data
            data_x = []
            data_y = []
            for i in range(int(info[3])):
                line_split = re.split(' |\n|\t', f.readline())
                data_x.append(float(line_split[0]))
                data_y.append(float(line_split[1]))
            self.rawdata.append([data_x, data_y])
            x.append(data_x)
            y.append(data_y)

            f.close()

        return np.matrix(np.concatenate((x, y), axis=0))

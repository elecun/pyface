#-*- coding:utf-8 -*-

import sys
import struct

'''
@:param [x, y, z, pitch, yaw, roll]
'''

class biwiDataset:
    def __init__(self):
        pass

    '''
    @brief  find files
    '''
    def __private_findfiles(self, ext):
        filelist = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        for file in filelist:
            if file.endswith(ext):
                self.files.append(join(self.path, file))

    def readPose(filepath):
        binfile = open(filepath, 'rb')
        raw = binfile.read()
        data = []
        data.append(struct.unpack('f', raw[0:4])[0])
        data.append(struct.unpack('f', raw[4:8])[0])
        data.append(struct.unpack('f', raw[8:12])[0])
        data.append(struct.unpack('f', raw[12:16])[0])
        data.append(struct.unpack('f', raw[16:20])[0])
        data.append(struct.unpack('f', raw[20:24])[0])
        binfile.close()

        return data
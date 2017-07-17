#-*- coding:utf-8 -*-

import sys
import struct

'''
@:param [x, y, z, pitch, yaw, roll]
'''
def readPose(filepath):

    binfile = open(filepath, 'rb')
    raw = binfile.read()
    data = []
    if len(raw) is 24:
        data.append(struct.unpack('f', raw[0:4])[0])
        data.append(struct.unpack('f', raw[4:8])[0])
        data.append(struct.unpack('f', raw[8:12])[0])
        data.append(struct.unpack('f', raw[12:16])[0])
        data.append(struct.unpack('f', raw[16:20])[0])
        data.append(struct.unpack('f', raw[20:24])[0])
    else:
        print("Warning : ", filepath, "has wrong length of data")
    binfile.close()

    return data

#-*- coding:utf-8 -*-

import json
from util import filelist
import re

if __name__ == "__main__":

    datalist = filelist.findfiles("./dataset/exp/msapi", ".txt")
    for data in datalist:
        f = open(data, 'r')
        line = f.readline()

        segment = re.split('[|]', line)
        print(len(segment), segment[0])
        data = json.loads(line)
        f.close()
    # data = json.loads(str)
    # roll = float(data['faceAttributes']['headPose']['roll'])
    # pitch = float(data['faceAttributes']['headPose']['pitch'])
    # yaw = float(data['faceAttributes']['headPose']['yaw'])

    # print(roll, pitch, yaw)
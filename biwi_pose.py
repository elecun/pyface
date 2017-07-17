#-*- coding:utf-8 -*-

from util import filelist
from pyFaceAlign import biwi

if __name__=="__main__":

    # 1. find all files in the path
    datalist = filelist.findfiles("./dataset/db_annotations", ".bin")

    # 2. write pose data from the biwi head pose data files
    f = open("biwi.txt", 'w')
    f.writelines("filename\tx\ty\tz\tpitch\tyaw\troll\n")
    for data in datalist:
        pos = biwi.readPose(data)
        f.write(data)
        f.write(''.join('\t'+str(p) for p in pos))
        f.write('\n')
    f.close()

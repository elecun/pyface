#-*- coding:utf-8 -*-

from pyFaceAlign import biwi
from util import filelist

if __name__=="__main__":
    datalist = filelist.findfiles("./dataset/db_annotations", ".bin")
    print(len(datalist))
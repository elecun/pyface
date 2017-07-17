# -*- coding : utf-8 -*-

import os

'''
@brief  find all files
'''
def findfiles(path, ext):
    files = []
    subdirs = [path+"/"+name for name in os.listdir(path)]

    for subdir in subdirs:
        files.append([subdir+"/"+f for f in os.listdir(subdir) if os.path.isfile(os.path.join(subdir, f))])
        print(files)
    print(len(files))
    # for file in filelist:
    #     if file.endswith(ext):
    #         files.append(join(path, file))
    #
    # return files

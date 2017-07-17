# -*- coding : utf-8 -*-

import os

'''
@brief  find all files
'''
def findfiles(path, ext):
    all_files = []
    subdirs = [path+"/"+name for name in os.listdir(path)]
    for subdir in subdirs:
        try:
            files = [subdir+"/"+f for f in os.listdir(subdir) if os.path.isfile(os.path.join(subdir, f)) and f.endswith(ext)]
            all_files += files
        except NotADirectoryError:
            pass
    return all_files


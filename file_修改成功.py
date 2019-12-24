# -*- coding: UTF-8 -*-
import os
import sys
#搞定了修改的功能
with open('D:/CMC.cfg','r')as f1,open('D:/CMC1.cfg', 'w') as f2:
    for line in f1:
        if "[Saving user: root]" in line:
            line = line.replace('[Saving user: root]','[Saving user: admin]')
        f2.write(line)
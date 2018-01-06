#!/usr/bin/env python  
# -*- coding:utf-8 -*-    
# @Time    : 2018/1/6  
# @Author  : sijt
#  python中有关操作系统的代码


from io import StringIO
from io import BytesIO
import os

f = StringIO()
f.write('beauty')
print(f.getvalue())
b = BytesIO()
b.write('美人'.encode('utf-8'))
print(b.getvalue())
print(os.name)
print(os.environ)

# 查看当前目录的绝对路径:
os.path.abspath('.')
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('G:\python', 'testdir')
# 然后创建一个目录:
os.mkdir(r'G:\python\testdir')
# 删掉一个目录:
os.rmdir(r'G:\python\testdir')

print(os.path.split('G:\python\PythonProject\SystemOS.py'))  # 可以直接获取文件的文件名
print(os.path.splitext('G:\python\PythonProject\SystemOS.py'))  # 可以直接获取文件的拓展名










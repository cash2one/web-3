# coding:utf-8
import os
os.system('net stop Apache2.2')
os.system('pause')
os.system('net start Apache2.2') # 最好加上版本号2.2

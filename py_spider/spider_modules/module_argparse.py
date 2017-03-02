# -*- coding: utf-8 -*-
# @Date:   2017-03-02 10:21:49
# @Last Modified time: 2017-03-02 14:17:07
"""
argparse————python命令行解析工具
python module_argparse.py -s ***
Namespace(s=123)

add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
name or flags————命令行参数名或者选项（如-p、--port），命令行参数如果没给定，且没有设置defualt，则出错；但是如果是选项的话，则设置为None
nargs—————命令行参数的个数，一般使用通配符表示（'?'：一个，'*'：0到多个，'+'：至少一个）
default————默认值
type————参数的类型，默认是string，还有float、int等
help————和ArgumentParser方法中的参数作用相似，出现的场合也一致
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-s', help='a num', type=int, default=1)
args = parser.parse_args()
print args
print args.s

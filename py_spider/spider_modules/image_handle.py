# -*- coding: utf-8 -*-
# @Date:   2017-03-08 14:29:02
# @Last Modified time: 2017-03-08 19:56:06
"""
安装pytesseract或者pyocr
依赖PIL——————————————图像处理库—————————————http://www.pythonware.com/products/pil/
依赖tesseract-ocr————google的ocr识别引擎————https://sourceforge.net/projects/tesseract-ocr-alt/files/
pip install pytesseract
pip install pyocr
添加path: C:\Program Files (x86)\Tesseract-OCR，重启
"""
import os
import pyocr
import pytesseract
from PIL import Image, ImageEnhance

# work_path = os.path.abspath(".")          # 启动文件工作目录（可能会变）
file_path = os.path.dirname(__file__)     # 文件目录
parent_path = os.path.join(file_path, 'test')


def reduce_noisy_point(image):
    """
    图片降噪
    去除背景、干扰线、干扰像素等不需要的信息，只剩下需要识别的文字，让图片变成2进制点阵最好
    把彩色图像转化为灰度图像。RBG转化到HSI彩色空间
    """
    result = image.convert('L')
    # result.show()
    return result


def two_poles(image):
    """
    二值化处理
    根据阈值选取的不同，分为固定阈值和自适应阈值
    固定阈值
    把大于临界灰度值（140）的像素灰度设为灰度极大值（一般设置为1）
    把小于临界灰度值（140）的像素灰度设为灰度极小值（一般设置为0）
    生成一张查找表，再调用point()进行映射
    """
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    result = image.point(table, '1')
    # result.show()
    return result


def strengthen(image):
    """
    图像增强
    调整对比度、亮度、色平衡和锐利度
    """
    enh = ImageEnhance.Contrast(image)
    result = enh.enhance(1.0)
    # result.show("30% more contrast")
    return result


def read_image(image):
    """
    # 使用pytesseract或者pyocr识别图片
    try:
        vcode = pytesseract.image_to_string(image)
        p.put({
            'keyid': p._request._ext['keyid'],
            'phone': vcode
        })
    except Exception, e:
        print e
    """
    tools = pyocr.get_available_tools()[:]
    if len(tools) == 0:
        print("No OCR tool found")
    else:
        vcode = tools[0].image_to_string(image, lang='eng')
        return vcode


file_names = os.listdir(parent_path)

if __name__ == "__main__":
    for i in file_names:
        file_name = os.path.join(parent_path, i)
        image = Image.open(file_name)
        result = two_poles(reduce_noisy_point(image))
        new_file_name = os.path.join(parent_path, 'new_' + i)
        result.save(new_file_name)
        new_image = Image.open(new_file_name)
        print read_image(new_image)

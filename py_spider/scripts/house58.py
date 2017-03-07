# coding: utf-8
__author__ = 'zdd'
"""
pytesseract或者pyocr

依赖PIL（图像处理库）、tesseract-ocr（google的ocr识别引擎）
http://www.pythonware.com/products/pil/
https://sourceforge.net/projects/tesseract-ocr-alt/files/

pip install pytesseract
pip install pyocr
添加path: C:\Program Files (x86)\Tesseract-OCR，修改pytesseract.py tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
Python脚本文件和读取的验证码图片都要保存在"D:\P\Python\Lib\site-packages\pytesseract"
"""
import os
import pyocr
import pytesseract
from PIL import Image


filepath = os.path.abspath(".")
# filename = os.path.join(filepath, "scripts\images\showphone.gif")
filename = os.path.join(filepath, "scripts\images\showphone.png")


starturl = [
    "http://bj.58.com/zhaozu/0/pve_1092_0/?PGTID=0d30000d-0000-1ce8-6db0-e86136a47008&ClickID=1"]
'''
0，个人
pve_1092_0，出租
'''

districts = [
    'chaoyang',
    'haidian',
    'dongcheng',
    'xicheng',
    'chongwen',
    'xuanwu',
    'fengtai',
    'tongzhouqu',
    'shijingshan',
    'fangshan',
    'changping',
    'daxing',
    'shunyi',
    'miyun',
    'huairou',
    'yanqing',
    'pinggu',
    'mentougou',
    'bjyanjiao',
    'beijingzhoubian'
]


def process(p):
    if p.isDefaultLevel():
        for i in districts:
            u = 'http://bj.58.com/'
            u += i
            u += '/zhaozu/0/pve_1092_0/?PGTID=0d30000d-0000-1ce8-6db0-e86136a47008&ClickID=1'
            p.addurl(u, level="qishiye")

    elif p.isLevel("qishiye"):
        xpath = p.HtmlSelector().xpath
        start_urls = xpath("//div[@class='subarea']/a/@href").textall()
        i = 0
        for url in start_urls:
            if i < 3:
                p.addurl(url, level="liebiaoye")
            i += 1

    elif p.isLevel("liebiaoye"):
        xpath = p.HtmlSelector().xpath
        list_urls = xpath("//div[@class='pager']/a/@href").textall()
        for url in list_urls:
            p.addurl(url, level="liebiaoye")
        detail_urls = xpath(
            "//table[@class='tbimg']/tr/td[@class='t']/a/@href").textall()
        for url in detail_urls:
            if '/haozu' in url:
                continue
            p.addurl(url, level="xiangqingye")

    elif p.isLevel("xiangqingye"):
        xpath = p.HtmlSelector().xpath
        keyid = p.TextSelector(p._request._url).re("(\d+)", 1).text()
        district = xpath("//ul[@class='info']/li[1]/a[1]/text()").text()
        circle = xpath("//ul[@class='info']/li[1]/a[2]/text()").text()
        office_name = xpath("//ul[@class='info']/li[2]/text()").text()
        address = xpath(
            "//ul[@class='info']/li[3]/text()").text().replace(' ', '').strip()
        type = xpath("//ul[@class='info']/li[4]/text()").text().strip()
        area = xpath("//ul[@class='info']/li[5]/text()").text()
        price = xpath("//ul[@class='info']/li[6]/em/text()").text()
        unit = xpath("//ul[@class='info']/li[6]/text()").text().strip()
        script = xpath(
            "//div[@id='newuser']/following-sibling::script[1]/text()").text()
        user = p.TextSelector(script).re(
            "username:'.+'", 0).text().strip("username:'").strip("'")
        company = xpath(
            "//div[@id='newuser']/ul[@class='userinfo']/li[5]/label/text()").text()
        p.put({
            'keyid': keyid,
            'district': district,
            'circle': circle,
            'office_name': office_name,
            'address': address,
            'type': type,
            'area': area,
            'price': price,
            'unit': unit,
            'user': user,
            'company': company
        })
        phone_str = xpath("//span[@id='t_phone']/text()").text().strip()
        phone = p.TextSelector(phone_str).re("^\d+$", 0).text()
        if phone:
            p.put({
                'keyid': keyid,
                'phone': phone
            })
        else:
            phone_script = xpath("//span[@id='t_phone']/script/text()").text()
            phone_url = p.TextSelector(phone_script).re(
                "src='.+'", 0).text().strip("src='").strip("'")
            p.addurl(phone_url, level="get_image", ext={'keyid': keyid})

    elif p.isLevel("get_image"):
        response = p._response
        f = open(filename, 'wb')
        f.write(response.content)
        f.close()

        image = Image.open(filename)
        """
        vcode = pytesseract.image_to_string(image)
        """
        tools = pyocr.get_available_tools()[:]
        if len(tools) == 0:
            print("No OCR tool found")
        else:
            vcode = tools[0].image_to_string(image, lang='eng')
            p.put({
                'keyid': p._request._ext['keyid'],
                'phone': vcode
            })

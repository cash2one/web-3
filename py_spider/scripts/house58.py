# coding: utf-8
__author__ = 'zdd'
import os
import pyocr
import pytesseract
from PIL import Image


file_path = os.path.dirname(__file__)


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
        # for i in districts:
        i = 'beijingzhoubian'
        u = 'http://bj.58.com/'
        u += i
        u += '/zhaozu/0/pve_1092_0/?PGTID=0d30000d-0000-1ce8-6db0-e86136a47008&ClickID=1'
        p.addurl(u, level="qishiye")

    elif p.isLevel("qishiye"):
        xpath = p.HtmlSelector().xpath
        start_urls = xpath("//div[@class='subarea']/a/@href").textall()
        i = 0
        for url in start_urls:
            p.addurl(url, level="liebiaoye")

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
        script1 = xpath("//script[1]/text()").text()
        company_info = p.TextSelector(script1).re(
            "_trackParams:\[.+(I\":10276,\"V\":\"[^\"]+).+\]", 0).text()  # [^..]，正则取反
        company = company_info.strip('I":10276,"V":"')
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
        phone = xpath("//span[@id='t_phone']/text()").text().strip()
        if phone:
            p.put({
                'keyid': keyid,
                'phone': phone
            })
        else:
            phone_script = xpath("//span[@id='t_phone']/script/text()").text()
            phone_url = p.TextSelector(phone_script).re(
                "src='.+'", 0).text().strip("src='").strip("'")
            p.put({
                'keyid': keyid,
                'phone_url': phone_url
            })
            p.addurl(phone_url, level="get_image", ext={'keyid': keyid})

    elif p.isLevel("get_image"):
        # file_name = os.path.join(work_path, "images", "showphone.png")
        # 单线程条件下可以反复读写同一文件
        # 多进程+多线程条件下，必须每次生成新文件
        name = str(p._request._ext['keyid']) + '.png'
        file_name = os.path.join(file_path, 'test_images', name)
        response = p._response
        f = open(file_name, 'wb')
        f.write(response.content)
        f.close()

        image = Image.open(file_name)
        tools = pyocr.get_available_tools()[:]
        if len(tools) == 0:
            print("No OCR tool found")
        else:
            vcode = tools[0].image_to_string(image, lang='eng')
            p.put({
                'keyid': p._request._ext['keyid'],
                'phone': vcode
            })

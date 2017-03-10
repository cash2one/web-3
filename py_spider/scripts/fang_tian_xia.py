# coding: utf-8
__author__ = 'zdd'
# import chardet


site = {"encoding": "gb2312"}
starturl = []
districts = [
    "a01",
    "a00",
    "a02",
    "a03",
    "a06",
    "a07",
    "a0585",
    "a011",
    "a010",
    "a012",
    "a09",
    "a08",
    "a013",
    "a016",
    "a014",
    "a015",
    "a0987",
    "a011817"
]
# for i in districts:
i = "a01"
if i:
    url = "http://office.fang.com/zu/house-"
    url += i
    url += "/a21/"
    starturl.append(url)
sh_districts = [
    "a025",
    "a019",
    "a020",
    "a027",
    "a028",
    "a024",
    "a021",
    "a018",
    "a023",
    "a022",
    "a026",
    "a029",
    "a030",
    "a0586",
    "a031",
    "a032",
    "a035",
    "a0996",
    "a01046"
]

# for i in sh_districts:
i = "a025"
if i:
    url = "http://office.sh.fang.com/zu/house-"
    url += i
    url += "/a21/"
    starturl.append(url)


def process(p):
    import BeautifulSoup
    if p.isDefaultLevel():
        """
        使用beautiful解析不规则html（标签不闭合）
        """
        soup = BeautifulSoup.BeautifulSoup(p._text)
        # 生成BeautifulSoup.Tag对象list
        tag = soup.findAll(name="div", attrs={"id": "esf_B03_04"})
        if len(tag) >= 1:
            all = tag[0].findAll('a')
            for a in all:
                url = a.get("href")
                if url:
                    p.addurl(url, level="liebiaoye")

    elif p.isLevel("liebiaoye"):
        soup = BeautifulSoup.BeautifulSoup(p._text)
        tags = soup.findAll(name='p', attrs={'class': "title"})
        for tag in tags:
            detail_url = tag.a['href']
            p.addurl(detail_url, level="xiangqingye")

    elif p.isLevel("xiangqingye"):
        text = p.HtmlSelector().xpath("//div[@class='inforTxt']").text()
        xpath = p.HtmlSelector(text=text).xpath

        month_price = xpath("//dl[1]/dt[1]/span[@class='red20b']/text()").text().strip()
        month_unit = xpath("///dl[1]//dt[1]/span[@class='black']/text()").text().strip()
        price = xpath("///dl[1]/dt[2]/span[1]/text()").text().strip()
        unit = xpath("///dl[1]/dt[2]/span[2]/text()").text().strip()
        area = xpath("//dl[1]/dd[1]/text()").text().replace("出租面积：", "").strip().replace("�", "㎡")
        phone = xpath("//div[@class='phone_top']/span/label/text()").text().strip()
        office_name = xpath("//dl[2]/dt[1]").text().split("(")[0].strip().split(" ")[-1]
        if '</a>' in office_name:
            office_name = xpath("//dl[2]/dt[1]/a[1]/text()").text().strip()
        district = xpath("//dl[2]/dt[1]/a[2]/text()").text().strip()
        business_circle = xpath("//dl[2]/dt[1]/a[3]/text()").text().strip()
        address = xpath("//dl[2]/dt[2]/a[1]/text()").text().strip()
        if not address:
            address = xpath("//dl[2]/dt[2]").text().strip("<dt>/").strip().split(" ")[-1]

        floor = xpath("//dl[2]/dd[1]/text()").text().strip()
        fee = xpath("//dl[2]/dd[2]/text()").text().strip()

        fee_company = xpath("//dl[2]/dd[3]").text().strip("<dd>/").strip().split(" ")[-1]
        office_level = xpath("//dl[2]/dd[4]").text().strip("<dd>/").strip().split(" ")[-1]
        zhuangxiu = xpath("//dl[2]/dd[5]").text().strip("<dd>/").strip().split(">")[-1].replace("\r\n", "").replace(" ", "")
        type = xpath("//dl[2]/dd[6]").text().strip("<dd>/").strip().split(" ")[-1]

        keyid = p.TextSelector(p._request._url).re("(\d+)", 1).text()
        if 'http://office.sh.fang.com/' in p._request._url:
            city = "上海"
        else:
            city = "北京"
        p.put({
            "keyid": keyid,
            "city": city,
            "month_price": month_price,
            "month_unit": month_unit,
            "price": price,
            "unit": unit,
            "area": area,
            "phone": phone,
            "office_name": office_name,
            "district": district,
            "business_circle": business_circle,
            "address": address,
            "floor": floor,
            "fee": fee,
            "fee_company": fee_company,
            "office_level": office_level,
            "zhuangxiu": zhuangxiu,
            "type": type
        })

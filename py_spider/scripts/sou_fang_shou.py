# coding: utf-8
import logging

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='error.log',
    filemode='a')

site = {"encoding": "gb2312"}

starturl = [
    "http://office.fang.com/shou/house/k2100/",
    "http://office.fang.com/shou/house/d230000-j2100-k2200/",
    "http://office.fang.com/shou/house/c230000-d240000-j2100-k2200/",
    "http://office.fang.com/shou/house/c240000-d250000-j2100-k2200/",
    "http://office.fang.com/shou/house/c250000-j2100-k2200/",
    "http://office.fang.com/shou/house/d240000-j2200-k2300/",
    "http://office.fang.com/shou/house/c240000-j2200-k2300/",
    "http://office.fang.com/shou/house/d240000-j2300-k2500/",
    "http://office.fang.com/shou/house/c240000-j2300-k2500/",
    "http://office.fang.com/shou/house/d240000-j2500-k2800/",
    "http://office.fang.com/shou/house/c240000-j2500-k2800/",
    "http://office.fang.com/shou/house/j2800-k21000/",
    "http://office.fang.com/shou/house/d240000-j21000-k22000/",
    "http://office.fang.com/shou/house/c240000-j21000-k22000/",
    "http://office.fang.com/shou/house/j22000/"
]


def process(p):
    if p.isDefaultLevel():
        xpath = p.HtmlSelector().xpath
        list_urls = xpath("//div[@class='fanye gray6']/a/@href").textall()
        for url in list_urls:
            p.addurl(url, level="")

        dds = xpath(
            "//div[@class='houseList']/dl/dd[@class='info rel floatr']").textall()
        for dd in dds:
            url = p.HtmlSelector(text=dd).xpath(
                "//p[@class='title']/a/@href").text()
            contact_name = p.HtmlSelector(text=dd).xpath(
                "//span[@class='marr7']/text()").text()
            if not contact_name:
                contact_name = p.HtmlSelector(text=dd).xpath(
                    "//a[@class='marr7']/text()").text()
            xingzhi = "个人" if "个人" in contact_name else "中介"
            name = p.HtmlSelector(text=dd).xpath(
                "//span[@class='spName']/text()").text()
            ext = {
                'contact_name': contact_name,
                'xingzhi': xingzhi,
                'name': name
            }
            p.addurl(url, level="xiangqingye", ext=ext)

    elif p.isLevel("xiangqingye"):
        text = p.HtmlSelector().xpath("//div[@class='inforTxt']").text()
        xpath = p.HtmlSelector(text=text).xpath

        if 'http://office.sh.fang.com/' in p.getUrl():
            city = "sh"
        else:
            city = "bj"
        price_month = xpath(
            "//dl[1]/dt[1]/span[@class='red20b']/text()").text().strip()
        wan = xpath("//dl[1]/dt[1]/span[@class='black']/text()").text().strip()
        if wan:
            price_month *= 10000
        price_text = xpath("//dl[1]/dt[1]").text()
        price = p.HtmlSelector(text=price_text).wildcard('(*元/*)', 0).text()

        area = filter(str.isdigit, xpath(
            "//dl[1]/dd[1]/span/text()").text().encode("utf-8"))
        if not area:
            area = filter(str.isdigit, xpath(
                "//dl[1]/dd[1]/text()").text().encode("utf-8"))
        span = p.HtmlSelector().wildcard('装*修：</span>*</dd>', 1).text()
        if u'精装' in span:
            zx = u'精装'
        elif u'简装' in span:
            zx = u'简装'
        elif u'毛坯' in span:
            zx = u'毛坯'
        elif u'简单' in span:
            zx = u'简装'
        else:
            zx = u'不详'
        kefenge = u'否' if u'不可分割' in span else u'是'

        phone = xpath(
            "//div[@class='phone_top']/span/label/text()").text().strip()
        ceng = xpath("//dl[2]/dd[1]/text()").textall()[-1].split('(')[0]

        _wyf = p.HtmlSelector().wildcard("物 业 费：*月", 0).text()
        wyf_list = _wyf.split('.')
        wyf_int = filter(str.isdigit, wyf_list[0].encode("utf-8"))
        wyf_float = filter(str.isdigit, wyf_list[1].encode(
            "utf-8")) if len(wyf_list) > 1 else '0'
        if u"平米" in _wyf:
            wyf = '%.2f' % (float(wyf_int + '.' + wyf_float) * float(area))
        else:
            wyf = '%.2f' % float(wyf_int + '.' + wyf_float)
        haswyf = '否' if float(wyf) == 0 else '是'

        house_no = keyid = p.TextSelector(p.getUrl()).re("(\d+)", 1).text()

        public_time = p.HtmlSelector().xpath(
            "//div[@class='title']/p[@class='gray9']/text()").text().split("：")[-1].strip("( ")
        update_time = p.HtmlSelector().xpath(
            "//div[@class='title']/p[@class='gray9']/span[@id='Time']/text()").text().strip(u"更新").strip()
        description = p.HtmlSelector().xpath(
            "//div[@class='describe mt10']").text()

        name = p.getExt("name")
        xingzhi = p.getExt("xingzhi")
        contact_name = p.getExt("contact_name")

        result = {
            "keyid": keyid,
            "city": city,
            "price_month": price_month,
            "price": price,
            "area": area,
            "zx": zx,
            "haswyf": haswyf,
            "wyf": wyf,
            "house_no": house_no,
            "public_time": public_time,
            "update_time": update_time,
            "description": description,
            "phone": phone,
            "ceng": ceng,
            "name": name,
            "xingzhi": xingzhi,
            "contact_name": contact_name,
            "kefenge": kefenge,
        }
        for key, value in result.iteritems():
            if not value:
                logging.error('[%s, %s]' % (p.getUrl(), key))

        p.put(result)

# coding: utf-8
import time

__author__ = 'zdd'
start_url = ["http://bj.58.com/job/?utm_source=market&spm=b-31580022738699-me-f-824.bdpz_biaoti&key="]
hangye = range(244, 288)
hangye.append(3527)
xingzhi = range(1476, 1486)
# xueli = range(2, 9)
# jingyan = range(4, 10)
minxinzi = ['0_999', '1000_1999', '2000_2999', '3000_4999', '5000_7999', '8000_11999', '12000_19999', '20000_24999', '25000_999999']


def process(p):
    if p.isDefaultLevel():
        for i in hangye:
            for j in xingzhi:
                for m in minxinzi:
                    u = "http://bj.58.com/job/"

                    u += "pve_5363_"
                    u += str(i)

                    u += "_pve_5754_"
                    u += str(j)

                    u += "/?utm_source=market&spm=b-31580022738699-me-f-824.bdpz_biaoti&key="

                    u += "&minxinzi="
                    u += m
                    p.addurl(u, level="liebiaoye")

        xpath = p.HtmlSelector().xpath
        url = xpath("//div[@class='pager']/a[1]/@href").text()
        p.addurl(url, level="liebiaoye")

    elif p.isLevel("liebiaoye"):
        xpath = p.HtmlSelector().xpath
        companys_address = xpath("//dd[@class='w46']/following-sibling::dd[@class='w96']/text()").textall()  # 公司地址
        issuedate = xpath("//dd[@class='w46']/following-sibling::dd[@class='w68']/text()").textall()         # 发布日期
        page = xpath("//div[@class='pager']/strong/span/text()").text()                                      # 页数,【可选】

        urls_liebiaoye = xpath("//div[@class='pager']/a/@href").textall()
        for u in urls_liebiaoye:
            p.addurl(u, level="liebiaoye")

        urls_gongsi = xpath("//dd[@class='w46']/following-sibling::dd[@class='w271']/a/@href").textall()
        urls_detail_list = xpath("//dd[@class='w46']/following-sibling::dt[1]/a/@href").textall()
        for i, url in enumerate(urls_detail_list):
            keyid = p.TextSelector(url).re("(\d+)", 1).text()
            # if i in range(10, 25):  # 小规模测试
            ext = {
                'pageurl': p._request._url,
                'company_address': companys_address[i],
                'issuedate': issuedate[i],
                'page': page,
                'keyid': keyid,
                'url_gongsi': urls_gongsi[i]
            }
            p.addurl(url, level="xiangqingye", ext=ext)

    elif p.isLevel("xiangqingye"):
        page = p._request._ext['page']                                                                      # 页数,【可选】
        xpath = p.HtmlSelector().xpath
        pageurl = p._request._ext['pageurl']                                                                # 帖子所在的列表页url
        issuedate = p._request._ext['issuedate']                                                            # 发布日期
        jobdetilurl = p._request._url                                                                       # 招聘详情页url
        company_address = p._request._ext['company_address']                                                # 公司地址
        keyid = p._request._ext['keyid']                                                                    # 招聘帖子id，即keyid
        if jobdetilurl:

            position = xpath("//div[@class='headConLeft']/h1/text()").text()                                # 招聘名称
            monthprice = xpath("//div[@class='xq']/ul/li[1]//span[@class='salaNum']/strong/text()").text()  # 月薪
            work_address = xpath("//div[@class='xq']/ul/li[3]/span[2]/text()").text()                       # 招聘岗位的工作地址
            trade = xpath("//div[@class='compMsg clearfix']/ul/li[1]/a/text()").text()                      # 行业类别
            company_type = xpath("//div[@class='compMsg clearfix']/ul/li[2]/text()").text()                 # 公司性质
            staff_size = xpath("//div[@class='compMsg clearfix']/ul/li[3]/text()").text()                   # 公司规模

            company = xpath("//a[@class='companyName']/text()").text()                                      # 公司名称
            company = company if company else xpath("//div[@class='compTitle']/a/text()").text()
            companydetilurl = xpath("//a[@class='companyName']/@href").text()
            companydetilurl = companydetilurl if companydetilurl else xpath("//div[@class='compTitle']/a/@href").text()

            if company:
                get_time = int(time.time())                                                                     # 抓取时间
                ext = {
                    'keyid': keyid,
                    'companydetilurl': companydetilurl,
                }
                p.put({
                    'jobdetilurl': jobdetilurl,
                    'page': page,
                    'pageurl': pageurl,
                    'issuedate': issuedate,
                    'company_address': company_address,
                    'keyid': keyid,
                    'position': position,
                    'company': company,
                    'monthprice': monthprice,
                    'work_address': work_address,
                    'trade': trade,
                    'company_type': company_type,
                    'staff_size': staff_size,
                    'companydetilurl': companydetilurl,
                    'get_time': get_time,
                })
                url_gongsi = p._request._ext['url_gongsi']
                p.addurl(url_gongsi, level="gongsi", ext=ext)

    elif p.isLevel("gongsi"):
        xpath = p.HtmlSelector().xpath
        website = xpath("//ul[@class='basicMsgListo basicMsgList clearfix']/li[6]/a/@href").text()  # 公司网站，即公司自己的网站
        website = website if website else p._request._url
        # form_data = xpath("//a[@class='businessName fl']/@title").text()
        # registration_address = ""  # 注册地址,【可选】
        # keytype = ""               # 关键词,【可选】
        # registration_time = ""     # 注册时间,【可选】
        p.put({
            'keyid': p._request._ext['keyid'],
            'website': website,
        })

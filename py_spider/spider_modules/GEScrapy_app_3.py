# coding:utf-8
from routing import Routing, Rule, Segment, RoutingEncoder
import requests
import json
import xmltodict
import logging
#from lxml.html.soupparser import  fromstring


METHOD = 'GE'


class GEScrapy_App():

    def __init__(self):
        self.session = requests.session()

    def requestSelectPage(self, dptairport, arrairport, fromdate, retdate, adults, child, infants):
        judgment_dpt = dptairport
        judgment_arr = arrairport

        self.session.headers.update({
            "Host": "appfun.tna.com.tw:8080",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "text/xml; charset=utf-8",
            "Accept-Language": "zh-cn",
            "SOAPAction": "http://www.tna.com.tw/getXMLData",
            "Cookie": "PHPSESSID=i772r8q7abekv954kps4rbeh56",
            "User-Agent": "TransAsia/2.44 CFNetwork/758.1.6 Darwin/15.0.0",
            # "Pragma": "no-cache",
            # "Cache-Control": "no-cache"
        })
        data1 = '''<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><getXMLData xmlns="http://www.tna.com.tw/"><xmlData>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf8&quot;?&gt;
&lt;Collection&gt;
    &lt;CMD&gt;&lt;![CDATA[INQ]]&gt;&lt;/CMD&gt;
    &lt;PLATFORM&gt;&lt;![CDATA[iPhone]]&gt;&lt;/PLATFORM&gt;
    &lt;VERSION&gt;&lt;![CDATA[2.44]]&gt;&lt;/VERSION&gt;
    &lt;DepartureDateTime&gt;&lt;![CDATA[%s]]&gt;&lt;/DepartureDateTime&gt;
    &lt;OriginLocation&gt;&lt;![CDATA[%s]]&gt;&lt;/OriginLocation&gt;
    &lt;DestinationLocation&gt;&lt;![CDATA[%s]]&gt;&lt;/DestinationLocation&gt;
    &lt;Back&gt;
        &lt;DepartureDateTime&gt;&lt;![CDATA[%s]]&gt;&lt;/DepartureDateTime&gt;
        &lt;OriginLocation&gt;&lt;![CDATA[%s]]&gt;&lt;/OriginLocation&gt;
        &lt;DestinationLocation&gt;&lt;![CDATA[%s]]&gt;&lt;/DestinationLocation&gt;
    &lt;/Back&gt;
    &lt;Condition&gt;
        &lt;PaxTypes&gt;
            &lt;PaxType
            id=&quot;ADT&quot;
            /&gt;
            &lt;PaxType
            id=&quot;CNN&quot;
            /&gt;
            &lt;PaxType
            id=&quot;SRC&quot;
            /&gt;
            &lt;PaxType
            id=&quot;DIS&quot;
            /&gt;
        &lt;/PaxTypes&gt;
        &lt;Seats
        Quantity=&quot;4&quot;
        /&gt;
    &lt;/Condition&gt;
&lt;/Collection&gt;</xmlData></getXMLData></soap:Body></soap:Envelope>''' % (fromdate, dptairport, arrairport, retdate, arrairport, dptairport)
        data2 = """<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><getXMLData xmlns="http://www.tna.com.tw/"><xmlData>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf8&quot;?&gt;
                &lt;Collection&gt;
                &lt;CMD&gt;&lt;![CDATA[INQ]]&gt;&lt;/CMD&gt;
                &lt;PLATFORM&gt;&lt;![CDATA[iPhone]]&gt;&lt;/PLATFORM&gt;
                &lt;VERSION&gt;&lt;![CDATA[2.44]]&gt;&lt;/VERSION&gt;
                &lt;IDCD&gt;&lt;![CDATA[I]]&gt;&lt;/IDCD&gt;
                &lt;FLYCLSCD&gt;&lt;![CDATA[Y]]&gt;&lt;/FLYCLSCD&gt;
                &lt;DepartureDateTime&gt;&lt;![CDATA[%s]]&gt;&lt;/DepartureDateTime&gt;
                &lt;OriginLocation&gt;&lt;![CDATA[%s]]&gt;&lt;/OriginLocation&gt;
                &lt;DestinationLocation&gt;&lt;![CDATA[%s]]&gt;&lt;/DestinationLocation&gt;
                &lt;Back&gt;
                    &lt;DepartureDateTime&gt;&lt;![CDATA[%s]]&gt;&lt;/DepartureDateTime&gt;
                    &lt;OriginLocation&gt;&lt;![CDATA[%s]]&gt;&lt;/OriginLocation&gt;
                    &lt;DestinationLocation&gt;&lt;![CDATA[%s]]&gt;&lt;/DestinationLocation&gt;
                &lt;/Back&gt;
                &lt;Condition&gt;
                    &lt;PaxTypes&gt;
                        &lt;PaxType
                        id=&quot;ADT&quot;
                        /&gt;
                    &lt;/PaxTypes&gt;
                    &lt;Seats
                    Quantity=&quot;1&quot;
                    /&gt;
                &lt;/Condition&gt;
            &lt;/Collection&gt;</xmlData></getXMLData></soap:Body></soap:Envelope>""" % (fromdate, dptairport, arrairport, retdate, arrairport, dptairport)

        Airports = ["TSA", "RMQ", "MZG", "KNH", "KHH", "HUN"]
        for i in Airports:
            if arrairport == i:
                response = self.session.post(
                    "http://appfun.tna.com.tw:8080/TNA/HM/HMWS34.asmx?op=getXMLData", data=data1, verify=False)
            else:
                response = self.session.post(
                    "http://appfun.tna.com.tw:8080/TNA/HM/HMWS36.asmx?op=getXMLData", data=data2, verify=False)

            root = xmltodict.parse(response.content)
            print root
            #broot= root["soap:Envelope"]["soap:Body"]["getXMLDataResponse"]["getXMLDataResult"]
            #contents = xmltodict.parse(broot)
            #content= json.dumps(contents)
            # print content
            # null='null'
            #my_dicts = contents['Collection']['PRICEINFOLIST']['AirItinerary']
            #judgment_msg = contents['Collection']["MSG"]
            # print judgment_msg
            # resultlist=[]
            #
            # if judgment_msg == 'OK':                                           #判断获取成功
            #    logging.info('select success!')
            #
            # 将获取的OriginDestinationOption列表的信息放到resultlist列表里
            #
            #    for i in my_dicts:
            #        my_dict = i['OriginDestinationOptions']['OriginDestinationOption']
            #        resultlist.append({"depAirport" : my_dict['DepartureAirport'],    #出发地
            #               "arrAirport":my_dict['ArrivalAirport'],                      #目的地
            #               "depTime" : my_dict['DepartureDateTime'],              #出发时间
            #               "arrTime" : my_dict['ArrivalDateTime'],                  #到达时间
            #               "flightNumber" : my_dict['FlightNumber'],                        #航班号
            #               "aircraftCode" : my_dict['AirEquipType'],                        #航空装备类型
            #               "cabin" : my_dict['RBD'],                                          #舱位级别
            #               "operatingCarrier" : my_dict['SeatCnt'],                                  #舱位数
            #               "TotalFare" : my_dict['TotalFare'],                              #总价
            #               "CurrencyCode" : my_dict['CurrencyCode'],                        #货币类型
            #               "carrier" : my_dict['AirlineCode']})                         #航司
            #    from_contlist=[]                                        #判断，去和回的机票，并分别放到列表里
            #    ret_contlist=[]
            #    for res in resultlist:
            #        if judgment_dpt == res["depAirport"]:
            #            from_contlist.append(res)
            #        elif judgment_arr == res["depAirport"]:
            #            ret_contlist.append(res)
            #
            #            print from_contlist

        #
        # for r in ret_contlist:
        #     print r
        # print from_contlist[0]
        # for c,v in from_contlist[0].items():
        #     print c,v
        # #
        #     def list():
        #         for qu in from_contlist:
        #             q = qu

            # routinglist=[]
            # rout = Routing()
            # rout.fromSegments = from_contlist
            # routinglist.append(rout)
            # if retdate != "":
            #     rout.retSegments = ret_contlist
            #     routinglist.append(rout)
            #    routinglist = []
            #    for ix in from_contlist:
            #
            #        if retdate !='':
            #            for k in ret_contlist:
            #                rout = Routing()
            #                rout.fromSegments=ix
            #                rout.retSegments = k
            #                routinglist.append(rout)
            #        else:
            #            rout = Routing()
            #            rout.fromSegments=ix
            #            routinglist.append(rout)
            #
            #        return {'ret': 0, 'msg': 'success', 'routings': routinglist}
            # else:
            #    logging.info('search failed!')
            #    return [], []
            #
            #

if __name__ == '__main__':
    scrapy = GEScrapy_App()
    result = scrapy.requestSelectPage(
        "TPE", "NRT", "2015-11-28", "2015-11-30", 1, 0, 0)  # TPE   NRT  KNH   TSA
    # print json.dumps(result, cls=RoutingEncoder)

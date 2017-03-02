# -*- coding: utf-8 -*-

import urllib2
import sys
import re
import glob
import operator

reload(sys)
sys.setdefaultencoding('utf-8')

alias = {
    'java': 'java',
    'javaee': 'java',
    'javase': 'java',
    'javaweb': 'java',
    'android': 'java',
    'eclipse': 'java',
    'weblogic': 'java',
    'tomcat': 'java',
    'jvm': 'java',
    'scala': 'scala',
    'clojure': 'clojure',
    'groovy': 'groovy',

    'net': '.net',
    '.net': '.net',
    'dotnet': '.net',
    'c#': 'c#',
    'unity': 'c#',
    'asp': 'asp',
    'asp.net': '.net',
    'winform': '.net',
    'vb': 'vb',
    'basic': 'vb',

    'php': 'php',
    'python': 'python',
    'perl': 'perl',
    'ruby': 'ruby',
    'rails': 'ruby',

    'c++': 'c++',
    'qt': 'c++',
    'c': 'c',
    'opencv': 'c',
    'objective-c': 'objective-c',
    'ios': 'objective-c',
    'iphone': 'objective-c',
    'cocos': 'objective-c',
    'swift': 'swift',

    'dba': 'sql',
    'oracle': 'sql',
    'mysql': 'sql',
    'pgsql': 'sql',
    'postgresql': 'sql',
    'database': 'sql',
    'sqlserver': 'sql',
    'sql': 'sql',

    'web': 'javascript',
    'js': 'javascript',
    'json': 'javascript',
    'node': 'javascript',
    'nodejs': 'javascript',
    'jquery': 'javascript',
    'phonegap': 'javascript',
    'angularjs': 'javascript',
    'javascript': 'javascript',
    'html': 'html',
    'css': 'css',

    'flash': 'actionscript',
    'flex': 'actionscript',
    'actionscript': 'actionscript',

    'sh': 'shell',
    'shell': 'shell',
    'unix': 'shell',
    'linux': 'shell',
    'ubuntu': 'shell',

    'go': 'go',
    'golang': 'go',
    'erlang': 'erlang',
    'lua': 'lua',
    'cobol': 'cobol'
}

languages = {}

urllib2.socket.setdefaulttimeout(10)
browser = urllib2.build_opener()
browser.addheaders = [
    ('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')]

url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%%2C00&district=000000&funtype=0100%%2C2500&industrytype=01%%2C38%%2C32%%2C40&issuedate=8&providesalary=99&keywordtype=1&curr_page=%d&lang=c&stype=2&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=01&companysize=99&lonlat=0%%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=-1'

for i in xrange(1, 2000):
    try:
        for content in re.findall('<td class="td1".*</td>', browser.open(url % i).read().decode('gbk')):
            title = re.search(
                'title="([^"]+)"', content) or re.search('>([^<]+)<', content)
            if title:
                for tech in re.findall('(?:c#|c\\+\\+|.net|[a-z]+)', title.group(1).lower()):
                    if alias.has_key(tech):
                        key = alias[tech]
                        languages[key] = languages.get(key, 0) + 1
    except:
        print('ignore')

for tech, count in sorted(languages.items(), key=operator.itemgetter(1)):
    print tech, count

from selenium import webdriver
import re
import os
import platform
class Dataer:
    __bd_url = 'https://www.baidu.com/baidu?isource=infinityitype=web&tn=02003390_42_hao_pg&ie=utf-8&wd='
    __sg_url = 'https://www.sogou.com/web?query='
    __360_url = 'https://www.so.com/s?q='
    def __init__(self):
        base_path = os.path.abspath(os.path.dirname(__file__))
        sys_str = platform.system()
        if sys_str == 'Windows':
            base_path += '\\chromedriver\\chromedriver.exe'
        elif sys_str == 'Linux':
            base_path += '\\chromedriver\\linuxchromedriver'
        else:
            base_path += '\\chromedriver\\macchromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"')
        self.driver = webdriver.Chrome(options=options,executable_path=base_path)
    def get_http(self,url):
        self.driver.get(url)
        html = self.driver.page_source
        re_comment=re.compile('<!--[^>]*-->')
        html = re_comment.sub('',html)
        pattern = r'<em>(.*?)</em>'
        resList = re.findall(pattern,html,re.S|re.M)
        resList.sort(key= lambda x:len(x),reverse=True)
        return resList
    def baidu(self,strList,redlen):
        result = []
        for i in range(len(strList)):
            urls = self.__bd_url + strList[i]
            resList = self.get_http(urls)
            if len(resList) > 2:
                if len(resList[0]) > redlen:
                    result.append({'word':strList[i],'url':urls,'status':1,'len':len(resList[0])})
                else:
                    result.append({'word':strList[i],'url':urls,'status':0,'len':len(resList[0])})
            else:
                result.append({'word':strList[i],'url':urls,'status':-1,'len':-1})
        return result
    def sougou(self,strList,redlen):
        result = []
        for i in range(len(strList)):
            urls = self.__sg_url + strList[i]
            resList = self.get_http(urls)
            if len(resList) > 2:
                if len(resList[0]) > redlen:
                    result.append({'word':strList[i],'url':urls,'status':1,'len':len(resList[0])})
                else:
                    result.append({'word':strList[i],'url':urls,'status':0,'len':len(resList[0])})
            else:
                result.append({'word':strList[i],'url':urls,'status':-1,'len':-1})
        return result
    def q360(self,strList,redlen):
        result = []
        for i in range(len(strList)):
            urls = self.__360_url + strList[i]
            resList = self.get_http(urls)
            if len(resList) > 2:
                if len(resList[0]) > redlen:
                    result.append({'word':strList[i],'url':urls,'status':1,'len':len(resList[0])})
                else:
                    result.append({'word':strList[i],'url':urls,'status':0,'len':len(resList[0])})
            else:
                result.append({'word':strList[i],'url':urls,'status':-1,'len':-1})
        return result
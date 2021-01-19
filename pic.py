import requests
import os
import re
import time
class image_get(object):
    def __init__(self,word):#初始化
        self.word = word
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}#添反爬加请求头防止
        self.start_url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn={}&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0'%word#网页初始页
        self.start_url_list = []
        i = 0;
        while i < 10:
            url = self.start_url.format(i*20)
            self.start_url_list.append(url)
            i = i+1
       

    def get_content(self,url):
        #print(url)
        html = requests.get(url,headers=self.headers)
        img_list = re.findall('"objURL":"(.*?)",',html.text)
        return img_list

    def save(self,start_url_list):
        x=1
        for pic_url in start_url_list:
            print("正在下载第%d张"%x)
            x+=1
            end = re.search('(.jpg|.jpeg|.png)$',pic_url)
            if end == None:
                pic_url = pic_url + '.jpg'
            try:
              
                with open(imgoutpath + self.word + '/{}'.format(pic_url[-10:]), 'ab') as f:
                    try:
                        pic = requests.get(pic_url,headers=self.headers,timeout=5)
                        f.write(pic.content)
                    except Exception:
                        pass
            except Exception:
                pass



    def run(self):
        for url in self.start_url_list:
            start_url_list = self.get_content(url)
            self.save(start_url_list)

if __name__ == '__main__':
    imgoutpath = "C://Users/12234/.spyder-py3/images";
    word = input('请输入关键字：')
    os.mkdir(imgoutpath + word)
    tupian = image_get(word)
    tupian.run()

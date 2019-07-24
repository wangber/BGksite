###从短文学网上爬取句子，随机取页，随机取页内句子###
# coding=utf-8
import requests
from bs4 import BeautifulSoup
import random
def get(url):
    i = random.randint(1,200)
    url="https://www.duanwenxue.com/yuju/shanggan/list_"+str(i)+".html"
    re=requests.get(url)
    soup = BeautifulSoup(re.text,"html.parser")

    sentence_set=soup.find_all("div",{"class":"list-short-article"})[0].text
    t=sentence_set.split("【伤感语句】")
    sentence_list=[]
    for t_instence in t:
        if len(t_instence.split("\n\n")[0])>=6:
            sentence_list.append(t_instence.split("\n\n")[0])
    j=random.randint(0,len(sentence_list))
    sen=sentence_list[j-1]
    return sen



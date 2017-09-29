
import requests
from bs4 import BeautifulSoup as bs
import json

# a = requests.get('http://www.osaka-info.jp/en/events/festivals_events/')
# a = requests.get('http://www.osaka-info.jp/jp/events/')
# a = requests.get('http://www.osaka-info.jp/admin/mt/mt-search.fcgi?IncludeBlogs=51&template_id=&limit=20&archive_type=Index&search_lang=ja&page=3')
# a = requests.get('http://www.osaka-info.jp/admin/mt/mt-search.fcgi?IncludeBlogs=51&template_id=&limit=20&archive_type=Index&search_lang=en&page=3')
def crawl(xxx):
    a = requests.get(xxx)
    a.encoding='utf8'




    b = bs(a.text, 'html.parser')
    # base ='http://www.osaka-info.jp'
    base=''


    tmp={}
    link = b.find_all('div', class_='entryListImg')
    for ii, i in enumerate(link):
        tmp={}
        tmp['link']=i.a['href']
        tmp['img']=i.img['src']
        tmp['pic'] = list(requests.get(base+i.img['src']).content)
        tmp['name']=i.img['alt']

    link = b.find('div', class_='entryListInfo')
    x = link.parent
    ii = 0
    ll=[]
    while (x):
        abc = x.find('div',{"class":"entryListDescription"})
        while (abc):
            if "".join(abc['class']) !='entryListMore':
                tmp["".join(abc['class'])]=abc.contents[-1]
            abc = abc.find_next_sibling()
        x=x.find_next_sibling()
        ll.append(tmp)
        ii +=1

    # tmp[0]
    return ll
y=[]
y = crawl('http://www.japan-osaka.cn/mt/mt-search.cgi?IncludeBlogs=6&template_id=&limit=20&archive_type=Index&page=1')
y.append(crawl('http://www.japan-osaka.cn/mt/mt-search.cgi?IncludeBlogs=6&template_id=&limit=20&archive_type=Index&page=2'))
y.append(crawl('http://www.japan-osaka.cn/mt/mt-search.cgi?IncludeBlogs=6&template_id=&limit=20&archive_type=Index&page=3'))


with open('osaka_festival.json','w') as fh:
    json.dump(y, fh, ensure_ascii=False)

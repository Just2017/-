
import urllib.request
import urllib.parse
import re
import os

header=\
    {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
     'Accept': 'text/plain, */*; q=0.01',
     'Accept-Language': 'zh-CN,zh;q=0.8',
     'X-Requested-With': 'XMLHttpRequest',
     'Connection': 'keep-alive',
    "Cookie":"__cfduid=d9625fabd71ff1ba94d67ec814e05e1571473486956; BDUSS=4tcGMxYzd-dm94ZzhzaTNqenptWVlpWFFGeUh5OGR1ZTRFMnhwNnRJekdEV0ZZSVFBQUFBJCQAAAAAAAAAAAEAAACevjl7vvTYvMq~2LwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMaAOVjGgDlYY2; BAIDUID=D6E9D0B92F3F35B1E4A7AD3CABCBAED3:FG=1; BIDUPSID=FF63886073870CA5ABC6EA2663979765; PSTM=1482469381; indexPageSugList=%5B%22king%20of%20the%20Kill%E5%A4%B4%E5%83%8F%22%2C%22%E5%88%9B%E6%84%8F%E6%91%84%E5%BD%B1%22%2C%22%E9%AB%98%E6%B8%85%E6%91%84%E5%BD%B1%22%2C%22test%22%2C%22s%20logo%22%5D; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; userFrom=null",
    "referer":"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1490169358952_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%BE%8E%E5%A5%B3"
    }
url="https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn={pageNum}&rn=30&gsm=1e00000000001e&1490169411926="
#keyword=input("请输入搜索关键字：")
keyword='美女'
keyword=urllib.parse.quote(keyword,"utf-8")
n=0
j=0
error=0

while(n<30*100):
    n+=30
    #url链接
    url1=url.format(word=keyword,pageNum=str(n))

    #获取请求
    rep=urllib.request.Request(url1,headers=header)
    #打开网页
    rep=urllib.request.urlopen(rep)
    #读取网页数据
    try:
        html=rep.read().decode("utf-8")
    except:
        print("something wrong!")
        error=1
        print("-------------now page ="+str(n))
    if(error==1): continue
    #正则匹配
    p=re.compile("thumbURL.*?\.jpg")
    #获取正则匹配结果，返回的是一个list
    s=p.findall(html)
    #写入文件夹
    if os.path.isdir("f:\\myproject\\MyCrawlPic\\美女")!=True:
        os.makedirs(r"f:\\myproject\\MyCrawlPic\\美女")
    with open("testPic1.txt","w") as f:
        for i in s:
            i=i.replace("thumbURL\":\"","")
            print(i)
            f.write(i)
            f.write("\n")
            urllib.request.urlretrieve(i,"f:\\myproject\\MyCrawlPic\\大胸\\pic{num}.jpg".format(num=j))
            j+=1









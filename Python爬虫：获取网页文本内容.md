>用python写个简单的爬虫练练手，基本就是抓取网页的文本内容，放到本地的txt文档中

1.准备工作：
需要用到的模块是：requests和BeautifulSoup，安装一下
在cmd或者git bash下运行以下代码安装（要装了pip）
```
$ pip install requests
$ pip install beautifulsoup4
```
2.导入模块
```
import requests
from bs4 import BeautifulSoup
```
requeses模块使用参考：
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0015109021115795adfc5c8629f4f98985063b5a7e3ff87000
beautifulsoup模块使用参考：
https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html

3 . 找到你要抓取的网页的主体内容所在的位置：
在浏览器中使用开发者工具查看网页源码：
![image.png](http://upload-images.jianshu.io/upload_images/4991143-3ec03ade80b80e94.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
可以看到我想要获取的文本内容在class为post-body的div里：
接下来就可以写了：
```
if __name__ == '__main__':
    html=requests.get('https://chenqingyun.github.io/')
    html.encoding='utf-8'
    soup = BeautifulSoup(str(html.text),'html.parser')
    if len(soup.select('.post-body')) > 0:
    	txt = soup.select('.post-body')[0].text
    	with open('G:\python\PythonProject\chenqingyun.txt','w') as f:
    		f.write(txt)
    	print('获取数据成功')
```
通过requests模块获取网页的源码，然后通过beautifulsoup获取.post-body类的文本内容，这里加了个判断是为了防止主体内容为空时报错，一开始我放错了网址就发生了类似的错误
以上就获取到了网页的第一篇文章，想要获取其他文章可以将select('.post-body')[0]这里的下标改成其他的数字，主要不要超出总长。
接着打开本地的txt就可以看到文档了。
![image.png](http://upload-images.jianshu.io/upload_images/4991143-9bf463d56ab8f74b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

知道了这个，后面可以应该尝试做个爬虫小工具了吧。
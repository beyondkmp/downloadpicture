import re
import urllib
import httplib
def getHtml(url):
	page=urllib.urlopen(url)
	html=page.read()
	return html

def DownImg(imgUrl,name):
	conn=httplib.HTTPConnection(imgUrl)
	user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
	headersP={'User-Agent':user_agent}
	conn.request("get","",headers=headersP)
	r1=conn.getresponse()
	data=r1.read()
	f=file(name,"wb")
	f.write(data)
	f.close()
def getImg(html):
	reg=r'<img src=\"(.*\.jpg)\" pic_ext'
	imgre=re.compile(reg)
	imglist=re.findall(imgre,html)
	x=1
	print 'starting...'
	for imgurl in imglist:
		print imgurl
		urllib.urlretrieve(imgurl,'%s.jpg' %x)
		#DownImg(imgurl,str(x))
		print str(x)+'is done'
		x+=1
	return 1

s=raw_input("please input the url:")
html=getHtml(s)
print 'Total:'+str(getImg(html))+' jpgs have been dwonload'

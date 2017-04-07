import time
from optparse import OptionParser
import urllib2
import sys
import re
import socket
def localtime(timeStamp):
	timeArray = time.localtime(timeStamp)
	otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
	return otherStyleTime


def  GetUserParser():
	usage = "usage:  %prog  [options] arg1 arg2"
	opt=OptionParser(usage=usage)
	opt.add_option("-u","--url",dest='url',help="masscan xml url",default="/root/log2.txt")
	opt.add_option("-t","--thread",dest='thread',help="thread ",default=10)
	(options, args) = opt.parse_args()
	if not options.url:
		print "-u or --url error"
	return options


socket.setdefaulttimeout(3)

def GetHtmlTitle(ip):
	try:
		type = sys.getfilesystemencoding()
		url=urllib2.urlopen("http://"+ip)
		html=url.read()
		html=html.decode("UTF-8").encode(type)
		if html and html!='' :
			title =re.search("<title>(.*)</title>",html)
			if title:
				return title.group(1)
		return ''
	except Exception as e:
		#print e
		pass
def FilePrint(ip,title):
	if ip and title:
		tt= ip,"/",title,"\r\n"
		print ip,"/",title
		f=open("/root/redtitle2.log",'a+')
		f.flush()
		f.writelines(tt)
		f.close()		



if __name__=="__main__":
	timeStamp = 1381419600
	print localtime(timeStamp)
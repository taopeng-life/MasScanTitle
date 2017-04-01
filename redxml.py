#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xml.dom.minidom
import urllib2
import re
import socket
import io
import sys
import threading

iplist=[]
index=0
socket.setdefaulttimeout(1)
def  GetXml():
	global iplist
	dom=xml.dom.minidom.parse('/root/log2.txt')
	root=dom.documentElement
	addresslist =root.getElementsByTagName('address')

	iplist=[]
	for x in addresslist:
		iplist.append(x.getAttribute("addr"))

def GetTitle(ip):
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
lock=threading.Lock();
def StartThreading():
	global index
	while index<len(iplist):
		lock.acquire()
		ip=iplist[index]
		thisindex=index=index+1
		lock.release()
		title=GetTitle(ip)
		FilePrint(str(thisindex)+"  "+ip,title)
		
def StartThread():
	GetXml()
	threads=[]
	for x in xrange(1,30):
		t=threading.Thread(target=StartThreading);
		threads.append(t)

	for t in threads:
		t.start()
	for t in threads:
		t.join()


if __name__=="__main__":
	StartThread()

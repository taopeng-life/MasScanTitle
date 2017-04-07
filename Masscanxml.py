import xml.dom.minidom
from Tools  import *
import threading
#from Tools import *


class XmlModel:
	"""docstring for ClassName"""
	#root=None;
	iplist=[]
	def __init__(self, url):
		dom=xml.dom.minidom.parse(url)
		self.root=dom.documentElement
		addresslist =self.root.getElementsByTagName('address')
		for x in addresslist:
			XmlModel.iplist.append(x.getAttribute("addr"))

	def  GetXmlInfo(self):
		nmaprun =int(self.root.getAttribute("start"));
		finished=int(self.root.getElementsByTagName("finished")[0].getAttribute("time"));
		print "messcan starttime:",localtime(nmaprun),"messcan endtime:",localtime(finished)



class FileWirt:
		"""docstring for FileWirt"""
		def __init__(self, arg):
			#super(FileWirt, self).__init__()
			self.arg = arg

		

class ThreadMan:
	"""docstring for ThreadMan"""
	


	def __init__(self,threadNum,iplist):
		self.iplist=iplist;
		self.threadNum =threadNum;
		self.index=0
		self.lock=threading.Lock();
			
	def StartThreading(self):
	#	global index
		#print self.index
		while self.index<len(self.iplist):
			self.lock.acquire()
			ip=self.iplist[self.index]
			# print ip
			thisindex=self.index=self.index+1
			# print "ssss"
			self.lock.release()
			title=GetHtmlTitle(ip)
			FilePrint(str(thisindex)+"  "+ip,title)
		
	def StartThread(self):
		print "StartThread start",self.threadNum
		#GetXml()
		threads=[]
		for x in xrange(0,self.threadNum):
			t=threading.Thread(target=self.StartThreading);
			threads.append(t)
		for t in threads:
			t.start()
		for t in threads:
			t.join()
	
if __name__ == '__main__':
	ThreadMan(1,["127.0.0.1"]).StartThread()


				
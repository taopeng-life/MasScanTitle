#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tools import *
from Masscanxml import *

if __name__=="__main__":
	
	option=GetUserParser();
	iplist=XmlModel(option.url).iplist
	#print iplist
	ThreadMan(option.thread,iplist).StartThread()

#-*- coding:utf-8 -*- 
 
import socket 
import struct 
import time 
import win32api 
import random
import os
 
def getOfflineTime(days):
	OFFSET = 31536000L
	data_result = 1470545989
	data_result = data_result - OFFSET + days*3600
	return data_result
 

def setSystemTime(days): 
	tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = time.gmtime(getOfflineTime(days))
	win32api.SetSystemTime(tm_year, tm_mon, tm_wday, tm_mday, tm_hour, tm_min, tm_sec, 0) 
	print tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst
	
	print "Set System OK!" 
	
def getRandom():
	stopNum = (int)(time.time()%100)
	print str(random.randint(0, stopNum))
	return str(random.randint(0, stopNum))
 
if __name__ == '__main__': 
	timeSpaces = 10
	days = 0
	writeTime = 0
	setSystemTime(days)
	
	while days <= 365:
		fp = open('random.txt', 'w')
		fp.write(getRandom())
		fp.close()
		os.system('git add .')
		os.system('git commit -m "commit"')
		writeTime = writeTime + 1
		if writeTime % 6 == 0:
			setSystemTime(days)
			days = days + 1
		time.sleep(timeSpaces)
		
	
	print 'finished'

import subprocess
import os
import threading

cmdping = "10.11.1."

class MyThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
    	def run(self):             
        	SCANIP(self.counter)

def SCANIP(x):		
	try:
		devnull = open(os.devnull, 'w')
    		res = subprocess.call('ping -c1 ' + cmdping + str(x),stdout=devnull, stderr=devnull,shell = True)

    		if res == 0:
       			print "ping OK To " + cmdping + str(x)
	except subprocess.CalledProcessError as e:
		print "error "


if __name__ == '__main__':
    for x in range(254):                                     # Four times...
        mythread = MyThread(1, "Thread" + str(x), x + 1)  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()    

import os,sys
import Tkinter
import sys,re
import logging
import argparse
import os
import re
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from socket import *

class hw4app_tk(Tkinter.Tk):
	def __init__ (self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()

	def initialize(self):
		self.grid()

		button1=Tkinter.Button(self,text=u"ICMP",height=3,width=10,command=self.func1)
		button1.grid(column=0,row=0)

		button2=Tkinter.Button(self,text=u"PORT",height=3,width=10,command=self.func2)
		button2.grid(column=0,row=1)

		button3=Tkinter.Button(self,text=u"ROUTERS",height=3,width=10,command=self.func3)
		button3.grid(column=0,row=2)

		button4=Tkinter.Button(self,text=u"WEB",height=3,width=10,command=self.func4)
		button4.grid(column=0,row=3)

		button5=Tkinter.Button(self,text=u"SNMP",height=3,width=10,command=self.func5)
		button5.grid(column=0,row=4)

		self.labelVar=Tkinter.StringVar()
		label=Tkinter.Label(self,fg="black",bg="white",anchor="w",textvariable=self.labelVar)
		label.grid(column=1,row=0,sticky='EW',columnspan=2)

		self.grid_columnconfigure(1,weight=1)

	def icmp(self):
		for k in range(1,255):
			ip = "192.168.144." + str(k)
			ans,unans=sr(IP(dst=ip)/ ICMP() / "Hello", timeout=0.1)
			my_ip=re.findall(r'proto=icmp dst=(\S+)', str(ans))
			for j in range(0,len(my_ip)):
				print my_ip[j]
				f = open('icmp.txt','a')
				f.write("IP:<%s>" %my_ip[0] + "\n")


	def port(self):
		file = open("icmp.txt",'r')
		IPs = file.readlines()
		for i in range(0,len(IPs)):
			ipp=re.findall(r'IP:<(\S+)>',str(IPs[i]))
			ans,unans=sr(IP(dst=ipp)/TCP(dport=range(79,85)),timeout=0.1)
			IP1=re.findall(r'proto=tcp dst=(\S+) ',str(ans))
			Port1=re.findall(r'TCP  dport=(\S+) ',str(ans))
			for j in range(0,len(IP1)):
				with open("port.txt",'a') as result:
					result.write("IP:<"+IP1[j]+"> Port:<" + Port1[j]+">\n")

	def web(self):
		ans,unans=sr(IP(dst=["sporx.com","facebook.com", "instagram.com", "twitter.com", "ieu.edu.tr", "google.com", "izmir.bel.tr", "yahoo.com", "stackoverflow.com", "9gag.com"])/TCP(dport=range(1,250)),timeout=0.1)
		IP1=re.findall(r'proto=tcp dst=(\S+) ',str(ans))
		Port1=re.findall(r'TCP  dport=(\S+) ',str(ans))
		for i in range(0,len(IP1)):
			with open("webserver.txt",'a') as result:
					result.write("IP:<"+IP1[i]+"> Port:<"+Port1[i]+">\n")

	def routers(self): 
		hostname = "google.com"
		for i in range(1, 28):
			for j in range(33433, 33436): # traceroute port range ( official ) 33434 - 333534
			    pkt = IP(dst=hostname, ttl=i) / UDP(dport=j) # Send the packet
			    reply = sr1(pkt, verbose=0,timeout=0.5)  # get a reply
			    if reply is None: # No reply
			        break
			    elif reply.type == 3:  # We've reached our destination
			        print "Done!", reply.src
			        break
			    else:	# We're in the middle somewhere
			        print "%d" % i , reply.src 
			        fl = open("routers.txt", 'a')
			        fl.write("IP:" + str(reply.src) + "\n")

	def snmp(self):
		for k in range(1, 255):
			ip = "192.168.144." + str(k)	
			ans,unans=sr(IP(dst=ip)/UDP(dport=161)/SNMP()/"Hello",timeout=0.1)
			my_ip=re.findall(r'proto=udp dst=(\S+) ',str(ans))
			my_port=re.findall(r'UDP  dport=(\S+) ',str(ans))
			for j in range(0,len(my_ip)):
				f = open('snmp.txt', 'a')
				f.write("IP:<" + my_ip[j] + "> Port:<" +  my_port[j] + ">\n")

	def func1(self):
		self.icmp()
		file_object= open('icmp.txt','r')
		a=file_object.read()
		file_object.close()
		self.labelVar.set(a)
		
	def func2(self):
		self.port()
		file_object=open('port.txt','r')
		b=file_object.read()
		file_object.close()
		self.labelVar.set(b)

	def func3(self):
		self.routers()
		file_object=open('routers.txt','r')
		e=file_object.read()
		file_object.close()
		self.labelVar.set(e)

	def func4(self):
		self.web()
		file_object=open('webserver.txt','r')
		f=file_object.read()
		file_object.close()
		self.labelVar.set(f)

	def func5(self):
		self.snmp()
		file_object=open('snmp.txt','r')
		g=file_object.read()
		file_object.close()
		self.labelVar.set(g)
	
if __name__== "__main__":
	app = hw4app_tk(None)
	app.title('CE340 Hw4 App')

	app.mainloop()
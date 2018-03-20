#!/usr/bin/env python3
import socket
import threading
import binascii
import sys
import select
#from termcolor import colored

def menu():
	printAccueil()
	quit = False
	hote = "192.168.1.13"
	port = 7890

	hote_temp = input('IP du C&C server : ')
	if hote_temp:
		print ('not hote_temp ')
		hote = hote_temp
	port_temp = input('Port du C&C server :')
	if port_temp:
			print ('not port_temp')
			port = int(port_temp)
	print ("Connexion au serveur....")
	socket_ = connect(hote,port)
	while not quit:	
		
		socket_list= [sys.stdin, socket_]
		#get the list sockets which are readable 
		ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [])
		for sock in ready_to_read:
			if sock == socket_:
				data = sock.recv(4096)
				if not data:
					print ('\nDisconnected from chat server')
					sys.exit()
				else:
					#print data
					sys.stdout.write(data.decode('utf-8'))
					sys.stdout.write('[Me receive] '); sys.stdout.flush()
			else:
				msg = sys.stdin.readline()
				socket_.send(msg.encode('UTF-8'))
				sys.stdout.write('[Me send] '); sys.stdout.flush()  



def listenToServer(socket_):
	data = socket_.recv(4096)
	if not data:
		print("\nDeconnexion du serveur")
	else:
		print("data type : " + str(type(data.decode('utf8'))))
		print("data received : {0!r}".format(data.decode('utf8')))
		sys.stdout.write(data)
		sys.stdout.write('[Receive from server : ] '); sys.stdout.flush()  
	

def connect(hote, port):
	try:
		socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket_.settimeout(2)
		socket_.connect((hote,port))
		print ("connection on port "+str(port))
	except Exception as e:
		s = str(e)    	
		print ("Problème lors de la connextion au serveur distant")
		print (s)
		sys.exit
	print ("Connected to remote host. You can start sending messages")
	sys.stdout.write('[first message] '); sys.stdout.flush()
	return socket_
	
def close(socket_):
	print("Fermeture de connexion...")
	socket_.close

def printAccueil():
	#print (colored ("hello", "red"))
	print (' __        ________		______	 ___________ 		')
	print ('|  |   	  |        \\ /      \\ |____   ____| 	')
	print ('|  |      |  .----. | |  *--*  |     | |     		')
	print ('|  |      |  *----* | |  |  |  |     | |    		')
	print ('|  |      |  .----. | |	 |  |  |     | |    		')
	print ('|  |_____ |  *----* | |  *--*  |     | |    		')
	print ('|________||________/  \________/	 |_|			')


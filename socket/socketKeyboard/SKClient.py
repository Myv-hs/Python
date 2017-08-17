import sys
import socket               
import keyboard

trgtIP = '192.168.1.9'
port = 12346
toggle = False

if len(sys.argv)>1:
	inputIP = sys.argv[1]
	trgtIP = inputIP
	print("You've chosen to connect to: "+trgtIP)

def sendKey (e):
	global toggle
	global port
	global trgtIP
	s = socket.socket()         

	if e.name == 'esc' and e.event_type == 'down':
		toggle = not toggle
		print("Key Transfer on: "+str(toggle))

	if toggle == True and e.name !='esc':# and e.name !='?' and e.name !='asciicircum':
		keyname = e.name
		key = e.event_type+" "+keyname
		try:
			s.connect((trgtIP, port))
			s.send(key.encode())
		except:
			print("Socket failed, check input IP")

keyboard.hook(sendKey)
keyboard.wait()
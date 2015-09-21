import socket
import sys
P  = '\033[35m' # purple
W  = '\033[0m'  # white (normal)
O  = '\033[33m' # orange
R  = '\033[31m'
G  = '\033[32m'
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
host = raw_input("write your ip : ") 
port = int(raw_input("write the port for listning : "))  
x = raw_input("Write the website to reginreator : ")           
s.bind((host, port)) 
b ="""HTTP/1.1 301 Moved Permanently\r\nServer: nginx\r\nDate: Wed, 21 May 2014 19:17:05 GMT\r\nContent-Type: text/html; charset=iso-8859-1\r\nContent-Length: 228\r\nConnection: keep-alive\r\nLocation: http://%s/\r\n\r\n<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>301 Moved Permanently</title>\n</head><body>\n<h1>Moved Permanently</h1>\n<p>The document has moved <a href="http://%s/">here</a>.</p>\n</body></html>\n""" %(x , x)
s.listen(5) 
try :
   while True:
      c, addr = s.accept()     
      print (P +'Got connection from') , addr , W
      data = c.recv(10000)
      print 'data is : ' , repr(data)
      c.send(b)
      print 'data is : ' , repr(data)
      
 
except KeyboardInterrupt :
    print R + "You pressed Ctrl+C" +W
    sys.exit()
except socket.gaierror:
    print R + 'Host did not open plz try to check if that your local ip ' +W
    sys.exit()
except socket.error:
    print R + "Couldn't listning the port maby is used" + W
    sys.exit()

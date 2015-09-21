import socket              
print "welcome to Download Direct link "
s = socket.socket()         
host = raw_input("write the ip : ") 
port = int(raw_input("write the port : "))
filE = raw_input("write the name of file : ")
asa = raw_input('location of file : ')
a = open(asa , 'r')
x = a.read()

send = """HTTP/1.1 200 OK\r\nServer: LRBD-bigdownload-\r\nDate: Thu, 16 Jul 2015 12:03:30 GMT\r\nConnection: close\r\nAccept-Ranges: bytes\r\nContent-transfer-encoding: binary\r\nContent-Length: """+ str(len(x)) +"""\r\nContent-Disposition: attachment; filename="""+ filE +"""\r\nContent-Type: application"""+"\r\n\r\n"+ x
s.bind((host, port))        

s.listen(5)                 
while True:
   c, addr = s.accept()     
   print ('Got connection from') , addr
   c.send(send)
   data = c.recv(10000)
   print 'shell code : ' , repr(data)
   print 'data is : ' , data
   c.close()                

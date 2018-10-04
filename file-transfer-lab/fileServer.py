#! /usr/bin/env python3
import sys, re, socket, os
sys.path.append("../lib")       # for params
import params

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "fileSServer"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # listener socket
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("listening on:", bindAddr)

i = 1
while (i < 10):   # listen to max 10 clients

    sock, addr = lsock.accept()
    child_pid = os.fork()

    if child_pid==0:
        print("connection rec'd from client " + str(i) + ": " + str(addr) + "\n")


        from framedSock import framedSend, framedReceive

        temp = ''
        #from fileClient import newfile

        while True:
            payload = framedReceive(sock, debug)
            if debug: print("rec'd: ", payload)

            if payload:
                temp += payload.decode()
            if not payload:
                filepath = os.path.join(os.getcwd()+"/Server/"+"myfile.txt")
                f = open(filepath, "w")
                f.write(temp)
                break
            print(payload)

            #if not os.path.exists(os.getcwd()+"Server"):
                #os.makedirs(os.getcwd()+"Server")
            framedSend(sock, payload, debug)
            break
    else: 
        i+=1



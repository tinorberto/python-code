
from array import *

def findOut(mac_oui):
    filepath = 'oui.txt'  
    with open(filepath,  encoding="utf8") as fp:  
        line = fp.readline()
        cnt = 1
        while line:
            #print("Line {}: {}".format(cnt, line.strip()))
            if line.strip().find(mac_oui) is not -1:
                   return line.strip()
                   #print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
    



listpath = 'list2.txt'
with open(listpath,  encoding="utf8") as fp:  
    line = fp.readline()
    cnt = 1
    data = []
    while line:
        if cnt == 1:
            line = fp.readline()
            cnt += 1
            continue
        #print("Line {}: {}".format(cnt, line.strip()))
        k =  line.strip().rfind("\t")
       
        if k != -1:
            name =  line.strip().split("\t")[0]
            mac = line[k+1:]
            format_mac = mac[:8].replace(":", "-")
            data.append(str("Name :%s   Mac :%s Description: %s"%(name, format_mac, findOut(format_mac))))
            #print ("Name :%s   Mac :%s Description: %s"%(name, format_mac, findOut(format_mac)))


        line = fp.readline()
        cnt += 1
    data.sort()
    for l in data:
        print (l)

 









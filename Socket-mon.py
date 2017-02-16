import socket  # This module provides socket functions
import psutil  # This module provides information of running process

lst = []       # Creation of Lists
tcpConns = []
id = []

def main():  # It process Tcp connections as list of local address, remote address, Pid and statu
    for con in psutil.net_connections(kind='tcp'): 
        laddr = "%s@%s" % (con.laddr) 
        raddr = ""
        if con.raddr:
            raddr = "%s:%s" % (con.raddr)
            if raddr ==" ": # Skips all the record which will having no remote address
             pass
            else:
                lst = [con.pid,laddr,raddr,con.status]
                tcpConns.append(lst)
                id.append(con.pid)  # appending all pid in one list
    tcpConns.sort()
    tracker = []
    frequencyCount = []
    for d in id:
      if d not in tracker:
          count = (id.count(d),d)  # counting number of connections and stores Pid and count of connection
          frequencyCount.append(count)
          sortFC = sorted(frequencyCount,reverse = True) 
          tracker.append(d)
    print '"PID","Laddr", "Raddr", "Status"'
    for fc in sortFC:
       for gettc in tcpConns: # matching the Pid from two list and print sorted list
        if fc[1] == gettc[0]: 
         print '"%s","%s","%s","%s"' % (gettc[0],gettc[1],gettc[2],gettc[3])
             
if __name__ == '__main__':
 main()

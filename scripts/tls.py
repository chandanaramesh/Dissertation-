import pyshark
import socket

#value = socket.gethostbyname('google.com')
#print(value)
cap = pyshark.FileCapture('encrypt.pcap')
'''
def tcp_stream(pkt):
    session_index = []
    for i in pkt:
        try:
            session_index.append(pkt.tcp.stream)
            print(session_index)
        except:
            pass
        print(session_index)
    if len(session_index) == 0:
        max_index = 0
        print("No TCP found")
    else:
        max_index = int(max(session_index)) + 1

tcp_stream(cap)
'''

def read_url():
    #linelist = list()
    #lineList = [line.rstrip('\n') for line in open('dnsreq.txt', 'r')]
    file = open("dnsreq.txt", "r")
    for elements in file:
        line = elements.split(",")
        for url in line:
            parsed = urlparse(url)
            if parsed.hostname:
                print(parsed.hostname)
            #resolve = socket.gethostbyname_ex(url)
            #print ("\n\nThe IP Address of the Domain Name is: "+repr(resolve))
            #resolve = socket.gethostbyname(hostname)
            #resolve = socket.gethostbyname("https://www.reddit.com/")
            print(resolve)


def tcp_stream(pkt):
    tcp = pkt.tcp
    if tcp.flags == '0x00000011':    
        print(tcp.stream, tcp.time_relative)
cap.apply_on_packets(tcp_stream, timeout=100)
#read_url()


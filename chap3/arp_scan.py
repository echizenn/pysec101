#!/usr/bin/python

from scapy.all import Ether, ARP, srp
import ipaddress   # IPv4アドレスやIPv6アドレスのネットワーク生成・変更・操作を行うライブラリ

myip = '172.20.10.2'
netmask = '255.255.255.240'
hwaddr = 'ff:ff:ff:ff:ff:ff'

def gen_cidr(ip, netmask):
    ipv4 = ipaddress.ip_address(ip)
    netmask = ipaddress.ip_address(netmask)
    netaddr = ipaddress.ip_address(int(ipv4) & int(netmask))
    netaddr = str(netaddr).split('/')[0]
    
    cidr = bin(int(netmask)).count('1')
    return str(netaddr) + '/' + str(cidr)

cidr = gen_cidr(myip, netmask)

print('Scanning on : ' + cidr)

pkt = Ether(dst=hwaddr)/ARP(op=1, pdst=cidr)
ans, uans = srp(pkt, timeout=2)

print('')
for send, recv in ans:
    print(recv.sprintf('%ARP.psrc% is up.'))
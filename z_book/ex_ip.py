#!/usr/bin/python3
# coding: utf-8 
"""
__title__ = ''
__author__ = ''dengminjie
__mtime__ = '18/06/04 0004'
# 
"""

#!/usr/bin/env python

from IPy import IP

# ip_s = raw_input('Please input an IP or net-range: ')
ip_s = input('Please input an IP or net-range: ')
ips = IP(ip_s)


if len(ips) > 1:
    print('net: %s' % ips.net())
    print('netmask: %s' % ips.netmask())
    print('broadcast: %s' % ips.broadcast())
    print('reverse address: %s' % ips.reverseNames()[0])
    print('subnet: %s' % len(ips))
else:
    print('reverse address: %s' % ips.reverseNames()[0])

print('hexadecimal: %s' % ips.strHex())
print('binary ip: %s' % ips.strBin())
print('iptype: %s' % ips.iptype())
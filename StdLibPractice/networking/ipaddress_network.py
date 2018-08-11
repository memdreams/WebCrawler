# https://pymotw.com/3/ipaddress/index.html

import binascii
import ipaddress

ADDRESSES = [
    '172.168.0.251',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]

def addresses(ad=ADDRESSES):
    for ip in ad:
        addr = ipaddress.ip_address(ip)
        print('{!r}'.format(addr))
        print('  IP version:', addr.version)
        print('  is private:', addr.is_private)
        print(' packed form:', binascii.hexlify(addr.packed))
        print('     integer:', int(addr))
        print()

NETWORKS = [
    '172.168.0.0/23',
    'fdfd:87b5:b475:5e3e::/64',
]

def network():
    for n in NETWORKS:
        net = ipaddress.ip_network(n)
        print('{!r}'.format(net))
        print('     is private:', net.is_private)
        print('      broadcast:', net.broadcast_address)
        print('     compressed:', net.compressed)
        print('   with netmask:', net.with_netmask)
        print('  with hostmask:', net.with_hostmask)
        print('  num addresses:', net.num_addresses)

        # ipaddress.ip_network iterate
        # for i, ip in zip(range(36, 39), net): # why ip always from 0?
        for i, ip in zip(range(36, 39), net.hosts()): # hosts check if the ip fits for a host
            print(ip)
        print(net[31])

def interface():
    for ip in NETWORKS:
        iface = ipaddress.ip_interface(ip)
        print('{!r}'.format(iface))
        print('network:\n ', iface.network)
        print('ip: ', iface.ip)
        print('IP with prefixlen:\n ', iface.with_prefixlen)
        print('netmask: ', iface.with_netmask)
        print('hostmask:', iface.with_hostmask)

interface()

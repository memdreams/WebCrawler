import socket

# gethostname
print(socket.gethostname())

HOSTS = [
    'www.google.com',
    'www.python.org',
    'pymotw.com', ## 66.33.211.242
    'nosuchname'
]

def hostname_eg():
    for host in HOSTS:
        try:
            name, aliases, addresses = socket.gethostbyname_ex(host)
            print('Hostname: {}, Aliases: {}, Address: {}'.format(name, aliases, addresses))

            print('{} : {}'.format(host, socket.gethostbyname(host)))
        except socket.error as msg:
            print('ERROR: {}, {}'.format(host, msg))


for host in ['pymotw.com', 'google.com']:
    print('{:>10} : {}'.format(host, socket.getfqdn(host)))

hostname, aliases, addresses = socket.gethostbyaddr('172.217.2.100')
print(hostname)

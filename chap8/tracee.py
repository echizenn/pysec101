#!/usr/bin/python

f = open('/etc/hosts', 'rb')
data = f.read()
print(data)
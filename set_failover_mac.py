#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import ovh
import json
import sys


if len(sys.argv)!=5:
        print "Error incorrect argument number"
        print "Usage: "+sys.argv[0]+" <ServiceName>  <MacAddress>  <IP> <VMName>"
        exit()

service = sys.argv[1]
mac =  sys.argv[2]
ip = sys.argv[3]
vm = sys.argv[4]

# Instanciate an OVH Client.
client = ovh.Client()


result = client.post('/dedicated/server/' + service + '/virtualMac/' + mac + '/virtualAddress',
    ipAddress = ip,
    virtualMachineName= vm,
    )


# Pretty print
print json.dumps(result, indent=4)

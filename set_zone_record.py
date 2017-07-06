#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import ovh
import json
import sys


if len(sys.argv)!=5:
        print "Error incorrect argument number"
        print "Usage: "+sys.argv[0]+" <DomainName>  <RecordType>  <Subdomain> <Value>"
        exit()

domain = sys.argv[1]
recordtype =  sys.argv[2]
subdomain = sys.argv[3]
value = sys.argv[4]

# Instanciate an OVH Client.
client = ovh.Client()


result = client.post('/domain/zone/' + domain + '/record',
    fieldType= recordtype,
    subDomain= subdomain,
    target= value,
)


# Pretty print
print json.dumps(result, indent=4)

result = client.post('/domain/zone/' + domain + '/refresh')

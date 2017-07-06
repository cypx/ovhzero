#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import ovh
import json
import sys


if len(sys.argv)!=4:
        print "Error incorrect argument number"
        print "Usage: "+sys.argv[0]+" <DomainName>  <RecordType>  <Subdomain>"
        exit()

domain = sys.argv[1]
recordtype =  sys.argv[2]
subdomain = sys.argv[3]

# Instanciate an OVH Client.
client = ovh.Client()


records = client.get('/domain/zone/' + domain + '/record')

for record_id in records:
    record = client.get('/domain/zone/' + domain + '/record/' + str(record_id))
    if ( record["subDomain"] == subdomain ) and ( record["fieldType"] == recordtype ):
        print json.dumps(record, indent=4)
        delete = client.delete('/domain/zone/' + domain + '/record/' + str(record_id))

#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import ovh
import json
import sys

ip = sys.argv[1]

# create a client
client = ovh.Client()

# Grab domains list
domains = client.get('/domain')

for domain in domains:
    #print domain
    records = client.get('/domain/zone/'+domain+'/record')
    for record in records:
        zone = client.get('/domain/zone/'+domain+'/record/'+str(record))
        #print json.dumps(zone)
        #print zone["fieldType"]+" "+zone["target"]
        if ( zone["fieldType"] == "A" ) and ( zone["target"] == ip ):
            print zone["subDomain"]+"."+domain

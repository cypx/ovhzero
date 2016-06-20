#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import ovh
import json

# create a client
client = ovh.Client()

# Grab domains list
domains = client.get('/domain')

# print raw data
#print domains

# print formatted json
#print json.dumps(domains)

# print readable list
for domain in domains:
    print domain

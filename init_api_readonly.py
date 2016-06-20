#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ovh

# create a client using configuration
client = ovh.Client()

# Request RO,  API access
ck = client.new_consumer_key_request()
ck.add_rules(ovh.API_READ_ONLY, "/")

# Request token
validation = ck.request()

print "Please visit %s to authenticate" % validation['validationUrl']
raw_input("and press Enter to continue...")

# Print nice welcome message
print "Welcome", client.get('/me')['firstname']
print "Btw, your 'consumerKey' is '%s'" % validation['consumerKey']

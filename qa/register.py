#! /bin/env python3

import requests
import sys
import json

def pn_register(addr, key, email):
    # construct contact JSON description
    contact = {"pubkey" : key, "email" : {"address" : email}}
    # expand URL
    if addr[0] == ':':
        addr = 'http://localhost' + addr
    # add registration path according to Peernotify API
    url_path = addr.strip(' /') + '/register'
    # send request
    try:
        r = requests.post(addr + '/register', data=json.dumps(contact))
        if not r.status_code == 200:
            print('Error: ' + r.reason)
    except Exception as e:
        print('Error: ' + str(e))

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage:\n\tregister <addr> <key> <email>')
    else:
        pn_register(sys.argv[1], sys.argv[2], sys.argv[3])
    

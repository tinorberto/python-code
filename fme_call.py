#!/usr/bin/env python3

# Python 3.4 example from the FME Server Developer playground
#
# This script calls the FME Server REST API in order to submit a job.

import urllib.request
import json

SERVER_URL = "http://fme.pbh/"
REPOSITORY = "TESTES"
WORKSPACE = "BUSCAR_ACERVO.fmw"
TOKEN = "fa88907df0f8c04a9d7d366ebdbdd235b5c8d4e4"

# Set up the published parameters as object
params = {
    "publishedParameters" : [
        {
            "name" : "INDICE_CADASTRAL",
            "value" : "007004 007A0319"
        },
        {
            "name" : "DestDataset_JSON",
            "value" : "Y:\TESTE.JSON"
        }
    ]
}

url = '{0}/fmerest/v2/transformations/commands/submit/{1}/{2}'.format(SERVER_URL, REPOSITORY, WORKSPACE)

# Request constructor expects bytes, so we need to encode the string
body = json.dumps(params).encode('utf-8')

headers = {
    'Content-Type' : 'application/json',
    'Accept' : 'application/json',
    'Authorization' : 'fmetoken token={0}'.format(TOKEN)
}

# This will use POST, since we are including data
req = urllib.request.Request(url, body, headers )

r = urllib.request.urlopen(req)

print('Request status: ' + str(r.status))

resp = r.read()
resp = resp.decode('utf-8')
resp = json.loads(resp)
print (resp)

if r.status == 202:
    print('Job ID is {0}'.format(resp['id']))

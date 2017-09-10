#!/usr/bin/python

import jwt
import json
import time
import argparse

SERVICE_ACCOUNT_KEY_FILE = 'service-account.json'

parser = argparse.ArgumentParser()
parser.add_argument('key_file', nargs='?', default=SERVICE_ACCOUNT_KEY_FILE, help='service account key file')
args = parser.parse_args()

key_file = args.key_file

with open(key_file) as f:
    service_account = json.load(f)

# private_key = open('public-key.pem', 'r').read()
# jwt.encode({'some': 'payloiad'}, key=private_key, algorithm='RS256')

payload= {
#  "iss": <account email address>,
  "scope":u"https://www.googleapis.com/auth/cloud-platform",
  "aud":u"https://www.googleapis.com/oauth2/v4/token",
#  "exp": <expiration (epoch)>,
#  "iat":<valid from (epoch)>
}

private_key = service_account[u'private_key']

payload['iss'] = service_account[u'client_email']
iat = int(time.time())
payload['iat'] = iat
payload['exp'] = iat + 3600

jwt = jwt.encode(payload, key=private_key, algorithm='RS256')

print jwt





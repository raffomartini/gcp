#!/usr/bin/python

import jwt
import json
import time

path_to_service_account = 'raffomartini-sandbox-6b93a3fdb649.json'

with open(path_to_service_account) as f:
    service_account = json.load(f)

{u'auth_provider_x509_cert_url': u'https://www.googleapis.com/oauth2/v1/certs',
 u'auth_uri': u'https://accounts.google.com/o/oauth2/auth',
 u'client_email': u'api-1-668@raffomartini-sandbox.iam.gserviceaccount.com',
 u'client_id': u'112620351808172036836',
 u'client_x509_cert_url': u'https://www.googleapis.com/robot/v1/metadata/x509/api-1-668%40raffomartini-sandbox.iam.gserviceaccount.com',
 u'private_key': u'-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDAX2xPJdX6n7cV\nlphNa5NvgxCtt/J7yuiS4lAqYSSoR77MYZUYhSeKeT3HSpAFXaDW5dMgQ5EMJc5b\n90XYZwszeEBC2WXRvo/b5IQlzenH49HbWPzSj/GS5xvt3/dtAEzdpZ4AWNOzRSt1\n1/TcLBrYtbWjVmP5Aw9VKSeACKIlX4mcBamdlLi2pt7YzvNVpwEHjm8D9hMMj3wa\nVmNRkH8psEIAkD2SlgWd+DiDwbF25hfqpM9lF0CdWe5AYW7RyGevdYyHh7bDx1IV\nYqqQkPm23v1k9f6nGj9nZmQ2gTX7KAPhUePnR8OXmeVzgCO6hd4xq/Y9l3c94jXB\nqi5btNbZAgMBAAECggEABInDvkwU07pJ6VtsU/LlmfVNiDbtOcciwdikU5RHgc+b\nzvUUMrgXw5QiYABl7HXQhhKgI/Qqw0P5jdEZT6vM93hUNheBknH/HAzUeBKsW7ky\nbEz5kuCPLlFffEGNiVUJsIFi5wccFbqxdftZGmARJpCxJyLSDdqTqs/t76mUef1F\nXHMqyQZxNUtep+5NT6gtlXmKZvWptKU/rWC81UujZK4YhD4PvSF0paUX7PhKNPU2\nqJR3u59HLYB/Zm9NpcxeC+ajXCLCIuWN983yjhkWa1Exr4yZQJzAbbINmXM3HFfp\nDsIOTgaojFCO+egR+QgtL8M+3Wycj82QH8K/8YV3MQKBgQDuYvslzwpTxrFiwcBF\nuhizscYoJTv8BCnY65aMI1wcSJRfT27DGx6COOhGRM6LrGWHlDN7euqG82wjrx6Z\nF1L83IGYMaLb2DnMfcNwPOe81AXh/rBq+OJFn24v6ZS5UUcxIWhSxw81EmTYOc8b\nmOmqXHcGjpAzfpzmIW9D5iosSQKBgQDOlhoBoDVXjEVxRv53TYavzgRnfXTFxQTL\nC/aUV1KRNDheMHV+qEEfBTRV47RwFyOzO/Z7Rj6dJpdyziJ/cTLws+OfNR+LT4Gm\nWJjCQcgveAjQw3giMyQCWFWZoWxO0I1rcg/nLLb+3B8K+2H/xegyb3k0bZ6f6nCh\nWaSn5Ay2EQKBgQDJyWlUGMxiG9d9hAowO5W7TekxhEshSZjusIUP/MJ0go9tmjxk\n1OjfTDJ5gLbhjj2nJTDq/iHVt+m6zvp0lkS+HB1q6eE0fPR3/6DWugdjVIniQget\nlR1b19eaoPsuXvmHQgMfxrY9s2M/kLeaYbaxaXGrUDQKEsvXFUgszoC2WQKBgQDG\nB/9ABbp8hPtgXiS6anes+Tkhl5Kjrnwsw/gINTjx9nP+XkeTNWjPeqazmsayGIxh\nWR6rBygobwEIzW8maXXiZR7S1BK78Wgf9JfixzpFvrP8oxP6/LkNAm50CdiQKL0X\n/UwfV67H2mxrk5RaofU2u8MdLeO7+fkjwpHjWumQcQKBgE8YrQgrXiinX+bJY998\nuyJTMrlYP1ctZ2pLGv1709Ybhg0FktiZEhIu0f27tzwvOU/7papkhVjxRLBKnGmB\nAR/9WWHHLaPpnd590brPsrwuZqbXiB7QxeuuymNxvHGpWdo5yW62jloxCM7nOi3G\n5aZNhTTid4b2iXWeofomHH0M\n-----END PRIVATE KEY-----\n',
 u'private_key_id': u'6b93a3fdb6493a4594ec95b6b8c5fd94e76a2acf',
 u'project_id': u'raffomartini-sandbox',
 u'token_uri': u'https://accounts.google.com/o/oauth2/token',
 u'type': u'service_account'}

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
payload['exp'] = iat + 3599

jwt = jwt.encode(payload, key=private_key, algorithm='RS256')

print jwt





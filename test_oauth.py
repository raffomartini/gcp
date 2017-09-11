from oauth2client.contrib.gce import AppAssertionCredentials
credentials = AppAssertionCredentials(
    'https://www.googleapis.com/auth/cloud-platform')
from oauth2client.service_account import ServiceAccountCredentials
scope_url='https://www.googleapis.com/auth/cloud-platform'
scopes = [scope_url]
path_to_json = ''
path_to_json = 'raffomartini-sandbox-6b93a3fdb649.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(path_to_json, scopes=scopes)
from httplib2 import Http
http_auth = credentials.authorize(Http())

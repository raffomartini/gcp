import argparse

SERVICE_ACCOUNT_KEY_FILE = 'service-account.json'
parser = argparse.ArgumentParser()
parser.add_argument('key_file', nargs='?', default=SERVICE_ACCOUNT_KEY_FILE, help='service account key file')
args = parser.parse_args()
print args.key_file
import boto3
from botocore.client import Config

# Configuration for NooBaa
NOOBAA_ENDPOINT = 'https://s3-openshift-storage.apps.ocp4.example.com:443'
ACCESS_KEY = '<key>'
SECRET_KEY = '<secret>'
BUCKET_NAME = 'exttestbucket-cb5458a3-c0e0-4c8f-a83c-778b78a23572'


s3 = boto3.resource('s3',
                    endpoint_url=NOOBAA_ENDPOINT,
                    aws_access_key_id=ACCESS_KEY,
                    aws_secret_access_key=SECRET_KEY,
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

for obj in s3.Bucket(BUCKET_NAME).objects.all():
    filename = obj.key
    downfile = f"dl/{filename}"
    s3.Bucket(BUCKET_NAME).download_file(filename, downfile)

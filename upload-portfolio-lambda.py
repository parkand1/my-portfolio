import json
import boto3
from botocore.client import Config
import StringIO
import zipfile

def lambda_handler(event, context):


    s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

    portfolio_bucket = s3.Bucket('andrewpark.io')
    build_bucket = s3.Bucket('codebuildandrewpark')

    portfolio_zip = StringIO.StringIO()
    build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

    with zipfile.ZipFile(portfolio_zip) as myzip:
        for nm in myzip.namelist():
            obj = myzip.open(nm)
            portfolio_bucket.upload_fileobj(obj, nm)
            portfolio_bucket.Object(nm).Acl().put(ACL='public-read')    # TODO implement
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }

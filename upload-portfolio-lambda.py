import botocore
import boto3
from botocore.client import Config
import StringIO
import zipfile
import mimetypes

def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:370032281567:deployPortfolioTopic')

    location = {
        "bucketName" : 'portfolioandrewpark.info',
        "objectKey" : "buildPortfolio.zip"
    }
    try:
        job = event.get("CodePipeline.job")

        if job:
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "BuildArtifact":
                    location = artifact["location"]["s3Location"]

        print "Building portfolio from " + str(location)
        s3 = boto3.resource('s3', config=botocore.client.Config(signature_version='s3v4')

        portfolio_bucket = s3.Bucket('andrewparkportfolio.info')
        build_bucket = s3.Bucket(location["bucketName"])

        buildBucket_zip = StringIO.StringIO()
        build_bucket.download_fileobj(["objectKey"], buildPortfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm)
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')


        print "Job done!"
        topic.publish(Subject="Portfolio Deployed",
             Message="Portfolio deployed successfully!")

        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job['id'])

    except:
        topic.publish(Subject="Portfolio Deploy Failed",
          Message="Portfolio was not deployed successfully.")
        raise


    return 'Hello from Lambda'

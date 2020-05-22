import boto3
client = boto3.resource('s3')
for bucket in client.buckets.all():
    if bucket.name.startswith("karthick"):
       print(bucket.name)
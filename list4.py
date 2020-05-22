import boto3
connection = boto3.client('s3')
response = connection.list_objects(Bucket='karthick-redshift-unload')
print(response)
import boto3
y = boto3.client('s3')
for x in y.list_objects(Bucket='karthick-redshift-unload'):
 print(x)
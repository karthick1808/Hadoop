import boto3
karthick = boto3.client('s3')
response = karthick.create_bucket(Bucket='karthick-selvam-boto4-demo',CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
print(response)
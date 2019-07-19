# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resources('s3')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
for dot in s3.buckets.all():
    print(dot)
    
new_bucket = s3.create_bucket(Bucket='iamabucket-commandlinebyadeboto3', CreateBucketConfiguration={'LocationConstraint':'us-east-1'})
new_bucket = s3.create_bucket(Bucket='iamabucket-commandlinebyadeboto3',
CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
new_bucket1 = s3.create_bucket(Bucket='iamabucket-commandlinebyadeboto3a',
CreateBucketConfiguration={'LocationConstraint':'us-east-2'})
new_bucket2 = s3.create_bucket(Bucket='iamabucket-commandlinebyadeboto3b', CreateBucketConfiguration={'LocationConstraint':'us-east-2'})
get_ipython().run_line_magic('history', '')
for dot in s3.buckets.all():
    print(dot)
    

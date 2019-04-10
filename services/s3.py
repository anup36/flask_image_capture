import cv2
import time
import os
import glob
import boto3
import uuid

session  = boto3.Session(
    aws_access_key_id='aws_access_key_id',
    aws_secret_access_key='aws_secret_access_key',
    region_name='ap-south-1'
)
s3 = session.resource('s3')
bucket = s3.Bucket('cvimg')



def upload_file(path, filename, metaD):
	print 'metaD', metaD
	data=open(path, 'rb')
	result = bucket.put_object(Key=filename, Body=data, ContentType='image/png', Metadata=metaD)
	return result



def get_s3_keys():
	s3 = boto3.client('s3', aws_access_key_id='aws_access_key_id', aws_secret_access_key='aws_secret_access_key', region_name='ap-south-1')

	objects = s3.list_objects(Bucket='cvimg')
	# print objects["Contents"]
	return  objects["Contents"]

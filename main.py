import cv2
import time
import os
import glob
import boto3
import uuid


x = 1

timeout = time.time() + 4  # 5 minutes from now
camera = cv2.VideoCapture(0)
frequency = 2
session  = boto3.Session(
    aws_access_key_id='aws_access_key_id',
    aws_secret_access_key='aws_secret_access_key',
    region_name='ap-south-1'
)
s3 = session.resource('s3')
bucket = s3.Bucket('cvimage')


def upload_file(path, filename):
	data=open(path, 'rb')
	result = bucket.put_object(Key=filename, Body=data)
	print "result", result



while True:

	check, frame = camera.read()

	print str(os.getcwd())+"/images/"+str(int(x))+".png"

	# cv2.imshow('image', frame)
	filename = str(os.getcwd())+"/images/"+str(uuid.uuid4())+".png"
	# frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

	cv2.imwrite(filename, frame)

	x += 1
	if time.time() > timeout:
		break
	time.sleep(frequency);



camera.release()
cv2.destroyAllWindows()




# If grayscal is selected transform image to grayscale and upload 
print glob.glob(os.getcwd()+"/images/*.png")

for file in glob.glob(os.getcwd()+"/images/*.png"):
	print 'file', file
	image = cv2.imread(file)
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imwrite(file, gray_image)
	print file.split("/")[6]
	upload_file(file, file.split("/")[6])





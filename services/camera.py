import cv2
import time
import os
import glob
import boto3
import uuid

max_time_out = 60 # 5 minutes from now


def init():
	return cv2.VideoCapture(0)


def capture(camera, folder, frequency):
	timeout = time.time() + max_time_out  
	while True:

		check, frame = camera.read()


		# cv2.imshow('image', frame)
		filename = folder+str(uuid.uuid4())+".png"
		# frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
		print filename


		cv2.imwrite(filename, frame)

		if time.time() > timeout:
			print 'breaking '
			break
			# return glob.glob(folder+"*.png")
		time.sleep(frequency);



	camera.release()
	cv2.destroyAllWindows()
	return glob.glob(folder+"*.png")

def gray_scale(images):
	for file in images:
		print 'file', file
		image = cv2.imread(file)
		gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		cv2.imwrite(file, gray_image)
		# print file.split("/")[6]
		# upload_file(file, file.split("/")[6])



# def upload_file(path, filename):
# 	data=open(path, 'rb')
# 	result = bucket.put_object(Key=filename, Body=data)
# 	print "result", result



# while True:

# 	check, frame = camera.read()

# 	print str(os.getcwd())+"/images/"+str(int(x))+".png"

# 	# cv2.imshow('image', frame)
# 	filename = str(os.getcwd())+"/images/"+str(uuid.uuid4())+".png"
# 	# frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

# 	cv2.imwrite(filename, frame)

# 	x += 1
# 	if time.time() > timeout:
# 		break
# 	time.sleep(frequency);



# camera.release()
# cv2.destroyAllWindows()
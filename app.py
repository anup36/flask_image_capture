import os
import time
import json
import requests
import shutil
from flask import Flask, render_template, request, url_for, redirect, jsonify
app = Flask(__name__, template_folder="templates")
from services.camera import init, capture, gray_scale
from services.s3 import upload_file, get_s3_keys

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/upload/images', methods=['POST'])
def upload_image():
	# print json.loads(get_s3_keys())	
	try:
		gray = False
		camera = init()
		# print  'frq', type(request.form['freq'])
		images = capture( camera, str(os.getcwd())+"/images/",  int(request.form['freq']) )
		# print "images", images
		if'gray' in request.form:
			print 'image is gray'
			gray_scale(images)
			gray=True

		for file in images:
			upload_file(file, file.split("/")[6], {'gray': str(gray)});

		os.system('rm -rf images/*')

		return jsonify(
	        status=200,
	        msg="Image Upload Done!",
	        listimages='http://localhost:5000/images'
	    )
	except TypeError, e:
		return jsonify(
			status=500,
			msg=e
			)



@app.route('/images', methods=['GET'])
def get_images():
	try:
		images = get_s3_keys()
		result = []
		image_dict = {}
		for img in images:
			image_dict = {}
			# https://s3-ap-southeast-1.amazonaws.com/cvimg
			# print 'img', img['LastModified'], img['Key']
			r=requests.get("https://s3-ap-southeast-1.amazonaws.com/cvimg/"+img['Key'])
			gray_scale =  r.headers['x-amz-meta-gray']	
				
			image_dict['date'] = img['LastModified']
			image_dict['name'] = img['Key']
			image_dict['gray_scale'] =  r.headers['x-amz-meta-gray']
			result.append(image_dict);

		return render_template('listImage.html', data = result)
	except TypeError, e:
		return jsonify(
			status=500,
			msg=e
			)





	


if __name__ == '__main__':
    app.run(debug = True)
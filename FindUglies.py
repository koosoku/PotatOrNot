import urllib
import cv2
import numpy as np
import os

def find_uglies():
	dir = 'neg'
	for file_type in [dir]:
		for img in os.listdir(file_type):
			for ugly in os.listdir('uglies'):
				try:
					current_image_path = str(file_type) + '/' + str(img)
					ugly = cv2.imread('uglies/' + str(ugly))
					question = cv2.imread(current_image_path)

					if ugly.shape == question.shape and not (np.bitwise_xor(ugly,question).any()):
						print('remove ugly')
						print(current_image_path)
						os.remove(current_image_path)

				except Exception as e:
					print (str(e))

find_uglies()
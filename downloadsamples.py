import urllib
import cv2
import numpy as np
import os

def store_raw_images():
	neg_image_links = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n01861778'
	neg_image_urls = urllib.urlopen(neg_image_links).read()

	dir = 'neg'
	if not os.path.exists(dir):
		os.makedirs(dir)

	pic_num = len(next(os.walk(dir))[2])

	for i in neg_image_urls.split('\n'):
		try:
			print(i)
			urllib.urlretrieve(i, dir + '/' + str(pic_num) + '.jpg')
			img = cv2.imread( dir + '/'+ str(pic_num) +'.jpg', cv2.IMREAD_GRAYSCALE)
			resized_image = cv2.resize(img, (100, 100))
			cv2.imwrite( dir + '/'+ str(pic_num) +'.jpg', resized_image)
			pic_num += 1

		except Exception as e:
			print(str(e))
			pic_num -= 1

store_raw_images()
#!/usr/bin/env python3

import argparse
import clipboard
from pyimgur import Imgur

CLIENT_ID = "bb26658e6ad2d9a"

imgur = Imgur(CLIENT_ID)

def upload(files):
	if len(files) == 0:
		return None
	elif len(files) == 1:
		return imgur.upload_image(files[0])
	else:
		print("Gallery uploads are not yet implemented")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Upload images to imgur')
	parser.add_argument('-c', '--copy', action='store_true')
	parser.add_argument('files', action='append')
	args = parser.parse_args()
	
	img = upload(args.files)
	if args.copy:
		clipboard.copy(bytes(img.link, 'UTF-8'))
	else:
		print(img.link)

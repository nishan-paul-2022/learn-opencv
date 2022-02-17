import os
import PIL
import cv2
import math
import shutil
import imutils
import imageio
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, ImageGrab
from moviepy.editor import VideoFileClip

import tkinter as tk
from functools import partial
from tkinter import *
from tkinter.filedialog import askopenfilename, askopenfilenames

plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
plt.margins(0, 0)


def askopen(directory, ask=False, video=False):
	multiple = isinstance(directory, list)
	if ask:
		filetypes = [('Video File', '.mp4')] if video else [('Image File', '.png')]
		functionname = askopenfilenames if multiple else askopenfilename
		path_ = functionname(filetypes=filetypes)
		directory = path_ if path_ else directory
	return directory


def plot_images(window_name, titles, imgs, axis='off', r=None, c=None):
	count = len(imgs)
	if r is None and c is not None:
		r = math.ceil(count / c)
	if c is None and r is not None:
		c = math.ceil(count / r)
	if r is None and c is None:
		r = int(math.sqrt(count))
		c = math.ceil(count / r)
		(r, c) = (1, count) if count < 4 else (2, math.ceil(count/2)) if count <= 6 else (3, 3) if count <= 9 else (r, c)

	plt.close()
	plt.figure().suptitle(window_name)

	for i in range(count):
		title, img = titles[i], imgs[i]
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		plt.subplot(r, c, i + 1)
		plt.title(title)
		plt.axis(axis)
		plt.imshow(img)

	plt.show()


def show_frame(window_name, frame, screens=None, wait_key=25):
	wait_key = 0 if screens is None else wait_key
	cv2.imshow(window_name, frame)
	if cv2.waitKey(wait_key) == ord('q'):
		if screens is not None:
			for screen in screens:
				getattr(screen, 'release')()
		cv2.destroyAllWindows()
		return False
	return True


def show_video(window_name, directory, wait_key=25):
	vCap = cv2.VideoCapture(directory)
	screens = [vCap]
	while vCap.isOpened():
		ret, frame = vCap.read()
		if not ret:
			break
		show_frame(window_name, frame, screens, wait_key)


def put_text_on_image(img, text, coordinate=(35, 35), fontScale=1, color=[255, 0, 0], thickness=2):
	font = cv2.FONT_HERSHEY_SIMPLEX
	img = cv2.putText(img, text, coordinate, font, fontScale, color, thickness, cv2.LINE_AA)
	return img


def _image_merge(frame_a, frame_b):
	ha, wa, ca = frame_a.shape
	hb, wb, cb = frame_b.shape
	H, W = ha + hb, max(wa, wb)
	combined = np.zeros(shape=(H, W, ca), dtype=np.uint8)
	combined[:ha, :wa] = frame_a
	combined[ha:, :wb] = frame_b
	return combined


def image_merge(frames):
	count = len(frames)
	imgs = list()

	for i in range(0, count, 5):
		img = frames[i] if len(frames[i].shape) == 3 else cv2.cvtColor(frames[i], cv2.COLOR_GRAY2BGR)
		for j in range(min(i+1, count), min(i+5, count)):
			frames[j] = frames[j] if len(frames[j].shape) == 3 else cv2.cvtColor(frames[j], cv2.COLOR_GRAY2BGR)
			img = np.hstack((img, frames[j]))
		imgs.append(img)

	number = len(imgs)
	combined = imgs[0]
	for i in range(1, number):
		combined = _image_merge(combined, imgs[i])
	return combined


def image_resize_specified(frame, height_, width_):
	height, width, column = frame.shape
	height_, width_ = int(height * height_), int(width * width_)
	frame_ = cv2.resize(frame, (width_, height_))
	return frame_


def dynamically_create_interface(window_title, function_packages):
	window = Tk()
	window.title(window_title)
	window.minsize(400, 200)

	function_exit = ['EXIT', window.destroy]
	function_packages.append(function_exit)

	count = len(function_packages)
	row = math.ceil(math.sqrt(count))
	column = row

	idx = 0
	for i in range(row):
		for j in range(column):
			if idx >= count:
				break
			function_name = function_packages[idx][0]
			function_set = function_packages[idx][1:]

			button = Button(window, text=function_name, padx=10, pady=10, bg="#2C3333", fg="white", command=partial(*function_set))
			button.grid(row=i, column=j, sticky="NSEW", padx=10, pady=10)
			idx += 1

	for i in range(row):
		Grid.rowconfigure(window, i, weight=1)
	for j in range(column):
		Grid.columnconfigure(window, j, weight=1)

	window.mainloop()

# https://www.geeksforgeeks.org/dynamically-resize-buttons-when-resizing-a-window-using-tkinter/
# https://stackoverflow.com/questions/42920201/how-to-combine-a-rgb-image-with-a-grayed-image-in-opencv
import library
from library import *


def image_resize_bulk(paths):
	imgs = list()
	count = len(paths)
	mean_height, mean_width = 0, 0
	num_of_images = len(paths)

	for path in paths:
		img = cv2.imread(path)
		width, height = img.shape[:2]
		mean_width += width
		mean_height += height
		imgs.append(img)

	mean_height, mean_width = int(mean_width / num_of_images), int(mean_height / num_of_images)

	for i in range(count):
		imgResize = cv2.resize(imgs[i], (mean_width, mean_height), interpolation=cv2.INTER_AREA)
		imgs[i] = imgResize

	return imgs, mean_width, mean_height


def get_frame_list_from_video(path):
	frame_list = []
	vCap = cv2.VideoCapture(path)
	while vCap.isOpened():
		ret, frame = vCap.read()
		if not ret:
			break
		frame_list.append(frame)
	frame_list.pop()
	return frame_list


# https://www.geeksforgeeks.org/opening-multiple-color-windows-to-capture-using-opencv-in-python/
def opening_multiple_color_windows():
	vCap = cv2.VideoCapture(0)
	modes = [cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2HLS, cv2.COLOR_BGR2LAB, cv2.COLOR_BGR2LUV,
	         cv2.COLOR_BGR2XYZ, cv2.COLOR_BGR2YCrCb, cv2.COLOR_BGR2YUV, cv2.COLOR_BGR2RGB]
	screens = [vCap]

	while vCap.isOpened():
		_, frame = vCap.read()
		imgs = [frame]
		for mode in modes:
			img = cv2.cvtColor(frame, mode)
			imgs.append(img)
		combined = library.image_merge(imgs)
		combined = library.image_resize_specified(combined, 0.5, 0.25)
		show_frame('opening_multiple_color_windows', combined, screens)


# https://www.geeksforgeeks.org/python-create-video-using-multiple-images-using-opencv/
def create_video_using_multiple_images():
	video_path = 'zmax/n22_create_video.mp4'
	img_paths = askopen(['zmax/n01_color_conversion.png', 'zmax/n01_color_spaces.png',
	                     'zmax/n01_extract_bgr.png'], ask=True)
	imgs, mean_width, mean_height = image_resize_bulk(img_paths)
	video = cv2.VideoWriter(video_path, -1, 1, (mean_width, mean_height))
	for img in imgs:
		video.write(img)
	video.release()
	show_video('create_video_using_multiple_images', video_path)


# https://www.geeksforgeeks.org/extract-images-from-video-in-python/
def extract_images_from_video():
	directory = 'zmax/n22_extract_images'
	if os.path.exists(directory):
		shutil.rmtree(directory)
	os.makedirs(directory)

	path = askopen('zmax/n22_create_video.mp4')
	vCap = cv2.VideoCapture(path)
	currentframe = 0
	titles = []
	imgs = []

	while vCap.isOpened():
		ret, frame = vCap.read()
		if not ret:
			break
		name = f'{directory}/frame{currentframe}.png'  # if video is still left continue creating zmax
		cv2.imwrite(name, frame)  # writing the extracted zmax
		titles.append(f'{currentframe}')
		imgs.append(frame)
		currentframe += 1

	plot_images('extract_images_from_video', titles, imgs)


# https://theailearner.com/2018/10/16/recording-a-specific-window-using-opencv-python/
def record_computer_screen():
	window_name1 = 'recording_video'
	window_name2 = 'recorded_video'
	path = f'zmax/n22_{window_name2}.mp4'
	imgs = list()

	while True:
		img = ImageGrab.grab(bbox=(0, 0, 400, 800))  # bbox specifies specific region (bbox= x,y,width,height)
		img1 = np.array(img)
		imgs.append(img1)
		if not show_frame(window_name1, img1, screens=[]):
			break

	imageio.mimsave(path, imgs)
	show_video(window_name2, path)


# https://www.geeksforgeeks.org/python-play-video-reverse-mode-using-opencv/
def play_video_in_reverse_mode():
	path = 'zmax/n22_create_video.mp4'
	frame_list = get_frame_list_from_video(path)
	frame_list.reverse()
	for frame in frame_list:
		if not show_frame('play_video_in_reverse_mode', frame, screens=[]):
			break


if __name__ == "__main__":
	function_packages = [
		['opening_multiple_color_windows', opening_multiple_color_windows],
		['create_video_using_multiple_images', create_video_using_multiple_images],
		['extract_images_from_video', extract_images_from_video],
		['record_computer_screen', record_computer_screen],
		['play_video_in_reverse_mode', play_video_in_reverse_mode],
	]

	window_title = 'N22_VIDEO_INTRO'
	dynamically_create_interface(window_title, function_packages)

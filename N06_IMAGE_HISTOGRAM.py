import library
from library import *


def color_image_histogram(img, path, mask=None):
	channels = cv2.split(img)
	colors = ("b", "g", "r")
	for (channel, color) in zip(channels, colors):
		# plt.gca().set_axis_off()
		hist = cv2.calcHist([channel], [0], mask, [256], [0, 256])
		plt.plot(hist, color=color)
	plt.savefig(path)


# https://docs.opencv.org/3.4/d4/d1b/tutorial_histogram_equalization.html
def gray_image_histogram_using_plot_hist():
	path = askopen('zmax/n06_calc_hist.png')
	sample = cv2.imread(path)
	gray = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
	equalized = cv2.equalizeHist(gray)

	titles = ['sample', 'gray', 'equalized', 'histogram', 'histogram_equalized']
	imgs = [sample, gray, equalized]

	for title, img in zip(titles[3:], imgs[1:]):
		# plt.gca().set_axis_off()
		path = f'zmax/n06_plot_hist_{title}.png'
		plt.hist(img.ravel(), 256, [0, 256], fc='k', ec='k')
		plt.savefig(path, bbox_inches='tight')
		img_histogram = cv2.imread(path)
		titles.append(title)
		imgs.append(img_histogram)

	plot_images('gray_image_histogram_using_plot_hist', titles, imgs)


# https://www.pyimagesearch.com/2021/04/28/opencv-image-histograms-cv2-calchist/
def gray_image_histogram_using_calc_hist():
	path = askopen('zmax/n06_calc_hist.png')
	sample = cv2.imread(path)
	gray = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
	histogram = cv2.calcHist([gray], [0], None, [256], [0, 256])
	histogram_normalized = histogram / histogram.sum()

	titles = ['sample', 'gray', 'histogram', 'histogram_normalized']
	imgs = [sample, gray, histogram, histogram_normalized]
	count = len(imgs)

	for i in range(2, count):
		# plt.gca().set_axis_off()
		title, img = titles[i], imgs[i]
		path = f'zmax/n06_calc_hist_{title}.png'
		plt.plot(img)
		plt.savefig(path)
		imgs[i] = cv2.imread(path)

	plot_images('gray_image_histogram_using_calc_hist', titles, imgs)


# https://www.pyimagesearch.com/2021/04/28/opencv-image-histograms-cv2-calchist/
def color_and_masked_image_histogram():
	path = askopen('zmax/n06_calc_hist.png')
	title1, title2 = 'histogram', 'histogram_masked'
	path1, path2 = f'zmax/n06_color_{title1}.png', f'zmax/n06_color_{title2}.png'
	sample = cv2.imread(path)
	mask = np.zeros(sample.shape[:2], dtype="uint8")
	cv2.rectangle(mask, (60, 290), (210, 390), 255, -1)
	masked = cv2.bitwise_and(sample, sample, mask=mask)

	color_image_histogram(sample, path1)
	color_image_histogram(sample, path2, mask=mask)

	histogram = cv2.imread(path1)
	histogram_masked = cv2.imread(path2)

	titles = ['sample', 'mask', 'masked', title1, title2]
	imgs = [sample, mask, masked, histogram, histogram_masked]
	plot_images('color_and_masked_image_histogram', titles, imgs)


if __name__ == "__main__":
	function_packages = [
		['gray_image_histogram_using_plot_hist', gray_image_histogram_using_plot_hist],
		['gray_image_histogram_using_calc_hist', gray_image_histogram_using_calc_hist],
		['color_and_masked_image_histogram', color_and_masked_image_histogram],
	]

	window_title = 'N06_IMAGE_HISTOGRAM'
	dynamically_create_interface(window_title, function_packages)

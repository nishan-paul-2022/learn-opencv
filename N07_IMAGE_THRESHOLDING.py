import library
from library import *


# https://docs.opencv.org/4.4.0/d7/d4d/tutorial_py_thresholding.html
def simple_thresholding():
	path = askopen('zmax/n07_simple.png')
	img = cv2.imread(path, 0)
	_, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
	_, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
	_, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
	_, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
	_, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

	titles = ['GRAY', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
	imgs = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
	plot_images('simple_thresholding', titles, imgs)


# https://docs.opencv.org/4.4.0/d7/d4d/tutorial_py_thresholding.html
def adaptive_thresholding():
	path = askopen('zmax/n07_adaptive.png')
	img0 = cv2.imread(path)
	img1 = cv2.imread(path, 0)
	img2 = cv2.medianBlur(img1, 5)
	_, th1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
	th2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
	th3 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

	titles = ['sample', 'gray', 'median_blur', 'global_thresholding (v = 127)', 'adaptive_mean_thresholding', 'adaptive_gaussian_thresholding']
	imgs = [img0, img1, img2, th1, th2, th3]
	plot_images('adaptive_thresholding', titles, imgs)


# https://docs.opencv.org/4.4.0/d7/d4d/tutorial_py_thresholding.html
def otsu_thresholding():
	path = askopen('zmax/n07_otsu.png')
	img = cv2.imread(path, 0)

	_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # global thresholding
	_, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Otsu's thresholding
	blur = cv2.GaussianBlur(img, (5, 5), 0)  # Otsu's thresholding after Gaussian filtering
	ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

	titles = ['noisy_image', 'noisy_image', 'gaussian_filtered_image',
	          'Global Thresholding (v=127)', "Otsu's Thresholding", "Otsu's Thresholding",
	          'histogram', 'histogram', 'histogram']
	images = [img, img, blur, th1, th2, th3]

	for i in range(3):
		plt.gca().set_axis_off()
		path = f'zmax/n07_otsu_{i}.png'
		plt.hist(images[i].ravel())
		plt.savefig(path)
		img = cv2.imread(path)
		images.append(img)

	plot_images('otsu_thresholding', titles, images)


if __name__ == "__main__":
	function_packages = [
		['simple_thresholding', simple_thresholding],
		['adaptive_thresholding', adaptive_thresholding],
		['otsu_thresholding', otsu_thresholding],
	]

	window_title = 'N07_IMAGE_THRESHOLDING'
	dynamically_create_interface(window_title, function_packages)
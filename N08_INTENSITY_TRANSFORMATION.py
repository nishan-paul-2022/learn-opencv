import library
from library import *


# https://www.geeksforgeeks.org/python-intensity-transformation-operations-on-images/
def log_transformation_of_image_intensity():
	path = askopen('zmax/n08_intensity.png')
	sample = cv2.imread(path)
	c = 255 / (np.log(1 + np.max(sample)))  # Apply log transform
	log_transformed = c * np.log(1 + sample)
	log_transformed = np.array(log_transformed, dtype=np.uint8)  # Specify the data type
	titles = ['sample', 'log_transformed']
	imgs = [sample, log_transformed]
	plot_images('log_transformation_of_image_intensity', titles, imgs)


# https://www.geeksforgeeks.org/python-intensity-transformation-operations-on-images/
def power_law_gamma_transformation_of_image_intensity():
	path = askopen('zmax/n08_intensity.png')
	sample = cv2.imread(path)
	titles = ['sample']
	imgs = [sample]
	for gamma in [0.1, 0.5, 1.2, 2.2]:  # Trying 4 gamma values.
		gamma_corrected = np.array(255 * (sample / 255) ** gamma, dtype='uint8')  # Apply gamma correction.
		imgs.append(gamma_corrected)
		titles.append(f'gamma {gamma}')
	plot_images('power_law_gamma_transformation_of_image_intensity', titles, imgs)


if __name__ == '__main__':
	function_packages = [
		['log_transformation_of_image_intensity', log_transformation_of_image_intensity],
		['power_law_gamma_transformation_of_image_intensity', power_law_gamma_transformation_of_image_intensity],
    ]

	window_title = 'N08_INTENSITY_TRANSFORMATION'
	dynamically_create_interface(window_title, function_packages)

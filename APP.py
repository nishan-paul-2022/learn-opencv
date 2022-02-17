import N01_BASIC
import N02_DRAW_ON_IMAGE
import N03_IMAGE_MANIPULATION
import N04_ARITHMETC_AND_BITWISE_OPERATION
import N05_IMAGE_PROCESSING
import N06_IMAGE_HISTOGRAM
import N07_IMAGE_THRESHOLDING
import N08_INTENSITY_TRANSFORMATION
import N09_MORPHOLOGICAL_OPERATION
import N10_GET_COORDINATE
import N11_EROSION_AND_DILATION
import N12_EXTRACT_OBJECTS
import N14_IMAGE_SEGMENTATION
import N15_FIELD_DETECTION
import N16_CONTOUR_DETECTION
import N19_CIRCLE_DETECTION
import N18_CORNER_DETECTION
import N17_DOT_DETECTION
import N20_BLOB_DETECTION
import N21_LINE_DETECTION
import N22_VIDEO_INTRO
import N23_DRAW_ON_WEBCAM
import N24_FACE_DETECTION
import N25_INVISIBLE_CLOAK
import N26_EXTRACTION_AND_SUBTRACTION
import N27_COLOR_SEGMENTATION
import N28_LANE_LINE_DETECTION
from library import *


if __name__ == '__main__':
	function_packages = [
		['image_read', N01_BASIC.image_read],
		['image_write', N01_BASIC.image_write],
		['get_image_height_and_width', N01_BASIC.get_image_height_and_width],
		['extract_bgr_value_of_pixel', N01_BASIC.extract_bgr_value_of_pixel],
		['bgr_color_palette', N01_BASIC.bgr_color_palette],
		['color_spaces_of_image', N01_BASIC.color_spaces_of_image],
		['color_conversion_of_image', N01_BASIC.color_conversion_of_image],
		['extract_user_defined_region_of_image', N01_BASIC.extract_user_defined_region_of_image],

		['draw_straight_line', N02_DRAW_ON_IMAGE.draw_straight_line],
		['draw_arrowed_line', N02_DRAW_ON_IMAGE.draw_arrowed_line],
		['draw_polyline', N02_DRAW_ON_IMAGE.draw_polyline],
		['draw_ellipse', N02_DRAW_ON_IMAGE.draw_ellipse],
		['draw_circle', N02_DRAW_ON_IMAGE.draw_circle],
		['draw_rectangle', N02_DRAW_ON_IMAGE.draw_rectangle],
		['draw_triangle', N02_DRAW_ON_IMAGE.draw_triangle],

		['image_generating', N03_IMAGE_MANIPULATION.image_generating],
		['image_bordering', N03_IMAGE_MANIPULATION.image_bordering],
		['image_pyramid', N03_IMAGE_MANIPULATION.image_pyramid],
		['image_grayscaling', N03_IMAGE_MANIPULATION.image_grayscaling],
		['image_scaling', N03_IMAGE_MANIPULATION.image_scaling],
		['image_rotating', N03_IMAGE_MANIPULATION.image_rotating],
		['image_shifting', N03_IMAGE_MANIPULATION.image_shifting],

		['arithmetic_addition', N04_ARITHMETC_AND_BITWISE_OPERATION.arithmetic_addition],
		['arithmetic_subtraction', N04_ARITHMETC_AND_BITWISE_OPERATION.arithmetic_subtraction],
		['bitwise_and', N04_ARITHMETC_AND_BITWISE_OPERATION.bitwise_and],
		['bitwise_or', N04_ARITHMETC_AND_BITWISE_OPERATION.bitwise_or],
		['bitwise_xor', N04_ARITHMETC_AND_BITWISE_OPERATION.bitwise_xor],
		['bitwise_not', N04_ARITHMETC_AND_BITWISE_OPERATION.bitwise_not],

		['image_blurring', N05_IMAGE_PROCESSING.image_blurring],
		['image_denoising', N05_IMAGE_PROCESSING.image_denoising],
		['image_inpainting', N05_IMAGE_PROCESSING.image_inpainting],
		['image_bilateral_filtering', N05_IMAGE_PROCESSING.image_bilateral_filtering],
		['image_cartooning', N05_IMAGE_PROCESSING.image_cartooning],
		['image_registration', N05_IMAGE_PROCESSING.image_registration],

		['gray_image_histogram_using_plot_hist', N06_IMAGE_HISTOGRAM.gray_image_histogram_using_plot_hist],
		['gray_image_histogram_using_calc_hist', N06_IMAGE_HISTOGRAM.gray_image_histogram_using_calc_hist],
		['color_and_masked_image_histogram', N06_IMAGE_HISTOGRAM.color_and_masked_image_histogram],

		['simple_thresholding', N07_IMAGE_THRESHOLDING.simple_thresholding],
		['adaptive_thresholding', N07_IMAGE_THRESHOLDING.adaptive_thresholding],
		['otsu_thresholding', N07_IMAGE_THRESHOLDING.otsu_thresholding],

		['log_transformation_of_image_intensity', N08_INTENSITY_TRANSFORMATION.log_transformation_of_image_intensity],
		['power_law_gamma_transformation_of_image_intensity', N08_INTENSITY_TRANSFORMATION.power_law_gamma_transformation_of_image_intensity],

		['morphological_operation', N09_MORPHOLOGICAL_OPERATION.morphological_operation],
		['image_segmentation_using_morphological_operation', N09_MORPHOLOGICAL_OPERATION.image_segmentation_using_morphological_operation],

		['get_coordinate_of_clicked_point', N10_GET_COORDINATE.get_coordinate_of_clicked_point],

		['erosion_and_dilation', N11_EROSION_AND_DILATION.erosion_and_dilation],

		['extract_objects_from_image_using_cursor', N12_EXTRACT_OBJECTS.extract_objects_from_image_using_cursor],
		['extract_objects_from_image_using_contour_detection', N12_EXTRACT_OBJECTS.extract_objects_from_image_using_contour_detection],

		['image_segmentation_using_watershed_algorithm', N14_IMAGE_SEGMENTATION.image_segmentation_using_watershed_algorithm],

		['field_detection_using_template_matching', N15_FIELD_DETECTION.field_detection_using_template_matching],

		['contour_detection_summarized', N16_CONTOUR_DETECTION.contour_detection_summarized],
		['contour_detection_detailed', N16_CONTOUR_DETECTION.contour_detection_detailed],

		['dot_detection_from_binary_image', N17_DOT_DETECTION.dot_detection_from_binary_image],
		['dot_detection_from_specific_colored_image', N17_DOT_DETECTION.dot_detection_from_specific_colored_image],

		['corner_detection_using_harris_raw', N18_CORNER_DETECTION.corner_detection_using_harris_raw],
		['corner_detection_using_harris_builtin', N18_CORNER_DETECTION.corner_detection_using_harris_builtin],
		['corner_detection_using_shi_tomasi', N18_CORNER_DETECTION.corner_detection_using_shi_tomasi],

		['circle_detection', N19_CIRCLE_DETECTION.circle_detection],

		['blob_detection', N20_BLOB_DETECTION.blob_detection],

		['line_detection_from_image', N21_LINE_DETECTION.line_detection_from_image],

		['opening_multiple_color_windows', N22_VIDEO_INTRO.opening_multiple_color_windows],
		['create_video_using_multiple_images', N22_VIDEO_INTRO.create_video_using_multiple_images],
		['extract_images_from_video', N22_VIDEO_INTRO.extract_images_from_video],
		['record_computer_screen', N22_VIDEO_INTRO.record_computer_screen],
		['play_video_in_reverse_mode', N22_VIDEO_INTRO.play_video_in_reverse_mode],

		['draw_on_webcam', N23_DRAW_ON_WEBCAM.draw_on_webcam],

		['face_detection_using_haarcascades', N24_FACE_DETECTION.face_detection_using_haarcascades],

		['invisible_cloak', N25_INVISIBLE_CLOAK.invisible_cloak],

		['foreground_extraction_using_grabcut_algorithm', N26_EXTRACTION_AND_SUBTRACTION.foreground_extraction_using_grabcut_algorithm],
		['background_subtraction_using_mog2', N26_EXTRACTION_AND_SUBTRACTION.background_subtraction_using_mog2],
		['background_subtraction_using_running_average_concept', N26_EXTRACTION_AND_SUBTRACTION.background_subtraction_using_running_average_concept],

		['color_segmentation_to_identify_specific_color', N27_COLOR_SEGMENTATION.color_segmentation_to_identify_specific_color],

		['lane_line_detection_from_video', N28_LANE_LINE_DETECTION.lane_line_detection_from_video]
	]

	window_title = 'APP'
	dynamically_create_interface(window_title, function_packages)

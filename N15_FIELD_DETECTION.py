import library
from library import *


# Function to Generate bounding boxes around detected fields
def get_boxed(img, gray, template, field_name):
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)  # Apply template matching
    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(res)
    # field_threshold = {'docu_prev_policy_no': 0.9, 'docu_address': 0.73, 'docu_tamil': 0.8, 'pro_batman': 0.59, 'pro_ironman': 0.8}
    # hits = np.where(res >= field_threshold[field_name])
    hits = np.where(res == np.max(res))

    color1 = [255, 0, 0]
    color2 = [0, 255, 0]
    thickness = 2

    for point in zip(*hits[::-1]):  # Draw a rectangle around the matched region.
        cv2.rectangle(img, point, (point[0] + w, point[1] + h), color1, thickness)
        y = point[1] - 10 if point[1] - 10 > 10 else point[1] + h + 20
        put_text_on_image(img, field_name, (point[0], y), 0.8, color2, thickness)

    return img


# https://www.geeksforgeeks.org/python-document-field-detection-using-template-matching/
# https://github.com/VivekKrG/Image-field-detection-using-template-matching-using-openCV
def field_detection_using_template_matching():
    lamdaA = lambda path: os.path.basename(path).replace('.png', '')
    paths = askopen(['zmax/n15_a.png', 'zmax/n15_a_address.png', 'zmax/n15_a_prev_policy_no.png', 'zmax/n15_a_tamil_nadu.png'])
    sample = cv2.imread(paths[0])
    result = sample.copy()
    gray = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)  # 3d to 2d conversion

    n = len(paths)
    for i in range(1, n):
        template = cv2.imread(paths[i], 0)  # Field templates
        field_name = lamdaA(paths[i])
        get_boxed(result, gray, template, field_name)

    titles = ['sample', 'detected_fields']
    imgs = [sample, result]
    plot_images('field_detection_using_template_matching', titles, imgs)


if __name__ == '__main__':
    function_packages = [
        ['field_detection_using_template_matching', field_detection_using_template_matching],
    ]

    window_title = 'N15_FIELD_DETECTION'
    dynamically_create_interface(window_title, function_packages)
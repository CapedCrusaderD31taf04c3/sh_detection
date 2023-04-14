__copyright__ = """
SalonAI 2023 
Developer : SNK
"""

import dlib
import numpy as np

from cv2_utils import (
    read_image, convert_color_to_gray,
    draw_filled_point_and_add_number,
    show_image_and_wait,
    get_masked_image,
    resize_image_by_percentage,
    save_image_at_path
)
from utils import distance_by_subtraction

IMAGE = "img/henry.jpg"
DAT_FILE = "dat_file/shape_predictor_68_face_landmarks.dat"


def save_mask_image(image_path, image_save_path):
    # Arrange
    image_3_chan_col = read_image(image_path)
    image_2_chan_gray = convert_color_to_gray(image_3_chan_col)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(DAT_FILE)

    faces = detector(image_2_chan_gray)
    landmark_points = []
    for face in faces:
        landmarks = predictor(image_2_chan_gray, face)

        for n in range(0,68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y

            landmark_points.append([x,y])

        # 68
        x_68 = int(landmark_points[21][0] + (distance_by_subtraction([landmark_points[22][0], landmark_points[21][0]])))
        temp_y_68 = distance_by_subtraction([landmark_points[22][1], landmark_points[21][1]])
        y_68 = int(( landmark_points[21][1] if landmark_points[21][1] <= landmark_points[22][1] else landmark_points[22][1] ) - temp_y_68)
        landmark_points.append([x_68, y_68])

        # 69
        y_69 = int(y_68 - abs(landmark_points[33][1] - y_68))
        landmark_points.append([x_68, y_69])

        # 70
        landmark_points.append([landmark_points[18][0], y_69])

        # 71
        landmark_points.append([landmark_points[25][0], y_69])

        # Draw point and text
        # image_3_chan_col = draw_filled_point_and_add_number(image_3_chan_col, location_points=landmark_points)


    # Draw Convex hull for point wrapping
    if not landmark_points:
        return False
    polygon_points = []
    for n in range(0,71+1):
        if n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 70, 71]:
            polygon_points.append(landmark_points[n])


    # get masked image
    masked_image = get_masked_image(image_3_chan_col, polygon_points)

    # resize image at specific percentage
    result_image = resize_image_by_percentage(masked_image, 20)

    # show and wait
    # show_image_and_wait(result_image)

    # save File
    save_image_at_path(image_save_path, result_image)

    return True
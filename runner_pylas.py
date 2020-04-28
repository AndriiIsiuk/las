import colorsys

import cv2
import numpy as np

import pylas


def eightbitify(colour):
    return colour/256

def to_hsv(rgb: np.ndarray):
    empty_image = np.zeros((1, 1, 3), dtype=np.uint8)
    empty_image[0, 0] = list(rgb)
    # empty_image[0, 0] = rgb
    hsv = cv2.cvtColor(empty_image, cv2.COLOR_RGB2HSV)
    return np.array(list(hsv[0, 0]))

# def rgb2hsv(rgb):
#     """ convert RGB to HSV color space
#
#     :param rgb: np.ndarray
#     :return: np.ndarray
#     """
#     print("111111111111 ===== ", rgb)
#     rgb = np.array(rgb)
#     print("222222222222 ===== ", rgb)
#
#     rgb = rgb.astype('float')
#     maxv = np.amax(rgb)
#     maxc = np.argmax(rgb)
#     minv = np.amin(rgb)
#     minc = np.argmin(rgb)
#
#     hsv = np.zeros(rgb.shape, dtype='float')
#     hsv[maxc == minc, 0] = np.zeros(hsv[maxc == minc, 0].shape)
#     hsv[maxc == 0, 0] = (((rgb[..., 1] - rgb[..., 2]) * 60.0 / (maxv - minv + np.spacing(1))) % 360.0)[maxc == 0]
#     hsv[maxc == 1, 0] = (((rgb[..., 2] - rgb[..., 0]) * 60.0 / (maxv - minv + np.spacing(1))) + 120.0)[maxc == 1]
#     hsv[maxc == 2, 0] = (((rgb[..., 0] - rgb[..., 1]) * 60.0 / (maxv - minv + np.spacing(1))) + 240.0)[maxc == 2]
#     hsv[maxv == 0, 1] = np.zeros(hsv[maxv == 0, 1].shape)
#     hsv[maxv != 0, 1] = (1 - minv / (maxv + np.spacing(1)))[maxv != 0]
#     hsv[..., 2] = maxv
#
#     return hsv

def convert_color(rgb_16: np.ndarray)->np.ndarray:
    converted_color = np.array([int(eightbitify(rgb_16[0])), int(eightbitify(rgb_16[1])), int(eightbitify(rgb_16[2]))])
    converted_hsv = to_hsv(converted_color)
    return converted_hsv

# Directly read and write las


data_file = 'data/W2 .las'
filtered_file = 'data/filtered_points.las'
coopy = 'data/filtered_points_good_copy.las'
# data_file = coopy

las = pylas.read(data_file)
print(las)


# las = pylas.convert(las, point_format_id=2)
# las.write('data/converted.las')

# Open data to inspect header and then read
with pylas.open(data_file) as f:
    las = f.read()


median = np.median(las.points['Z'])
mean = np.mean(las.points['Z'])
good_idx = np.where(las.points['Z'] < mean)
filtered_points = np.take(las.points, good_idx)
reduced_shape_points = np.squeeze(filtered_points)


print("START1 = ", reduced_shape_points.shape)
print("START2 = ", las.points.shape)
print("==== ", las.points)


bad_idx = np.where(las.points['Z'] >= mean*1.05)
bad_ffp= np.take(las.points, bad_idx)
reduced_bad_ffp = np.squeeze(bad_ffp)

colors = reduced_bad_ffp[["red", "green", 'blue']]
vf = np.vectorize(convert_color)
converted = vf(colors[:10])

filered_colors = 150 < converted[0] < 250

#todo funkcja, ktora sprawdzi czy kolor jest powyzej czy ponizej

import pdb;pdb.set_trace()

# for color in colors:
#     converted = convert_color(color)

# import pdb;pdb.set_trace()



# filtered_points.write('data/filtered_points.las')
new_test1 = pylas.create(point_format_id=2)
new_test1.points = reduced_bad_ffp
new_test1.vlrs = las.vlrs
new_test1.header = las.header
new_test1.write('data/filtered_points_experiments.las')


print(11111251552, las.points_data)

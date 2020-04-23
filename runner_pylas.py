import colorsys

import cv2
import numpy as np

import pylas


def eightbitify(colour):
    # notzero = np.where(colour > 0)
    # colour[notzero] = (colour[notzero]/255) - 1
    return (colour/255)-1



data_file = 'data/W2 .las'
filtered_file = 'data/filtered_points.las'

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

new_test1 = pylas.create(point_format_id=2)
new_test1.points = reduced_shape_points
new_test1.vlrs = las.vlrs
new_test1.header = las.header
new_test1.write('data/filtered_points_1.las')


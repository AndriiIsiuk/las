import numpy as np

import pylas
from pylas.lasdatas import base, las14

# Directly read and write las
from pylas.point import record

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
    # if f.header.point_count < 10 ** 8:
    las = f.read()


median = np.median(las.points['Z'])
mean = np.mean(las.points['Z'])
good_idx = np.where(las.points['Z'] < mean)

filtered_points = np.take(las.points, good_idx)
redused_shape_points = np.squeeze(filtered_points)


print("START1 = ", redused_shape_points.shape)
print("START2 = ", las.points.shape)




# filtered_points.write('data/filtered_points.las')
new_test1 = pylas.create(point_format_id=2)
new_test1.points = redused_shape_points
new_test1.vlrs = las.vlrs
new_test1.header = las.header
new_test1.write('data/filtered_points2.las')


print(11111251552, las.points_data)

# points_1 = record.PackedPointRecord.from_point_record(
#         las.points_data, 2
#     )

# las_new_test1 = las14.LasData(header=las.header, vlrs=las.vlrs, points=filtered_points)
# las_new_test1 = pylas.create(point_format_id=2)
# las_new_test1.points = filtered_points
# las_new_test1.vlrs = las.vlrs
# las_new_test1.header = las.header
# print(21151251552, las_new_test1.points_data)
# points_2 = record.PackedPointRecord.from_point_record(
#         las_new_test1.points_data, 2
#     )


# las_new_test1.write('data/filtered_points2.las')


# new_test2_good = pylas.create(point_format_id=2)
# new_test2_good.points = las.points
# new_test2_good.vlrs = las.vlrs
# new_test2_good.header = las.header
# new_test2_good.write('data/filtered_points_good_copy.las')


# new_las = base.LasBase(header = las.header, vlrs=las.vlrs, points=filtered_points)
# new_las.write('data/filtered_points.las')




# with pylas.open('data/W2 .las') as fh:
#     print('Points from Header:', fh.header.point_count)
#     las = fh.read()
#     print(las)
#     print('Points from data:', len(las.points))
#     ground_pts = las.classification == 2
#     import pdb;pdb.set_trace()
#     print(2222, las[0])
#     print(3333, ground_pts)
#
#     bins, counts = np.unique(las.return_number[ground_pts], return_counts=True)
#     print('Ground Point Return Number distribution:')
#     print(8888, bins)
#     print(9999, bins)
#     for r,c in zip(bins,counts):
#         print('    {}:{}'.format(r,c))
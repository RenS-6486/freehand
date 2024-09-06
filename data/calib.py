
import csv

import numpy as np

def read_calib_matrices(filename_calib, resample_factor):
    # T{image->tool} = T{image_mm -> tool} * T{image_pix -> image_mm} * T{resampled_image_pix -> image_pix}
    tform_calib = np.empty((8,4), np.float32)
    with open(filename_calib, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')  
        i = 0
        for row in csv_reader:
            print(row)
            if i not in [0, 5, 10, 11]:
                #tform_calib[i,:] = (list(map(float,row)))
                i += 1
        raise ValueError('A very specific bad thing happened.')
    return tform_calib[4:8,:] @ tform_calib[0:4,:] @ np.array([[resample_factor,0,0,0], [0,resample_factor,0,0], [0,0,1,0], [0,0,0,1]], np.float32)

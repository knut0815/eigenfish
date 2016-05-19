import numpy
import scipy.misc


def load_img_mat(files):
    shape = scipy.misc.imread(files[0], True).shape
    img_mat = numpy.empty((shape[0] * shape[1], len(files)))
    for i, file in enumerate(files):
        img_mat[:, i] = scipy.misc.imread(file, True).flatten()
    return img_mat

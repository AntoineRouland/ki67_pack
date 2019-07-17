import logging

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.exposure import equalize_adapthist
from skimage.filters import gaussian
from skimage.transform import resize
from skimage.color import rgb2lab

from seg.segmentation import segmentation
from seg.utils import apply_on_normalized_luminance, outline_regions
from seg.fct import ki_67_percentage
from seg.data_loader import *


def ki67_segmentation(original_image,
                      positive_color=np.array([16.36, 110.89, 53.06]),
                      negative_color=np.array([53.15, -18.15, 1.20]),
                      background_color=np.array([53.15, -18.15, 1.20]),
                      sigma=0.454,
                      resize_factor=8,
                      visualize_regions=False):
    """ This function takes an image and return the ratio for cells marked by the ki-67 antigen.
    Also, it plots on the initial image the regions that the algorithm considers as positives cells,
    negatives cells or background.
    The parameters by default are the ones which work good with the images I have worked with.

    :param original_image: original image with cells, without pre process
    :param positive_color: color of positives cells as a np.array, in the color lab space,
    np.array([16.36, 110.89, 53.06]) by default
    :param negative_color: color of negatives cells as a np.array, in the color lab space,
    np.array([53.15, -18.15, 1.20]) by default
    :param background_color: color of the background as a np.array, in the color lab space,
    np.array([53.15, -18.15, 1.20]) by default
    :param sigma: variance of the 2 dimensional gaussian for the weight matrix, 0.454 by default
    :param resize_factor: to resize the original image, 8 by default
    :param visualize_regions: boolean, False by default
    :return: the ratio of positives cells
    """

    logging.info('Resizing')
    resize_original = (resize(original_image,
                              (int(original_image.shape[0] / resize_factor), (original_image.shape[1] / resize_factor)),
                              anti_aliasing=True))

    image = apply_on_normalized_luminance(
        operation=lambda img: gaussian(img, sigma=2),
        image_rgb=original_image)

    image = apply_on_normalized_luminance(
        lambda img: equalize_adapthist(img, clip_limit=0.02),
        image_rgb=image)

    image_lab = rgb2lab(image)

    logging.info('Resizing')
    resize_factor = 8
    image_lab = resize(image_lab, (int(image.shape[0] / resize_factor), (image.shape[1] / resize_factor)),
                       anti_aliasing=True)

    all_mask = segmentation(image_lab,
                            brown_lab=positive_color,
                            blue_lab=negative_color,
                            white_lab=background_color,
                            sigma=sigma)

    regions_positive = outline_regions(resize_original[5:resize_original.shape[0] - 5,
                                       5:resize_original.shape[1] - 5], all_mask[0, :, :])

    regions_negative = outline_regions(resize_original[5:resize_original.shape[0] - 5,
                                       5:resize_original.shape[1] - 5], all_mask[1, :, :])

    regions_background = outline_regions(resize_original[5:resize_original.shape[0] - 5,
                                         5:resize_original.shape[1] - 5], all_mask[2, :, :])

    p = ki_67_percentage(all_mask[0, :, :], all_mask[1, :, :])

    if visualize_regions:
        plt.subplot(221)
        plt.imshow(original_image)
        plt.title("Original Image")
        plt.subplot(222)
        plt.imshow(regions_positive)
        plt.title("Positives cells")
        plt.subplot(223)
        plt.imshow(regions_negative)
        plt.title("Negatives Cells")
        plt.subplot(224)
        plt.imshow(regions_background)
        plt.title("Background")
        plt.show()
    return p


def load_data():
    """ This function loads 5 examples of images and the positive and negative masks associated with each images.

    :return: a list of dictionary with the followed keys : "sample_name", "original_image", "positive_mask"
    and "negative_mask".
    """
    names = references_names()
    ref_paths = []
    ori_paths = []
    data = []

    for i in range(len(names)):
        ref_paths.append(references_paths(names[i]))
        ori_paths.append(originals_paths(names[i]))

    nb_images = len(ref_paths)
    for j in range(nb_images):
        d = dict()
        d["sample_name"] = names[j]
        d["original_image"] = io.imread(ori_paths[j][0])
        d["positive_mask"] = io.imread(ref_paths[j][0])
        d["negative_mask"] = io.imread(ref_paths[j][1])
        data.append(d)

    return data

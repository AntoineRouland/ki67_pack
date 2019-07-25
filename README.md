To install, type in terminal:

`pip install ki67segmentation`

Then:

`from cells_detection.ki67_segmentation import ki67_segmentation, load_data`

This package contains two functions :

`ki67_segmentation(original_image,
                  positive_color=np.array([16.36, 110.89, 53.06]),
                  negative_color=np.array([53.15, -18.15, 1.20]),
                  background_color=np.array([53.15, -18.15, 1.20]),
                  sigma=0.454,
                  resize_factor=8,
                  visualize_regions=False):`
                      
    This function takes an image and return the ratio for cells marked by the ki-67 antigen.
    Also, it is able to plot on the initial image the regions that the algorithm considers as positives cells,
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
    
    
`load_data():`

    This function loads 5 examples of images and the positive and negative masks associated with each images.

    :return: a list of dictionary with the followed keys : "sample_name", "original_image", "positive_mask"
    and "negative_mask".
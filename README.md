This package contains two functions :

-ki67_segmentation(original_image,
                      positive_color=np.array([16.36, 110.89, 53.06]),
                      negative_color=np.array([53.15, -18.15, 1.20]),
                      background_color=np.array([53.15, -18.15, 1.20]),
                      sigma=0.454,
                      resize_factor=8,
                      visualize_regions=False):
                      
  This function takes an image and return the ratio for cells marked by the ki-67 antigen.
    Also, it plots on the initial image the regions that the algorithm considers as positives cells,
    negatives cells or background.
    The parameters by default are the ones which work good with the images I have worked with.
    
    
-def load_data():

This function loads 5 examples of images and the positive and negative masks associated with each images.
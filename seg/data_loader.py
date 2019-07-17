import os
import warnings

FOLDER_REFERENCES = 'References'

warnings.filterwarnings("ignore", category=UserWarning)


def root_dir(*args):
    return os.path.abspath(os.path.join(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir, *args)))


def references_names():
    path_data = root_dir(FOLDER_REFERENCES)
    return [name for name in os.listdir(path_data)
            if os.path.isdir(os.path.join(path_data, name))]


def references_paths(references_name):
    path_images = root_dir(FOLDER_REFERENCES, references_name)
    return [os.path.join(path_images, name) for name in os.listdir(path_images)
            if os.path.splitext(os.path.join(path_images, name))[1] == '.png']


def originals_paths(references_name):
    path_images = root_dir(FOLDER_REFERENCES, references_name)
    return [os.path.join(path_images, name) for name in os.listdir(path_images)
            if os.path.splitext(os.path.join(path_images, name))[1] == '.jpg']

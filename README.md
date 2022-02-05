# DatasetBuilder
> If not already, follow the guide video found: XXX


Utilize cv2 tracking to track a bounding box to your objects in a video. Creates the image files of video frames and the annotation data in PASCAL VOC format. This data can then be trained by utilzing the [Object Detection with TensorFlow Lite Model Maker](https://colab.research.google.com/github/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/tutorials/model_maker_object_detection.ipynb)
## FTC Notes
- If you are not already using FTC-ML(FTC Machine Learning Tool Chain), please use the FTC-ML as it provides better resources and accessibility to most FTC Teams.
- Only use this method if you are running into issues with the FTC-ML, as this process for building data is less accessible and relies on computer resources.
## Setup
> This program has only been tested on windows operating systems, you may find issues when using other operating systems.
- Install [Python 3.8](https://www.python.org/downloads/release/python-3812/) or install [Anaconda](https://www.anaconda.com/products/individual)
> Recommened to use the Anaconda method
- (Anaconda)Open a terminal, either cmd or powershell, and create a anaconda virtual enviornment by typing `conda create -n datacreate python=3.8`
- (Anaconda)Open the virtual enviornment by typing `conda activate datacreate'
- 

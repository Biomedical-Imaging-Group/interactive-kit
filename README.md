# IPLabViewer
Interactive image visualization tool for Jupyter notebook based on [matplotlib](https://matplotlib.org/) and [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/). 

## Purpose of the Project
This project has the goal of simplifying image visualization and manipulation when performing Image Processing tasks (or any kind of task involving image visualization) in Python. Using the **IPLabViewer** class in a Jupyter Notebook, a user with virtually no programming experience, and without experience with *matplotlib*, will be able to display an image and interactively change its characteristics (brightness, contrast, size, zoom), and even to extract information or perform operations on the image, without the need to recall the **IPLabViewer** or to plot again.  

The class is designed to run in Jupyter Notebooks or Jupyter Lab, using *matplotlib*'s dynamic environment (activate with the magic command `%matplotlib widget`). All the functunalities are controlled either through *matplotlib*'s native widgets (zoom and change of figure size) or through additional *ipywidgets'* buttons and sliders. See [requirements.txt]() file for more details on the necessary libraries and its versions.

## Main Features 
Once called, from the **IPLabViewer** and using both widgets and programmatic commands, a user will be able to:

* Plot several images at the same time, and choose different display options (one image at a time, or a customized grid of images),
* Change the brightness and contrast of the images through a slider,
* Explore the histogram of the image,
* Choose different colormaps and visualization options (colorbar, axis), 
* Get statistics -updated automatically when zooming to a region- of the image, 
* Declare functions that perform operations on an image, and through widgets, see the effect of the function with different parameters and applied on different functions. directly inside the **IPLabViewer** object.

Please refer to the [tutorial]() for examples on different use cases, or to our [wiki](https://github.com/Biomedical-Imaging-Group/IPLabImageViewer/wiki/Python-IPLabViewer()-Class) for a complete documentation.  

## Team 
The project was developed in the most part by:
* Alejandro Noguerón Aramburu (alejandro.nogueronaramburu@epfl.ch, [Alejandro-1996](https://github.com/Alejandro-1996))

under the guidance, help, testing and feedback of:
* Kay Lächler (kay.lachler@epfl.ch, [TheUser0571](https://github.com/TheUser0571))
* [Pol del Aguila Pla](https://poldap.github.io), (pol.delaguilapla@epfl.ch, [poldap](https://github.com/poldap))
* [Daniel Sage ](http://bigwww.epfl.ch/sage/index.html), (daniel.sage@epfl.ch, [dasv74](https://github.com/dasv74))

It was supported by EPFLs [Center for Digital Education (CEDE)](https://www.epfl.ch/education/educational-initiatives/cede/), and it belongs to de [Biomedical Imaging Group](http://bigwww.epfl.ch/).

## Installation and Usage
The easiest way to start using the class is to download the [lib]() directory, place it in the same directory as your notebook, and include the following lines in a cell of your notebook:
```python
%matplotlib widget

from lib.iplabs import IPLabViewer as viewer
```

If you want to keep the `iplabs.py` file in a separate location, you can import it with the following lines:
```python
%matplotlib widget

import sys  
sys.path.insert(0, PATH)
from iplabs import IPLabViewer as viewer
```
## Licence

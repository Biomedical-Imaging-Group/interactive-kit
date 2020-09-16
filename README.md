# IPLabViewer

Interactive image visualization tool for [Jupyter](https://jupyter.org/) Notebook based on [matplotlib](https://matplotlib.org/) and [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/). 

![](IPLabsJupyter_banner.gif)

## Purpose of the project
This project has the goal of simplifying image visualization and visual feedback in image-processing teaching and learning Jupyter Notebooks. Using the **IPLabViewer** class in a Jupyter Notebook, a user with virtually no programming experience, and without experience with *matplotlib*, will be able to display an image and interactively change its characteristics (brightness, contrast, size, zoom). The user will even be able to extract information or perform operations on the image, without the need to recall the **IPLabViewer** or to plot again.  

The class is designed to run in Jupyter Notebooks or Jupyter Lab, using *matplotlib*'s dynamic environment (activate with the magic command `%matplotlib widget`). All the functionalities are controlled either through *matplotlib*'s native widgets (zoom and change of figure size) or through additional *ipywidgets*' buttons and sliders. 

<!---
See the [requirements.txt]() file for more details on the necessary libraries and its versions.
-->

## Main features 
Once called, from the **IPLabViewer** and using both widgets and programmatic commands, a user will be able to:

* Plot several images at the same time, and choose different display options (one image at a time, or a customized grid of images),
* Change the brightness and contrast of the images through a slider,
* Explore the histogram of the image,
* Choose different colormaps and visualization options (colorbar, axis), 
* Get 1st and 2nd order statistics -updated automatically when zooming into a region- of the image, 
* Declare functions that perform operations on an image, and through custom widgets, see the effect of the function with different parameters applied on different images, directly inside the **IPLabViewer** object.

Please refer to the [tutorial](./source/IPLabViewer_Tutorial.ipynb) for examples on different use cases, or to our [wiki](https://github.com/Biomedical-Imaging-Group/IPLabImageViewer/wiki/Python-IPLabViewer()-Class) for a complete documentation.  

## Team 
The viewer was initially developed by:
* Alejandro Noguerón Aramburu (alejandro.nogueronaramburu@epfl.ch, [Alejandro-1996](https://github.com/Alejandro-1996))

under the guidance, help, testing and feedback of:
* Kay Lächler (kay.lachler@epfl.ch, [TheUser0571](https://github.com/TheUser0571))
* [Pol del Aguila Pla](https://poldap.github.io), (pol.delaguilapla@epfl.ch, [poldap](https://github.com/poldap))
* [Daniel Sage ](http://bigwww.epfl.ch/sage/index.html), (daniel.sage@epfl.ch, [dasv74](https://github.com/dasv74))

This project is supported by the EPFL's [Center for Digital Education (CEDE)](https://www.epfl.ch/education/educational-initiatives/cede/), and it belongs to the [Biomedical Imaging Group](http://bigwww.epfl.ch/).

## Installation and usage
The easiest way to start using the class is to download the [lib](./source/lib/) directory, place it in the same directory as your notebook, and include the following lines in a cell of your notebook:
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

### Members of the EPFL community

If you want to start using IPLabViewer rightaway, without going through the process of installing Python and Jupyter, you can [click here](https://noto.epfl.ch/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FBiomedical-Imaging-Group%2FIPLabImageViewer&urlpath=tree%2FIPLabImageViewer%2FIPLabViewer_Tutorial.ipynb&branch=master) and start using right away from [Noto](https://www.epfl.ch/education/educational-initiatives/cede/digitaltools/noto/), EPFL's Jupyter centralized platform.

## Contributions

We appreciate contributions, feedback and bug reports from the community:
* If you encounter any bug, please open an issue and describe. We will try to fix it or give you a workaround as soon as possible. 
* If you widh to contribute, fork the repository and then open a pull request. 

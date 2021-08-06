# InteractiveKit

A toolkit for interactive visualization of signal and image processing on [Jupyter](https://jupyter.org/) Notebooks.

![](IPLabsJupyter_banner.gif)

InteractiveKit was created to simplify visualization in image and signal processing teaching, learning and research. Using [Jupyter Notebooks](https://jupyter.org/) in combination with InteractiveKit, a user with virtually no programming experience, and without experience with *matplotlib*, will be able to display and manipulate one or several signals -in the form of *NumPy Arrays*- and interactively change their characteristics. It is even possible to extract information and perform operations directly on the signal, without the need to re-run the cell or to plot again.  

The class is designed to run in Jupyter Notebooks or Jupyter Lab, using *matplotlib*'s dynamic environment (requires [`ipympl`](https://github.com/matplotlib/ipympl), which can be activated with the magic command `%matplotlib widget`). All the functionalities are controlled either through *matplotlib*'s native widgets (zoom and change of figure size) or through additional *ipywidgets*' buttons and sliders. 

## Modules

#### **Image Viewer** (`imviewer`)

Optimized for image visualization and manipulation. See the dedicated [tutorial](https://github.com/Biomedical-Imaging-Group/interactive-kit/tree/master/tutorials/ImageViewer_Tutorial.ipynb) and [wiki](https://github.com/Biomedical-Imaging-Group/interactive-kit/wiki/Image-Viewer).

##### Main features 
Once called, from the `imviewer` and using both widgets and programmatic commands, a user will be able to:

* Plot several images at the same time, and choose different display options (one image at a time, or a customized grid of images),
* Change the brightness and contrast of the images through a slider,
* Explore the histogram of the image,
* Choose different colormaps and visualization options (colorbar, axis), 
* Get 1st and 2nd order statistics -updated automatically when zooming into a region- of the image,
* Calculate and visualize differences between two different images,
* Declare functions that perform operations on an image, and through custom widgets, see the effect of the function with different parameters applied on different images, directly inside the `imviewer` object. 


#### **Signal Viewer** (`sigviewer`) 
Optimized for 1-dimensional signal  visualization and manipulation. See the dedicated [tutorial](https://github.com/Biomedical-Imaging-Group/interactive-kit/tree/master/tutorials/SignalViewer_Tutorial.ipynb) and [wiki](https://github.com/Biomedical-Imaging-Group/interactive-kit/wiki/Signal-Viewer).

<!-- ### **Decision Boundary Viewer** (`boundviewer`) -->
## Installation and usage
First, make sure you have installed Python 3.6 or higher. Then, InteractiveKit can easily be installed through PyPI:

```
pip install interactive-kit==0.1rc3
```

To use in a jupyter notebook, you can import the modules in the following way:

```python
from image_viewer_kit import imviewer, sigviewer
```

## Team 
The viewer was initially developed by:
* Alejandro Noguerón Aramburu (alejandro.nogueronaramburu@epfl.ch, [Alejandro-1996](https://github.com/Alejandro-1996))

under the guidance, help, testing and feedback of:
* Kay Lächler (kay.lachler@epfl.ch, [TheUser0571](https://github.com/TheUser0571))
* [Pol del Aguila Pla](https://poldap.github.io), (pol.delaguilapla@epfl.ch, [poldap](https://github.com/poldap))
* [Daniel Sage ](http://bigwww.epfl.ch/sage/index.html), (daniel.sage@epfl.ch, [dasv74](https://github.com/dasv74))

This project is supported by the EPFL's [Center for Digital Education (CEDE)](https://www.epfl.ch/education/educational-initiatives/cede/), and it belongs to the [Biomedical Imaging Group](http://bigwww.epfl.ch/).



### Members of the EPFL community

If you want to start using InteractiveKit rightaway, without going through the process of installing Python and Jupyter, you can [click here](https://noto.epfl.ch/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FBiomedical-Imaging-Group%2FIPLabImageViewer&urlpath=tree%2FIPLabImageViewer%2FIPLabViewer_Tutorial.ipynb&branch=master) and start using right away from [Noto](https://www.epfl.ch/education/educational-initiatives/cede/digitaltools/noto/), EPFL's Jupyter centralized platform.

## Contributions

We appreciate contributions, feedback and bug reports from the community:
* If you encounter any bug, please open an issue and describe. We will try to fix it or give you a workaround as soon as possible. 
* If you wish to contribute, fork the repository and then open a pull request. 

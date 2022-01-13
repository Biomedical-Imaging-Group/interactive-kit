# `interactive-kit`

A toolkit for interactive visualization of signal and image processing on [Jupyter](https://jupyter.org/) Notebooks.

![](IPLabsJupyter_banner.gif)

`interactive-kit` was created to simplify visualization in image and signal processing teaching, learning and research. Using [Jupyter](https://jupyter.org/) Notebooks in combination with `interactive-kit` a user with virtually no programming experience, or without any experience with `matplotlib`, will be able to display and manipulate one or several signals or images and interactively explore them. It is even possible to extract information and perform operations directly on the signal or image without the need to re-run the cell or to plot again.  

The class is designed to run in Jupyter Notebooks or Jupyter Lab, using `matplotlib`'s dynamic widget-based environment ([`ipympl`](https://github.com/matplotlib/ipympl)), which needs to be activated with the magic command `%matplotlib widget`. All the functionalities are controlled either through `matplotlib`'s native widgets (zoom, pan, and change of figure size) or through additional `ipywidgets`-based buttons and sliders. 

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
First, make sure you have installed Python 3.6 or higher. Then, `interactive-kit` can easily be installed through PyPI:

```
pip install interactive-kit==0.1rc3
```

To use in a jupyter notebook, you can import the modules in the following way:

```python
from interactive_kit import imviewer, sigviewer
```

## Team 
The viewer was developed at the [EPFL's Biomedical Imaging Group](https://bigwww.epfl.ch/), mainly by

* Alejandro Noguerón Aramburu (alejandro.nogueronaramburu@epfl.ch, [Alejandro-1996](https://github.com/Alejandro-1996))

with contributions from 

* Kay Lächler (kay.lachler@epfl.ch, [TheUser0571](https://github.com/TheUser0571))
* [Pol del Aguila Pla](https://poldap.github.io), (pol.delaguilapla@epfl.ch, [poldap](https://github.com/poldap))
* [Daniel Sage ](http://bigwww.epfl.ch/sage/index.html), (daniel.sage@epfl.ch, [dasv74](https://github.com/dasv74))

The development of the viewer was supported by the [Digital Resources for Instruction and Learning (DRIL) Fund](https://www.epfl.ch/education/educational-initiatives/cede/digitaltools/dril/) at EPFL, which supported the projects _IPLAB – Image Processing Laboratories on Noto_ and _FeedbackNow – Automatic grading and formative feedback for image processing laboratories_ by Pol del Aguila Pla and Daniel Sage in the sprint and fall semesters of 2020, respectively. See the video below for more information. 

[![Image Processing Labs with Jupyter video on YouTube](http://img.youtube.com/vi/AF18wN37B6Q/0.jpg)](http://www.youtube.com/watch?v=AF18wN37B6Q "Image Processing Labs with Jupyter")

### Members of the EPFL community

If you want to start using `interactive-kit` rightaway, without going through the process of installing Python and Jupyter, you can [click here](https://noto.epfl.ch/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2FBiomedical-Imaging-Group%2FIPLabImageViewer&urlpath=tree%2FIPLabImageViewer%2FIPLabViewer_Tutorial.ipynb&branch=master) and start using right away from [Noto](https://www.epfl.ch/education/educational-initiatives/cede/digitaltools/noto/), EPFL's Jupyter centralized platform.

In addition, you could [go here](https://renkulab.io/projects/learn-renku/teaching-on-renku/interactive-kit) and click on the **Start** button to use it in an interactive session from [RenkuLab](https://renkulab.io/), an open source platfrom developed by the [Swiss Data Science Center](https://datascience.ch/) based at EPFL and ETHZ.

## Contributions

We appreciate contributions, feedback and bug reports from the community:
* If you encounter any bug, please open an issue and describe. We will try to fix it or give you a workaround as soon as possible. 
* If you wish to contribute, fork the repository and then open a pull request. 

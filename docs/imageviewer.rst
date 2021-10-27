ImageViewer
===========

Welcome to the documentation of *ImageViewer*! *ImageViewer* is a class for interactive visualization of images in Jupyter Notebooks. It is intended for users in education and research, as it has features covering image comparison, image analysis, and image manipulation. 

It allows you to quickly visualize an image and interact with its properties. You can easily change the brightness and contrast of your image, display its histogram, plot the image with different dynamic ranges and in different colormaps and quickly access the pixel-value statistics of any zoomed-in region. Moreover, *ImageViewer* is flexible enough to incorporate different transforms and filters in the form of lists of additional functions and callbacks, a functionality that allows to try different parameters/transforms without the need for rerunning a cell. Look at our `tutorial <https://github.com/Biomedical-Imaging-Group/interactive-kit/blob/master/tutorials/ImageViewer_Tutorial.ipynb>`_ for examples and use cases, or see below for a thorough explanation. of the input parameters.

Initialization
--------------

To initialize ImageViewer, you need to call it with the images that you want to plot inside a list as first parameter:

.. code-block:: python

    >> imviewer([image_1, image_2, image_3])
    
Note that all the images have to be `Numpy Arrays <https://numpy.org/doc/stable/reference/generated/numpy.array.html>`_. The rest of the parameters are all optional, and will help you customize the display of images:

.. autofunction:: interactive_kit.imageviewer.ImageViewer.__init__

Using Widgets
-------------

The widgets are organized in two main groups, where each group is displayed separately (excluding the simple view with only the `Show Widgets` button).
* Inital Menu
    * *Brightness & Contrast* Slider: Use the slider to adjust the minimum and maximum values of the images (in percentage of the maximum).
    * *Show/Hide Histogram* Button: On click, displays/hides the histogram of the image to the right of the image. If there are several images, it displays a histogram for each figure, arranged accordingly. 
    * *Options* Button: Switch to the *Options* menu
    * *Reset* Button: Sets all parameters their original state.
    * *Next* and `Prev` Buttons: Browse through the images (removed if **ImageViewer** was called with only one image, or if the parameter `subplots` was given).

* Options Menu
    * *Colormap* Dropdown Menu: choose one of the available colormaps.
    * *Show/Hide Axis* Button: Show or hide the axis of the images, with pixels as units.
    * *Show/Hide Colorbar* Button: Show or hide a colorbar next to each image.
    * *Back* Button: Returns to the Initial view.  

All the views include a text box with the statistics of the images, which is updated when applying any transformation to the image.

User Defined Widgets
--------------------

One of the goals of **ImageViewer** was for it to be as intuitive and simple as possible, but at the same time to offer as much functionality as possible to an interested user. The result is the possibility to add *User Defined Widgets*. These serve the purpose of applying a specific operation or transformation to your images, a transformation that might depend on one or more parameters. **ImageViewer** allows you to create a function in a Jupyter cell and apply it simultaneously to all images within your **ImageViewer** object with the help of a set of sliders. The function or transformation will take as parameters:

* an image (`NumPy array`), and 
* one or more parameters.

Your function will then  apply an operation on the image that depends on the parameters. Without advanced knowledge of Matplotlib, you would have to manually run the same process several times, and visualize the results each time. With **ImageViewer**, you can simply declare the widgets(s) that choose the parameters and an activation function as parameters to the viewer, and it will call your function and update the images for you. 

Additional to the core function that actually performs the operation, you need to declare:
 * widgets to set the parameters of your operation (sliders, dropdown menus, text inputs, see `ipywidgets documentation <https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html>`_ 
 * an callback that will take as input **only an image**, and will get the necessary parameters from the widgets. This activation function will subsequently call your transformation.
 * an `ipywidgets.Button` with a meaningful description, that will call your activation function

To activate this functionality, you will pass all the widgets (both the ones to set the parameters and the button to apply the transformation) through the parameter `new_widgets = [widget1, widget2, ..., button]`, and the callback through the parameter `callbacks = [callback]`. This will alter the widgets menus accordingly:
 
* The *Initial View* will have an additional button, *Extra Widgets*. This button will  let you access the *Extra Widgets Menus*,
* *Extra Widgets Menu*, contains:
    * Additional Widgets: The ones you declared through the parameter `new_widgets` arranged vertically,
    * Activation Button: The button (also declared through the parameter `new_widgets`) that will call your activation function (declared through callbacks)
    * `Back` Button: Returns to the *Initial View*.

Look at our `tutorial <https://github.com/Biomedical-Imaging-Group/interactive-kit/blob/master/tutorials/ImageViewer_Tutorial.ipynb>`_ for a detailed example.
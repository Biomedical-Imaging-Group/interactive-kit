import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import ipywidgets as widgets
# To stringify variables
import inspect
# To get user ID 
import getpass
# For timestamp
import time

# This block is to hide mpl buttons (un)comment to enable or disable buttons
from matplotlib import backend_bases
 ## MPL button behaviour for images
backend_bases.NavigationToolbar2.toolitems = (
    ('Home', 'Reset original view', 'home', 'home'),
#     ('Back', 'Back to  previous view', 'back', 'back'),
#     ('Forward', 'Forward to next view', 'forward', 'forward'),
    (None, None, None, None),
    ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
    ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
#     ('Subplots', 'Configure subplots', 'subplots', 'configure_subplots'),
    (None, None, None, None),
#     ('Save', 'Save the figure', 'filesave', 'save_figure'),
)


# Now we actually begin the class
class SignalViewer():
    
        ## Constructor, only mandatory argument is an image
    def __init__(self, signal_list, **kwargs):
        '''Initialization funcion of SignalViewer. 

        The only required argument is a signal (1D NumPy array) or a list of 
        signals. If the signals are not NumPy arrays, a ValueException will 
        be raised. All the rest of the parameters are optional         
        
        Parameters
        ----------
        signal : NumPy array or iterable of NumPy arrays
            The image or images to visualize
            
        bode : boolean 
            Whether to show the bode diagram from the beginning or not
            
        callbacks :  list
            The list should have either $1$ element or the same number of
            elements as there are signals. In the former case, the same
            callback will be applied to all signals. In the latter, the n-th
            callback of the list will be applied to the n-th signal. All
            callbacks should have as sole input and output parameters an 
            image. All other required parameters should taken from widgets
            values (see parameter `new_widgets`).  
            
        clip_range : iterable of two floats
            Indicates the min and max values that will be enforced on 
            all images. Images with values outside this range will be 
            clipped to the range, as in `numpy.clip`.
            
        compare : boolean
            Whether to activate the image comparison functionality. 
            Defaults to `False`. It only has an effect when `ImageViewer`
            is initialized with two images. Regions of the two images 
            where there are differences will be shown in red.

        grid : boolean
            Whether to plot with a grid or not
            
        joint_zoom : boolean
            Whether to activate or not the joint zoom functionality from 
            the initialization. When it is activated, zooming to an area 
            in an image will make the rest of the images zoom to the same
            area. It only has an effect when there is an image grid. It can
            be (de)activated also through the widgets menu.
            
        new_widgets : list of ipywidgets objects
            It is meant to be used jointly with the parameter `callbacks`.
            If a callback depends on tunable parameters, this should be set
            by ipywidgets sliders/dropdown menus, which need to be passed 
            to `ImageViewer` through this parameter. The last element in the 
            list should always be an `ipywidgets.Button`, that will serve to 
            apply any transform.
            
        normalize : boolean
            Whether to scale the values of all signals to the range $[0, 1]$.
            Defaults to False

        scale_range : iterable of 2 floats
            If given, all signals will be rescaled to the specified range.
            
        style : string {'stem', 'line', 'dot'}
            A string that determines the plotting style of the signal.
            Defaults to 'stem'.
            
        subplots :  iterable of 2 ints
            Specify a grid for the signals (see Matplitlib gridspec). If there
            are more signals than spaces in the grid, the rest of the signals 
            will not be shown.
        
        title : list of strings
            Specifies the title of every signal. If not given, the name of the 
            variable will be used as title.
        
        widgets : boolean
            Display the widget menu. If not specified (or set to False),
            only the button *Show Wisgets* will be displayed.
            
        '''

        # Get timestamp
        import time
        ts = time.gmtime()

        date_str = time.strftime("%x %X", ts)
        # 09/01/20 02:21:33
        # Also possible, iso Format
        # print(time.strftime("%c", ts))
        # Tue Sep  1 02:21:33 2020
        
        # Get user ID (SCIPER in Noto), and the number of the figure to be created
        uid = getpass.getuser().split('-')[2] if len(getpass.getuser().split('-')) > 2 else getpass.getuser()
        fig_num = int(len(plt.get_fignums()) / 2) + 1        
        
        # Make sure that the signal_list is a list of numpy arrays
        # If a numpy array is given, place it inside a list
        if type(signal_list) == np.ndarray:
            signal_list = [signal_list]
        # If a list is given, check that all objects inside are numpy arrays. Raise exception otherwise.
        elif type(signal_list) == list:       
            if not(all(isinstance(sig, np.ndarray) for sig in signal_list)):
                raise ValueException('Make sure that all your signals are numpy arrays. Use the method np.array(object).')
        # Raise exception otherwise. if object type not numpy array nor list.
        else:
            raise Exception('Please give the first argument as a list of numpy arrays.')
                
        # Once a list of numpy arrays is ensured, make the list an attribute of the viewer object.        
        self.signal_list = signal_list
        
        # Get the number of signals 
        self.number_signals = len(signal_list)         
        
        # Default behaviour is to show only one signal at a time, in different plots 
        subplots = [1 ,1]
        self.all_in_one_subplot = False
        
        # Attribute to keep track of signalage in display 
        self.current_signal = 0
        # Attribute to keep track on wether we have a comparison
        self.compare = False
        
        # Check if user requested a specific axis grid (subplopts = [m, n]). If so, modify the variable subplots
        if 'subplots' in kwargs:
            subplots = kwargs.get('subplots')   
            if subplots == 1 or subplots in ['same', 'all']:
                # If user requested, all signals will be shown in the same AxesSubplot
                self.all_in_one_subplot = True
                subplots = [1, 1]
                
            # Attribute that will be use to check if single_signal was required, and If so, which signal is currently on display
            self.current_signal = None
            
        # Create output widget to wrap figure and handle display of signals
        self.out_fig = widgets.Output(layout = widgets.Layout(width = '80%')) #(%80 for V layouot)
        with self.out_fig:            
            # Initialize figure and subplots inside just created widget
            self.fig, self.axs = plt.subplots(subplots[0], subplots[1], num = f'Signal {fig_num} - SCIPER: {uid} - Date: ' + date_str)   
        # Set an appropriate size (in inches) for the figure. These are similar to matplotlib default sizes. Modify them to change signal physical size. You can also set them constant, in which case, more signals --> smaller signals.
        if self.current_signal != None:
            self.fig.set_size_inches([subplots[1]*4.7*1.3, subplots[0]*4.5*1.3])
        else:
            self.fig.set_size_inches([subplots[1]*4.7*0.84, subplots[0]*4.5*0.75]) 
        # (subplots[1]*6.4*0.7, subplots[0]*5.5*0.7 for V layout, (0.84, 0.75) for IP1)               
        # Make sure that the axs is iterable in one foor loop (1D numpy array)
        self.axs = np.array(self.axs).reshape(-1)

        
        # This code block will get further information on the signals, and store it as atttriutes of the object. 
        # First, we create lists to store the info of each signals. 
        self.original = []         # Store the originals 
        self.data = []             # Store current data (only perform operations here)
        self.min = []              # Min value
        self.max = []              # Max value
        self.length = []           # Length of signals
        # Iterate through each image and prepare for plotting, according to user specifications        
        count = 0        
        for signal in signal_list:
                
            # Check if any transformation is required by the user and perform. Assign min-max values accordingly   
            if kwargs.get('normalize', False):
                #Stretch contrast to range [0, 1]
                signal = (signal - np.amin(signal)) / (np.amax(signal) - np.amin(signal))
                self.min.append(np.amin(signal))
                self.max.append(np.amax(signal))
            elif 'clip_range' in kwargs:
                # Clip signal to range specified by user 
                clip_range = kwargs.get('clip_range')
                signal = np.clip(signal, clip_range[0], clip_range[1])
                self.min.append(np.amin(clip_range[0]))
                self.max.append(np.amax(clip_range[1]))
            elif 'scale_range' in kwargs:
                # Scale signal to range specified by user
                scale_range = kwargs.get('scale_range')
                signal = (signal - np.amin(signal)) / (np.amax(signal) - np.amin(signal))
                signal = signal * (scale_range[1] - scale_range[0]) + scale_range[0]
                self.min.append(np.amin(signal))
                self.max.append(np.amax(signal))
            else:
                self.min.append(np.amin(signal))
                self.max.append(np.amax(signal))
            
            ### Now that we have the signal as the user specified it, store in attributes        
            self.original.append(np.copy(signal))
            self.data.append(np.copy(signal))
            
            # This will be useful in case pixel_grid was requested
            try:
                length = np.squeeze(signal).shape
                self.length.append(1)
            except:
                raise Exception(f'Signal {count} is not one dimensional.')
            count += 1

        # Now we are going to prepare the Axes. Again, initialize arrays        
        self.im = []       # list of Stem/Line objects (note that the object type is different)        
        self.titles = []   # List of titles        
        self.xlim = []     # List to store the x plotting range of each figure        
        # Check if titles were given, if not, stringified variable name (see self.retrieve_name() at the end of the class)
        title_arg = kwargs.get('title', [])
        if type(title_arg) != list:
            title_arg = [title_arg]
        # Iterate through the number of images 
        for i in range(self.number_signals):
            # Check if title was given by user. If so, append to our list of titles.
            if i < len(title_arg): 
                self.titles.append(title_arg[i])
            # If not, stringify variable name and append to title list
            else:
                self.titles.append(self.retrieve_name(self.signal_list[i]))
        
        # In the next for loop we will iterate through the number of signals, and actually plot them (according to the use case) 
        count = 0
        for i in range(self.number_signals):
            # axes_subplot is to choose whether to plot everything on the same AxesSubplot object
            if self.all_in_one_subplot: axs_idx = 0
            if not self.all_in_one_subplot:
                axs_idx = i
                # check that we have images left to plot in our axis array (useful in case subplots option was used, and there are more spaces than images). 
                # Enter if condition if we are in the last image (in case there are more axis than images) or last axis (in case single_image)
                if i == len(self.axs) or i == self.number_signals -1:
                    # If we're out of axis (will happen if user requested single_image or subplots = [m, n], and m*n < number_iamges), break loop
                    if len(self.axs) < len(self.data):
                        break
                    else:
                        # If this is the last image (will happen if user requested subplots = [m, n], and m*n > number_iamges)...
                        for j in range(i + 1, len(self.axs)):
                            # Turn off any remaining axis and exit for loop
                            self.axs[j].axis('off')
                
            
            # Create AxesImage and plot with user-requested parameters
            plotting_style = kwargs.get('style','stem')
            line_color = kwargs.get('color', 'blue')
            if plotting_style == 'stem':
                # Plot with STEM (kwarg use_line_collection is to avoid a warning)
                self.im.append(self.axs[axs_idx].stem(self.data[count], use_line_collection = True))
            elif plotting_style == 'line':
                self.im.append(self.axs[axs_idx].plot(self.data[count]))            
            elif plotting_style == 'dot':
                self.im.append(self.axs[axs_idx].plot(self.data[count], ':'))

            if not self.all_in_one_subplot:
                # Set the user rquested title
                self.axs[i].set_title(self.titles[count])
            else: self.axs[0].set_title('signals')
            # Save the limits of the plot in each axis (this are the default by matplotlib)
            self.xlim.append(np.round(self.axs[axs_idx].get_xlim(),1))

            # Hide the axis by default 
#             self.axs[i].axes.yaxis.set_visible(False)
#             self.axs[i].axes.xaxis.set_visible(False)
            # Place the axis in the top of the image 
            count += 1   
            
        ###############################################################################
        ### Declare widgets and link to callbacks (Names are self selfexplanatory) ####
        ###############################################################################
        
        # Go to Options menu Button
        self.button_options = widgets.Button(description = 'Options')
#         self.button_options.on_click(self.options_button)
        # Go to Main menu Button (Back)
        self.button_back = widgets.Button(description = 'Back')
#         self.button_back.on_click(self.back_button_callback)
        # Reset view and widgets original value
        self.button_reset = widgets.Button(description = 'Reset')
#         self.button_reset.on_click(self.reset)

        ##################### Text
        # Get stats. Instead of connecting to a callback, it is updated continuously
#         mean, std, min_value, max_value, num_channels, shape, xlim, ylim, descriptive_string = self.get_statistics()
#         _, _, _, _, _, _, _, descriptive_string = self.get_statistics()
        self.stats_text = widgets.Textarea(value = '', continuous_update = True,
                                           layout = widgets.Layout(width = '170px', height = '220px'), disabled = True) 
        
        if self.current_signal != None :
            
            # Button next image ('\U02190' for right arrow, not supported by python apparently)        
            self.button_next = widgets.Button(description = 'Next', layout = widgets.Layout(width = '80px'))
            self.button_next.on_click(self.next_button_callback)
            # Button prev image ('\U02192' for left arrow)
            self.button_prev = widgets.Button(description = 'Prev', layout = widgets.Layout(width = '80px'))
            self.button_prev.on_click(self.prev_button_callback)
            # Wrap both buttons in one Horizontal widget
            self.next_prev_buttons = widgets.HBox([self.button_prev, self.button_next])
        
        self.style = kwargs.get('style', 'stem')
        if self.style not in ['stem', 'line', 'dot']: style == 'stem'
        self.dropdown_style = widgets.Dropdown(options = ['stem', 'line', 'dot'], 
                                              value = self.style, 
                                              disabled = False, 
                                              layout = widgets.Layout(width = '65%'))
        self.dropdown_style.observe(self.style_callback, 'value')
        
        ####################### Wrap widgets in boxes ##################333
        widget_list = [self.button_options, self.button_reset, self.dropdown_style, self.stats_text]
        
        # If more than one image, add next and previous buttons
        if self.current_signal != None and self.number_signals > 1:
            widget_list.insert(5, self.next_prev_buttons)
        
        self.init_widg_view = widgets.VBox(widget_list)
        
        self.final_orig_view = widgets.HBox([self.out_fig, self.init_widg_view])
        display(self.final_orig_view)
        
    ##############################################################################################
    ################################# Widget Callbacks ###########################################
    ##############################################################################################
    
    def style_callback(self, change):
        '''Callback of cmap menu, to change the colormap to the selected one. 
        '''
        # Set the colormap of the images
        self.set_style(style = change.new)
        
    def prev_button_callback(self, change):
        '''Callback of *Prev* button, to browse to the previous image. 
        
        It is only active when there are several images, and the display mode
        is single image. When there is no previous image, it is disabled.
        '''
        # Change image to one before the currently plotted 
        self.change_signal(-1)
        
    def next_button_callback(self, change):
        '''Callback of *Next* button, to browse to the previous image. 
        
        It is only active when there are several images, and the display mode
        is single image. When there is no further image, it is disabled.
        '''
        # Change image to one after the currently plotted
        self.change_signal(1)
        
    ##############################################################################################
    ########### General Functions (used either by user, __init__ or widget callbacks) ############
    ##############################################################################################
        
    def set_style(self, style = 'stem'):
        # First we clear all the signals
        self.clear_axs()
        # And replot according to change
        count = 0
        for i in range(self.number_signals):
            # axes_subplot is to choose whether to plot everything on the same AxesSubplot object
            if self.all_in_one_subplot or self.current_signal != None: 
                axs_idx = 0
            elif not(self.all_in_one_subplot) and self.current_signal == None :
                axs_idx = i
            if self.current_signal != None and i > 0: break
            if self.current_signal != None:
                count = self.current_signal

            if style == 'stem':
                # Plot with STEM (kwarg use_line_collection is to avoid a warning)
                self.im.append(self.axs[axs_idx].stem(self.data[count], use_line_collection = True))
            elif style == 'line':
                self.im.append(self.axs[axs_idx].plot(self.data[count]))            
            elif style == 'dot':
                self.im.append(self.axs[axs_idx].plot(self.data[count], ':'))
            count += 1
            
    def clear_axs(self):
        '''Auxiliary function to clear all axs
        '''
        for ax in self.axs:
            ax.clear()
            
    def link_axs(self):
        '''Function called when there is any change in the axis to store

        This function is called when a displayed signal changes, when there 
        is a zoom event, or any event to changes the axis. If the 
        functionality *Joint Zoom* is activated, it updates the axis of the 
        rest of the images also. Moreover, it updates the statistics, to 
        get the information from the image currently in display.
        '''

        def on_xlims_change(event_ax):
            # Iterate through all the images
            for i in range(self.number_signals):
                # In the case of single_image == True, stop at the first
                if len(self.axs) == 1:
                    # Update xlim attribute
                    self.xlim[i] = np.round(event_ax.get_xlim(),1)
                    break
                # Check if joint zoom is on
#                 if self.button_joint_zoom.description == 'Disable Joint Zoom':
#                     self.xlim[i] = np.round(event_ax.get_xlim(),1)
                # Else look for the Axes which had the changes
                elif event_ax == self.axs[i]:
                    # Once found, update xlimits
                    self.xlim[i] = np.round(event_ax.get_xlim(),1)
                
#             self.update_stats()
            
        def on_ylims_change(event_ax):
            for i in range(self.number_signals):
                if len(self.axs) == 1:
                    self.ylim[i] = np.round(event_ax.get_ylim(),1)
                    break
#                 if self.button_joint_zoom.description == 'Disable Joint Zoom':
#                     self.ylim[i] = np.round(event_ax.get_ylim(),1)
                elif event_ax == self.axs[i]:
                    self.ylim[i] = np.round(event_ax.get_ylim(),1)
#             self.update_stats()
            
        count = 0            
        # Connect all Axes to the same handler (The handler we just defined takes care of identifying the Axes that changed)
        for ax in self.axs:
            if self.number_signals == count:
                break
            ax.set_xlim(self.xlim[count])
#             ax.set_ylim(self.ylim[count])
            ax.callbacks.connect('xlim_changed', on_xlims_change)
            ax.callbacks.connect('ylim_changed', on_ylims_change)
            count += 1
            
    def change_signal(self, change = 0):
        '''Called by the buttons *Prev*/*Next* to browse through the images.
0123456789112345678921234567893123456789412345678951234567896123456789712345 67898123456789
        This image takes care of changing the images, and updating the 
        information associated with the image (statistics, histogram, 
        colorbar, axis). If the previously displayed image had the same 
        dimensions as the new one, and it was zoomed to a region, it keeps 
        the zoomed area. Otherwise, it also resets the zoom
        '''
        # Restore self.im (attribute that holds AxesImage objects)
        self.im = []
        # If image in display is to be changed (change = 1, -1, 2, ...), check that there is another image to go to. Otherwise, do nothing
        if self.current_signal + change in range(self.number_signals):
            # Update attribute self.current_image
            self.current_signal += change
            
            # Local variable
            current_signal = self.current_signal
            
            # Keep track of wether the new and the previous image have the same shape 
            if self.data[current_signal].shape == self.data[current_signal - change].shape:
                old_axis = self.xlim[0]
            
            self.set_style(style = self.dropdown_style.value)
            # Set correct title
            self.axs[0].set_title(self.titles[current_signal])

#             # Repeat process for histogram
#             self.axs_hist[0].clear()
#             self.axs_hist[0].bar(self.bins[curr_img][:-1], self.hist[curr_img], 
#                              width = (self.bins[curr_img][1] - self.bins[curr_img][0]) / 1.2) 
#                         # Uncomment if condition to show y-axis
# #                 if self.button_show_axis.description == 'Show Axis':
# #                 self.axs_hist[0].axes.yaxis.set_visible(False)
#             self.axs_hist[0].set_yticks([])
#             self.axs_hist[0].set_ylabel('Count')
#             self.axs_hist[0].set_xlabel('Bin')
#             self.axs_hist[0].set_title(self.titles[curr_img])  
#             if self.max[0] != self.min[0]:
#                 # Assigning this limit is to fully visualize the first bin, otherwise, half of the bin gets lost
#                 self.axs_hist[0].set_xlim(self.min[self.current_image] - 0.01  *(self.max[self.current_image] 
#                                             - self.min[self.current_image]), self.max[self.current_image])
#             else:
#                 # If there is only one value in the image, mpl adjusts automatically but throws warning that we want to hide
#                 self.axs_hist[0].set_xlim(self.min[self.current_image] - 0.05, self.min[self.current_image] + 0.05)
#             self.axs_hist[0].set_ylim(0, 1.1*np.amax(self.hist[curr_img]))

#             ### Block to set lines
#             xmin = self.slider_clim.value[0]*0.01
#             xmax = self.slider_clim.value[1]*0.01
# #             self.lines[0][0].set_xdata([xmin*self.max[self.current_image], xmax*self.max[self.current_image]])
#             data = [xmin*(self.max[curr_img]-self.min[curr_img])+self.min[curr_img], 
#                     xmax*(self.max[curr_img]-self.min[curr_img])+self.min[curr_img]]
#             self.lines.append(self.axs_hist[0].plot(data, self.axs_hist[0].get_ylim(), 'k', linewidth = '0.3', linestyle = 'dashed'))

            if self.data[current_signal].shape == self.data[current_signal - change].shape:
                self.axs[0].set_xlim(old_axis[0])
#                 self.axs[0].set_ylim(old_axis[1])
                
            # link new axis to callbacks (for zoom) and update stats to new image
            
            #########################3 NEXT STEP
            self.link_axs()
#             self.update_stats()
        
        # Manage disabling of buttons (Disable prev if it's the first fig, next if it's the last, else enable both)
        if current_signal == self.number_signals -1 :
            self.button_next.disabled = True
            self.button_prev.disabled = False
        elif current_signal == 0:
            self.button_prev.disabled = True
            self.button_next.disabled = False
        else:
            self.button_next.disabled = False
            self.button_prev.disabled = False

        
    def retrieve_name(self, var): 
        '''Auxiliary function to retrieve the name of a variable in str form
        '''
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]
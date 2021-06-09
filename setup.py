from distutils.core import setup
setup(
  name = 'interactive-viewer-TEST',         
  packages = ['interactive-viewer-TEST'],   
  version = '0.1',      
  license='CC0-1.0',        
  description = 'Interactive image visualization tool, optimized for image comparison, \
                 and for applying transforms withing the image',
  author = 'BioMedical Imaging Group?',
  author_email = '',      # Type in your E-Mail
  url = 'https://github.com/Biomedical-Imaging-Group/IPLabImageViewer',
  download_url = 'https://github.com/Biomedical-Imaging-Group/IPLabImageViewer/archive/v_01.tar.gz',
  keywords = ['Image', 'Visualization', 'Intaractivity'],  
  install_requires=[ 
          'numpy',
          'ipywidgets',
          'cv2',
          'matplotlib'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose forom "3 - Alpha", "4 - Beta" or "5 - Production/Stable" 
#     'Intended Audience :: Developers',      # Define that your audience are developers
#     'Topic :: Software Development :: Build Tools',
#     'License :: OSI Approved :: MIT License',   # Again, pick a license
#     'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
#     'Programming Language :: Python :: 3.4',
#     'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
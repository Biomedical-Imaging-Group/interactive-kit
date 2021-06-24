# from distutils.core import setup
# setup(
#   name = 'interactive-viewer-TEST',         
#   packages = ['interactive-viewer-TEST'],   
#   version = '0.2',      
#   license='CC0-1.0',        
#   description = 'Interactive image visualization tool, optimized for image comparison, \
#                  and for applying transforms withing the image',
#   author = 'BioMedical Imaging Group',
#   author_email = '',      # Type in your E-Mail
#   url = 'https://github.com/Biomedical-Imaging-Group/IPLabImageViewer',
#   download_url = 'https://github.com/Biomedical-Imaging-Group/IPLabImageViewer/archive/v_01.tar.gz',
#   keywords = ['Image', 'Visualization', 'Intaractivity'],  
#   install_requires=[ 
#           'numpy',
#           'ipywidgets',
#           'matplotlib'
#       ],
#   classifiers=[
#     'Development Status :: 5 - Production/Stable',      # Chose forom "3 - Alpha", "4 - Beta" or "5 - Production/Stable" 
#     'Programming Language :: Python :: 3.7',
#   ],
# )
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="image-viewer-kit-TEST",
    version="0.4",
    license='CC0-1.0',
    author="Alejandro Noguerón",
    author_email="alex.noguerona@gmail.com",
    description="Interactive image viewer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Biomedical-Imaging-Group/IPLabImageViewer',
#     project_urls={
#         "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
#     },
    classifiers=[
        "Operating System :: OS Independent",
        'Development Status :: 5 - Production/Stable',      # Chose forom "3 - Alpha", "4 - Beta" or "5 - Production/Stable" 
        'Programming Language :: Python :: 3.7',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
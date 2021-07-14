import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="interactive-kit",
    version="0.1rc3",
    author="Alejandro Noguerón",
    author_email="alex.noguerona@gmail.com",
    description="Interactive viewer for signal processing, image processing, and machine learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Biomedical-Imaging-Group/interactive-kit',
    classifiers=[
        "Operating System :: OS Independent",
        'Development Status :: 5 - Production/Stable',      # Chose forom "3 - Alpha", "4 - Beta" or "5 - Production/Stable" 
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
    install_requires=[ 
          'numpy', 
          'matplotlib', 
          'jupyter',
          'jupyterlab',
          'ipympl', 
          'ipywidgets',
      ],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
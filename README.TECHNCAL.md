# **UK Food Magazine Restaurant Analysis using MongoDB**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, scipy.

In addition to those modules, the IPython notebook needs the following to execute: holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image, pymongo, MongoDB.

Here are the requisite Terminal commands for the installation of these peripheral modules:

python3 -m pip install holoviews

python3 -m pip install hvplot

python3 -m pip install geoviews

python3 -m pip install geopy

python3 -m pip install aspose-words

python3 -m pip install dataframe-image

python3 -m pip install pymongo

https://www.mongodb.com/docs/v6.0/tutorial/install-mongodb-on-os-x/ \
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/

----

### **Usage:**

----

The IPython notebooks, mongodb_setup.ipynb and restaurant_analysis.ipynb, require the following Python scripts with them in the same folder:

logx_constants.py

logx.py

mongodbx.py

pandasx.py

restaurant_analysisx.py

timex.py

If the folders, logs and omages, are not present, an IPython notebook will create them.  The folder, resources, holds the input file for the IPython Notebook, mongodb_setup.ipynb; the folder, logs, contains log files from testing the IPython Notebooks; and the folder, images has the PNG image and html files of the IPython Notebooks' tables and plots.

To place the IPython notebook in log mode or image mode set the parameter for the appropriate subroutine in coding cell #2 to True. In log mode, it writes information to the log file in the folder, logs. If the program is in image mode, it writes all DataFrames, hvplot maps, and matplotlib plots to png files in the folder, images.

----

### **Resource Summary:**

----

#### Source code

mongodb_setup.ipynb, restaurant_analysis.ipynb, logx_constants.py, logx.py, mongodbx.py, pandasx.py, restaurant_analysisx.py, timex.py

#### Input files

establishments.json

#### Output files

n/a

#### SQL script

n/a

#### Software

Jupyter Notebook, Matplotlib, MongoDB, Numpy, Pandas, PyMongo, Python 3.11.4

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./mongodb_setup.ipynb](./mongodb_setup.ipynb)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./README.md](./README.md)

|&rarr; [./restaurant_analysis.ipynb](./restaurant_analysis.ipynb)

|&rarr; [./restaurant_analysisx.py](./restaurant_analysisx.py)

|&rarr; [./table-of-contents.md](./table-of-contents.md)

|&rarr; [./images/](./images/)

  &emsp; |&rarr; [./images/restaurant_analysisFigure211WorstHygieneEstablishments.html](./images/restaurant_analysisFigure211WorstHygieneEstablishments.html)

  &emsp; |&rarr; [./images/restaurant_analysisFigure212WorstHygieneEstablishmentsCloseUp.html](./images/restaurant_analysisFigure212WorstHygieneEstablishmentsCloseUp.html)
  
  &emsp; |&rarr; [./images/restaurant_analysisFigure221HighRatingValueLondon.html](./images/restaurant_analysisFigure221HighRatingValueLondon.html)
  
  &emsp; |&rarr; [./images/restaurant_analysisFigure222HighRatingValueLondonCloseUp.html](./images/restaurant_analysisFigure222HighRatingValueLondonCloseUp.html)
  
  &emsp; |&rarr; [./images/restaurant_analysisFigure231HighestRatingBestHygiene.html](./images/restaurant_analysisFigure231HighestRatingBestHygiene.html)

  &emsp; |&rarr; [./images/NoSQLAnalysisFigure232HighestRatingBestHygieneCloseUp.png](./images/NoSQLAnalysisFigure232HighestRatingBestHygieneCloseUp.png)

  &emsp; |&rarr; [./images/restaurant_analysisFigure232HighestRatingBestHygieneCloseUp.html](./images/restaurant_analysisFigure232HighestRatingBestHygieneCloseUp.html)

  &emsp; |&rarr; [./images/restaurant_analysisTable21WorstHygieneEstablishments.png](./images/restaurant_analysisTable21WorstHygieneEstablishments.png)

  &emsp; |&rarr; [./images/restaurant_analysisTable22HighRatingValueLondonEstablishments.png](./images/restaurant_analysisTable22HighRatingValueLondonEstablishments.png)

  &emsp; |&rarr; [./images/restaurant_analysisTable23HighestRatingBestHygieneEstablishments.png](./images/restaurant_analysisTable23HighestRatingBestHygieneEstablishments.png)

  &emsp; |&rarr; [./images/restaurant_analysisTable24LocalAuthoritieswithNumberofEstablishmentswithHighestHygieneScore.png](./images/restaurant_analysisTable24LocalAuthoritieswithNumberofEstablishmentswithHighestHygieneScore.png)

  &emsp; |&rarr; [./images/README.md](./images/README.md)

|&rarr; [./logs/](./logs/)

  &emsp; |&rarr; [./logs/20240427mongodb_setup_log.txt](./logs/20240427mongodb_setup_log.txt)

  &emsp; |&rarr; [./logs/20240427restaurant_analysis_log.txt](./logs/20240427restaurant_analysis_log.txt)

  &emsp; |&rarr; [./logs/README.md](./logs/README.md)

|&rarr; [./resources/](./resources/)

  &emsp; |&rarr; [./resources/establishments.json](./resources/establishments.json)

  &emsp; |&rarr; [./resources/README.md](./resources/README.md)

----

### **References:**

----

[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

[Matplotlib Documentation](https://matplotlib.org/stable/index.html)

[MongoDB Documentation](https://www.mongodb.com/docs/)

[Numpy documentation](https://numpy.org/doc/1.26/)

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

[PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/)

[Python Documentation](https://docs.python.org/3/contents.html)

----

### **Authors and Acknowledgment:**

----

### Copyright

Nicholas J. George © 2023. All Rights Reserved.

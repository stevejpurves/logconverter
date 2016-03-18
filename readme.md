# log converter

DT log unit converstion and a notebook to look at well logs. Easily customiable to do more.

## Pre requisites

 1. Install [Anaconda python](https://www.continuum.io/downloads) (or some other scientific python distro)
 1. Install LAS file IO [lasio](http://pythonhosted.org/lasio/). From the Anaconda Commdn Prompt type `pip install lasio`

## Usage

The repo has a converter script and an ipython notebook

### to run the script

las_conv.py will run from the command line `ipython las_conv.py` but you will need to customise the 
main section (at the bottom of las_conv.py to point to the folder with your las files and provide the right filenames. 
        
    if __name__ == "__main__":
        data_path = 'D:\\MyDataPath\\Logs\\'
        filenames = ['F-O1.las', 'F-O2.las', 'F-O3.las', 'F-O4.las']
        batch_convert(data_path, filenames)

### To use the notebook

type `ipython notebook` in this folder and open the notebook in the browser. Customise!
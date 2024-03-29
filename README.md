# baselineWavelet_python
Implementing baseline correction to spectrum by python using baselineWavelet package written in R

## 1. Installation of R and baselineWavelet
In windows, **Make sure R is not installed on C disk**.

For R library of baselineWavelet and its installation, please see: https://github.com/zmzhang/baselineWavelet
or use the file provided in this repository.
* Please use R in version 3.6.2
* Then install Rstudio to include the baselineWavelet library
## 2. Install rpy2 in python
* The version of python in my computer is 3.7.4

Downloading repository: https://pypi.org/project/rpy2/

or using : 

* pip install rpy2
## 3. Run script test.py in this repository
There are two important steps before running the code.

 import rpy2 to your environment

* from rpy2.robjects.packages import importr

 import R's package baselineWavelet

* bW= importr('baselineWavelet')

This script contains the example program provided in the R baselineWavelet library.

If it works, it will save three figures in png the same as provided in this repository
1. Spectrum             --  Signal_Bg.png
2. Ridge lines          --  RidgeList.png
3. wavelet coefficient  --  WaveletCoeffs.png
## 4. Use the function written in python to process your spectrum

The function is defined as Python__R_wavelet_Func.py

* def baselineWavelet(Spectrum_data):
* ...
* return array(wCoefs),array(backgr),array(corrected)

where Spectrum_data is a one_dimensional data representing spectrum.

And this function returns three numpy arrays
1. wavelet coeffecients
2. baseline
3. baseline-corrected spectrum

## Article information

DOI	https://doi.org/10.1039/D0JA00431F

## How to cite:

Copy the Bibtex file as below:

@Article{D0JA00431F,

author ="Zou, Long and Sun, Chen and Wu, Mengting and Zhang, Yuqing and Yue, Zengqi and Xu, Weijie and Shabbir, Sahar and Chen, Fengye and Liu, Bin and Liu, Wenhui and Yu, Jin",

title  ="Online simultaneous determination of H2O and KCl in potash with LIBS coupled to convolutional and back-propagation neural networks",

journal  ="J. Anal. At. Spectrom.",

year  ="2021",

volume  ="36",

issue  ="2",

pages  ="303-313",

publisher  ="The Royal Society of Chemistry",

doi  ="10.1039/D0JA00431F",

url  ="http://dx.doi.org/10.1039/D0JA00431F"
}


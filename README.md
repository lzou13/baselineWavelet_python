# baselineWavelet_python
Implementing baseline correction to spectrum by python using baselineWavelet package written in R

## 1. Installation of R and baselineWavelet
In windows, Make sure R is not installed on C disk.

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
url  ="http://dx.doi.org/10.1039/D0JA00431F",
abstract  ="We demonstrate in this work online in situ characterization of potash fertilizer{,} a powder material{,} at its final production stage in factory on the production conveyer belt for quality assessment{,} with a specifically developed laser-induced breakdown spectroscopy (LIBS) instrument and dedicated data treatment software based on machine learning. Besides the usual difficulties encountered in online LIBS analysis{,} the specific challenge resides in moisture variation in the product{,} which results in a complex sample of powder of particle size ∼100 μm mixed with water (H2O). The influence on the LIBS spectrum was clearly observed{,} while no detailed physical model is available to describe such an influence. In addition{,} the emission line intensity from hydrogen (Hα line) observed in the spectrum did not show a clear relationship to the H2O concentration. The approach of analysis by correlation of the whole spectrum to the concentration was used to first determine the H2O concentration{,} which was further used as an additional parameter to concatenate with a LIBS spectrum in the formation of a generalized spectrum. The last was used as the input vector to train a potassium chloride (KCl) concentration calibration model. More specifically{,} LIBS spectra were first transformed into 2-D images with continuous wavelet transform (CWT). A convolutional neural network (CNN) then allowed mapping of the spectrum-images to the H2O concentrations of the corresponding samples{,} while a back-propagation neural network (BPNN) mapped generalized spectra to the KCl concentrations of the samples. The tests with online LIBS spectra and the corresponding offline analysis data of 119 samples taken during the period of LIBS measurements demonstrate advanced analytical performances of the trained models for H2O and KCl. Comparison between the model-predicted concentrations and the data from the offline analysis shows determination biases which fulfil the requirements of the concerned national standards (bias ≦0.20% for H2O and ≦0.598% for KCl) for the quasi totality of the tested samples."}


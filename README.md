# baselineWavelet_python
Implementing baseline correction to spectrum by python using baselineWavelet written in R
## 1. Installation of R and baselineWavelet
In windows, Make sure R is not installed on C disk.
For R library of baselineWavelet and it installation, please see: https://github.com/zmzhang/baselineWavelet
or use the file provided in this repository.
* Please use R in version 3.6.2
## 2. Install rpy2 in python
Downloading repository: https://pypi.org/project/rpy2/
or using : pip install rpy2
## 3. Run script test.py in this repository
There are two important step before running the code.
* import rpy2 to your environment
from rpy2.robjects.packages import importr
* import R's package baselineWavelet
bW= importr('baselineWavelet')

This script contains the example program provided in the R baselineWavelet library.
If it works, it will save three figures in png the same as provided in this repository
1. Spectrum             --  Signal_Bg.png
2. Ridge lines          --  RidgeList.png
3. wavelet coefficient  --  WaveletCoeffs.png
## 4. Use the function written in python to process your spectrum
The script contains this function is 

The function is defined as Python__R_wavelet_Func.py

* def baselineWavelet(Spectrum_data):
* ...

where Spectrum_data is a one_dimensional data representing spectrum
And this function returns three numpy arrays
1. wavelet coeffecients
2. baseline
3. baseline-corrected spectrum



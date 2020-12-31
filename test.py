####################################################
####################################################
## Test R program running in python env.
## baseline wavelet correction
from rpy2.robjects.packages import importr

# import R's "base" package
bW= importr('baselineWavelet')

import rpy2.robjects as robjects
test='''
data(raman)
x=m[7,]
scales <-seq(1, 70, 1)
wCoefs <- cwt(x, scales=scales, wavelet='mexh')
png("WaveletCoeffs.png",width=1000,height=600)
image(1:nrow(wCoefs), scales, wCoefs, col=terrain.colors(256), axes=FALSE, xlab='index', ylab='CWT coefficient scale', main='CWT coefficients')
box()
dev.off()

localMax <- getLocalMaximumCWT(wCoefs)
ridgeList <- getRidge(localMax, gapTh=3, skip=2)
png("RidgeList.png",width=1000,height=600)
plotRidgeList(ridgeList)
dev.off()

majorPeakInfo = identifyMajorPeaks(x, ridgeList, wCoefs, SNR.Th=1,ridgeLength=5)
peakWidth=widthEstimationCWT(x,majorPeakInfo)                                                
backgr = baselineCorrectionCWT(x,peakWidth,lambda=1000,differences=1)
corrected=x-backgr
png("Signal_Bg.png",width=1000,height=600)
plot(xa,x,type='l',ylim=c(min(c(x,corrected)),max(c(x,corrected))),main="The background-correction result of Raman Spectra",xlab=expression("Wavenumber / cm"^-1),ylab="Raman Intensity/Arbitr. Units")
points(xa[majorPeakInfo$peakIndex],x[majorPeakInfo$peakIndex])
lines(xa,backgr,lty=5)
lines(xa,corrected)
dev.off()
'''

robjects.r(test)

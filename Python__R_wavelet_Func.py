from rpy2.robjects.packages import importr
# import R's "baselineWavelet" package
bW= importr('baselineWavelet')
def baselineWavelet(Spectrum_data):
    S=Spectrum_data
    # Transform the original data into R language format
    rFS=ro.FloatVector(S)
    # Creating a R array correspond to the data's dimension
    sS=ro.FloatVector(range(1,shape(S)[0]+1))
    ## Start the wavelet analysis from R's baselineWavelet package
    scales=ro.r.seq(1,127,1)
    cwtargs={'scales':scales,'wavelet':'mexh'}
    
    # Wavelet coeffecients calculated by cwt
    ####******************########
    wCoefs=ro.r.cwt(rFS,**cwtargs)
    ####******************########
    
    # Get the ridge of wavelet coeffecients and output it into png file.
    localMax=bW.getLocalMaximumCWT(wCoefs)
    ####******************########
    ridgeList=bW.getRidge(localMax, gapTh=3, skip=2)
    # Calculating the background contribution
    MPargs={'SNR.Th':1,'ridgeLength':10}
    # Peak infomation
    majorPeakInfo = bW.identifyMajorPeaks(rFS, ridgeList, wCoefs,scales,**MPargs)
    peakWidth=bW.widthEstimationCWT(rFS,majorPeakInfo)
    
    bCargs={'lambda':1000,'differences':1}
    ####******************########
    backgr = bW.baselineCorrectionCWT(rFS,peakWidth,**bCargs)
    corrected=ro.FloatVector(array(rFS)-array(backgr))
    ####******************########
    #wavelet coeffecients, baseline, baseline-corrected spectrum
    return array(wCoefs),array(backgr),array(corrected)
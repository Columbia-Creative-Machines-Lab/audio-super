## Author - Chandra S Narain Kappera
## Audio Preprocessing tools

from pylab import *
from scipy.io import wavfile
import random

def clip_audio(fname,ofname,threshold):
    '''
    fname = input audio file name
    threshold = maximum percentage of output
    ofname = output file name
    '''
    sampFreq,snd = wavfile.read(fname)
    thres = threshold*max(snd)
    dtype = snd.dtype
    def trim(x):
        if x > thres:
            print(x,thres)
            x = thres
        return x

    out = list(map(trim,snd))

    out = np.asarray(out,dtype=dtype)
    
    wavfile.write(ofname,sampFreq,out)

    #print(snd.dtype,snd.shape,sampFreq,max(snd))
    return

def random_down_sample(fname,ofname,target):

    import math
    sampFreq,snd = wavfile.read(fname)
    n2 = int(len(snd)*target/sampFreq)
    dtype = snd.dtype

    k = math.ceil(len(snd)/(len(snd)-n2))
    print(k)

    index = [i+1 for i in range(len(snd))]
    
    out_index = random.sample(index,n2)
    out_index.sort()

    out = [snd[i-1] for i in out_index]

    out = np.asarray(out,dtype=dtype)

    wavfile.write(ofname,target,out)
    print(n2,len(snd),len(out))
    print(out)
    #print(snd.dtype,snd.shape,sampFreq,max(snd))
    return


def downsample(fname,ofname,target):
    import math
    sampFreq,snd = wavfile.read(fname)
    n2 = int(len(snd)*target/sampFreq)
    dtype = snd.dtype

    k = math.ceil(len(snd)/(len(snd)-n2))
    print(k)

    def drop(i):
        if i%k==0:
           return False
        return True
    index = [i+1 for i in range(len(snd))]
    out_index = list(filter(lambda i: i%k != 0,index))

    out = [snd[i-1] for i in out_index]


    out = np.asarray(out,dtype=dtype)

    wavfile.write(ofname,target,out)
    print(n2,len(snd),len(out))
    print(out)
    #print(snd.dtype,snd.shape,sampFreq,max(snd))
    return


#clip_audio('./input/p293_001.wav','./output/clip.wav',0.05)
#downsample('./input/p293_001.wav','./output/down.wav',16000)
random_down_sample('./input/p293_001.wav','./output/down_random.wav',16000)




import numpy as np
import matplotlib.pyplot as plt
import wave
import struct
freq=1000
sampling_rate=48000.0
num_samples=48000
amp=16000
file="firstwav.wav"
sine_wave=[np.sin(2*np.pi*freq*x/sampling_rate)for x in range(num_samples)]

nframes=num_samples
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2

wav_file=wave.open(file, 'wb')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amp)))

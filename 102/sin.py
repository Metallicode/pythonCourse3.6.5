import math
import matplotlib.pyplot as plt
import wave
import struct

def save_wav(file_name, audio):
    wav_file=wave.open(file_name,"wb")
    nchannels = 1
    sampwidth = 2
    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, 44100, nframes, comptype, compname))

    for sample in audio:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()

def sinFunc(x):
      return math.sin(math.radians(x))

tone = []

for i in range(360):
      tone.append(sinFunc(i))
      #to use more then one overtone, uncomment next 3 lines & comment out $$$ line
      
      #tone.append(sinFunc(i) + sinFunc(i*2))
      
##mx = max(tone)
##tone = [x/mx for x in tone] * 500


plt.plot(tone)

plt.show()

#this is $$$ lise to comment out
tone = tone*500

save_wav("hello.wav", tone)



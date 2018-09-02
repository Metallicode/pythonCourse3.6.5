#import libs
import matplotlib.pyplot as plt
import math
import wave
import struct
import datetime
import random

class Osc:
      #class ctor, creates "tones" list and hashes a uniqe name to the obj
      def __init__(self):
            self.tones = []
            self.name = "Sound" + str(hash(datetime.datetime.now())) + ".wav"

      #calc sin value 
      def __sinFunc(x):
            return math.sin(math.radians(x))

      #halp to create a range of floates
      def frange(x, y, step):
            while x > y:
                  yield x
                  x -= step

      #append a tone to "tones" list
      def addTone(self, tone):
            self.tones.append(tone)

      #return the sum of all tones in "tones" list
      def getMergedTones(self):
            return self.__class__.sumTones(self.tones)

      #creates a 360 length list of floats (1.0 -> -1.0) modelling a sin function wave. octv is the n full sin wav in this list 
      @classmethod
      def sin(cls, octv):
            tone = []
            for i in range(0, 360):
                  tone.append(cls.__sinFunc(i*octv))
            return tone

      #creates a X length list of floats (1.0 -> -1.0) modelling a noise waveform.
      @staticmethod
      def noise(length):
            return [random.uniform(-1.0, 1.0) for x in range(length)]

      #creates a 360 length list of floats (1.0 -> -1.0) modelling a square wave.
      @classmethod
      def square(cls, octv):
            tone = []
            for i in range(0, 359):
                  if cls.__sinFunc(i*octv) > 0:
                        tone.append(1.0)
                  elif cls.__sinFunc(i*octv) == 0:
                        tone.append(0.0)
                  else:
                        tone.append(-1.0)
            tone.append(0.0)     
            return tone

      #halps to create the saw tone...
      def __sawFunc(x, octv):
            return -1.0 + ((2/((360-octv)/octv))*x)

      #creates a 360 length list of floats (1.0 -> -1.0) modelling a saw wave.
      @classmethod
      def saw(cls, octv):
            tone = []
            for i in range(0, int(360/octv)):
                  tone.append(cls.__sawFunc(i, octv))
            return tone*octv

      #set gain (0.0 - 1.0) to tone.
      @staticmethod
      def gainTone(tone, gain):
            return [x*gain for x in tone]

      #merge all tones to one tone (return list length is as the shortest tone), scale to -1.0, 1.0 range.
      @staticmethod
      def sumTones(*args):
            listOfLengths = []
            for i in range(len(args[0])):
                  listOfLengths.append(len(args[0][i]))

            min_tone = min(listOfLengths)
            
            new_tone = [0 for x in range(min_tone)]

            for tone in args[0]:
                  for i in range(min_tone):
                        new_tone[i] += tone[i]

            mx = max(new_tone)
            mn = min(new_tone) 
            new_tone = [((((x - mn) * (2)) / (mx - mn)) -1) for x in new_tone]         
            return new_tone

      #save your tone
      @staticmethod
      def save_wav(file_name, audio):
            wav_file=wave.open(file_name,"w")

            nchannels = 1
            sampwidth = 2

            nframes = len(audio)
            comptype = "NONE"
            compname = "not compressed"
            wav_file.setparams((nchannels, sampwidth, 44100, nframes, comptype, compname))

            for sample in audio:
                  wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

            wav_file.close()

      #show tone on a x, y plot
      @staticmethod
      def plotTone(tone):
            plt.plot(tone)
            plt.show()

      #set the length of a tone (~seconds)
      @staticmethod
      def setLength(tone, x):
            sample_size = 44100*x
            timer = sample_size/len(tone)
            return tone*int(timer)

      #set the Pitch of a tone in two uses: 1- phase (PWM-ish) , 2 - full tone pitch 
      @staticmethod
      def setPitch(tone, gain):
            if gain > 180:
                  gain = 180
            step = int((len(tone) / gain))
            new_tone = []
            for i in range(len(tone)):
                  if not i % step == 0:
                        new_tone.append(tone[i])

            return new_tone


            
#init Osc
osc = Osc()

#create tones
osc.addTone(Osc.gainTone(Osc.setPitch(Osc.saw(1),1),1.0))
osc.addTone(Osc.gainTone(Osc.setPitch(Osc.saw(2),10),0.9))
osc.addTone(Osc.gainTone(Osc.setPitch(Osc.sin(20),20),0.8))
osc.addTone(Osc.gainTone(Osc.setPitch(Osc.saw(4),30),0.7))

#marge tones
tone = osc.getMergedTones()

#plot tone
Osc.plotTone(tone)

#set pitch
tone = Osc.setPitch(tone,30)

##osc.addTone(Osc.noise(10000))
##tone = osc.getMergedTones()

#set lenght
tone = Osc.setLength(tone, 2)

#save tone
Osc.save_wav(osc.name, tone)





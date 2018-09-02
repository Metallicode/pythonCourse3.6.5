#import libs
##http://pydub.com/
##https://pypi.org/project/pynput/
from pydub import AudioSegment
from pydub.playback import play
from pynput.mouse import Controller, Listener
import pynput

#create AudioSegment obj
sound = AudioSegment.from_wav("test.wav")

#gain volume
sound = sound + 6

#scale values
#NewValue = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
def scaleToScreenSize(xMouse, yMouse, soundLn):
      fx = (xMouse * soundLn) / 1360
      fy = (yMouse  * soundLn) / 767
      
      return fx, fy


#event calls this func
def playTheSound(a,b,c,d):
      #event args (x,y,button,up/down)
      print(a,b,c,d)
      #scale mouse info
      fx, fy = scaleToScreenSize(a,b,len(sound))
      if d:
            #play section times 4
            play(sound[fx:fx+fy]*4)


#start listener
with Listener(on_click=playTheSound) as listener:
    listener.join()

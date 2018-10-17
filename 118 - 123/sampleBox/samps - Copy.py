from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from playsound import playsound
import time, threading

def runSound(soundName):
    playsound(soundName)

class rootWidget(GridLayout):
    def playSound(self, s):
        eg = threading.Thread(target=runSound,
                      args=(),
                      kwargs={"soundName": s+".wav"})
        eg.start()

class MyApp(App):
    def build(self):
        return rootWidget()
        
if __name__ == "__main__":
    MyApp().run()

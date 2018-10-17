from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from playsound import playsound
import time, threading

class rootWidget(GridLayout):
    def playSound(self, s):
        playsound(s+".wav")

class MyApp(App):
    def build(self):
        return rootWidget()
        
if __name__ == "__main__":
    MyApp().run()

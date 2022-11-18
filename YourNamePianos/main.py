from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from pynput.keyboard import Key
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from keyboard import *


# --- this changes the app's default background --- #
Window.clearcolor = (0.9, 0.9, 0.9, 1)
Window.size = (1200, 600)

sounds = ["piano/do.wav", "piano/do-octave.wav", "piano/do-stretched.wav",
          "piano/do-stretched-octave.wav", "piano/fa.wav", "piano/fa-stretched.wav", "piano/la.wav",
          "piano/la-stretched.wav", "piano/mi.wav", "piano/mi-stretched.wav", "piano/re.wav",
          "piano/re-stretched.wav", "piano/si.wav", "piano/si-stretched.wav", "piano/sol.wav",
          "piano/sol-stretched.wav", "piano/do.wav", "piano/do-octave.wav", "piano/do-stretched.wav",
          "piano/do-stretched-octave.wav", "piano/fa.wav", "piano/fa-stretched.wav", "piano/la.wav",
          "piano/la-stretched.wav", "piano/mi.wav", "piano/mi-stretched.wav", "piano/re.wav",
          "piano/re-stretched.wav", "piano/si.wav", "piano/si-stretched.wav", "piano/sol.wav",
          "piano/sol-stretched.wav" ]


class BoxLayoutGame(BoxLayout):
    button_enabled = BooleanProperty(True)
    text_input_str = StringProperty("Your Name")
    def on_text_validate(self, widget):
        self.text_input_str = widget.text
        if self.text_input_str == " ":
            self.button_enabled = True
            print(self.text_input_str)
        if self.text_input_str != " ":
            self.button_enabled = False
            print(self.text_input_str)
            sound = SoundLoader.load(sounds[0])
            sound.play()

class BoxLayoutGameButtons(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 16):
            b = Button(background_color=(1, 1, 1, 1))
            self.add_widget(b)
            b.bind(on_press=self.btn_pressed)
    def btn_pressed(self, arg):
            for i in range(0, 31):   
                sound = SoundLoader.load(sounds[i])
                sound.play()

class MainWidget(Widget):
    pass

class YourNamePianosApp(App):
    pass


YourNamePianosApp().run()
#coding: utf-8
#qpy:kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class Ex20(BoxLayout):
    def on_touch_down(self, touch):
        print("pos: {}\nspos: {}\n".format(touch.pos, touch.spos))


class Ex20App(App):
    def build(self):
        return Ex20()

if __name__ == '__main__':
    Ex20App().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class TrucoApp(BoxLayout):
    def ganhou(self,text):
        print(text)




class Aplication(App):
    def build(self):
        return TrucoApp()
    


if __name__ == '__main__':
    Aplication().run()




from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class TrucoApp(BoxLayout):
    def __init__(self):
        super().__init__()
        self.pontostruco = 1
        self.pontosenvido = 0
        self.pontosflor = 0

    def ganhou(self,time):
        if self.ids.tipo.text == 'Envido' or self.ids.tipo.text == 'Flor':
            if time == 'time1':
                self.ids.tentos1.text = str(int(self.ids.tentos1.text)+int(self.ids.pontos.text))
                if int(self.ids.tentos1.text) >= 15:
                    self.ids.bois1.text = str(int(self.ids.bois1.text) + 1)
            elif time == 'time2':
                self.ids.tentos2.text = str(int(self.ids.tentos2.text)+int(self.ids.pontos.text))
                if int(self.ids.tentos2.text) >= 15:
                    self.ids.bois2.text = str(int(self.ids.bois2.text) + 1)
            self.ids.tipo.text == 'Truco'
            self.ids.pontos.text = str(self.pontostruco)

        elif self.ids.tipo.text == 'Truco':
            if time.name == 'time1':
                self.ids.tentos1.text = str(int(self.ids.tentos1.text)+self.pontostruco)
                if int(self.ids.tentos1.text) >= 15:
                    self.ids.bois1.text = str(int(self.ids.bois1.text) + 1)
                    self.ids.tentos1.text = '0'
                    self.ids.tentos2.text = '0'
            elif time.name == 'time2':
                self.ids.tentos2.text = str(int(self.ids.tentos2.text)+self.pontostruco)
                if int(self.ids.tentos2.text) >= 15:
                    self.ids.bois2.text = str(int(self.ids.bois2.text) + 1)
                    self.ids.tentos1.text = '0'
                    self.ids.tentos2.text = '0'

            self.ids.tipo.text = 'Truco'
            self.pontostruco = 1
            self.ids.pontos.text = str(self.pontostruco)


        self.ids.btruco.text = 'Truco'
        self.ids.benvido.text = 'Envido'
        self.ids.bflor.text = 'Flor'

        

    def Truco(self):
        if self.pontostruco == 1:
            self.pontostruco = 2
            self.ids.pontos.text = str(self.pontostruco)
            self.ids.btruco.text = 'Retruco'
            self.ids.tipo.text = 'Truco'
        elif self.pontostruco == 2:
            self.pontostruco = 3
            self.ids.pontos.text = str(self.pontostruco)
            self.ids.btruco.text = 'Vale 4'
            self.ids.tipo.text = 'Truco'
        elif self.pontostruco == 3:
            self.pontostruco = 4
            self.ids.pontos.text = str(self.pontostruco)
            self.ids.btruco.text = 'Vale o jogo'
            self.ids.tipo.text == 'Truco'
        elif self.pontostruco == 4:
            self.pontostruco = 15
            self.ids.pontos.text = 'X'
            self.ids.btruco.text = 'valendo o jogo'
            self.ids.tipo.text = 'Truco'

    def Envido(self):
        if self.ids.tipo.text != 'Flor':
            if self.pontosenvido == 0:
                self.pontosenvido = 1
                self.ids.pontos.text = str(self.pontosenvido)
                self.ids.benvido.text = 'Aceita?'
                self.ids.tipo.text == 'Envido'
            elif self.pontosenvido == 1:
                self.pontosenvido = 2
                self.ids.pontos.text = str(self.pontosenvido)
                self.ids.benvido.text = 'Real Envido'
                self.ids.tipo.text == 'Envido'
            elif self.pontosenvido == 2:
                self.pontosenvido = 5
                self.ids.pontos.text = str(self.pontosenvido)
                self.ids.benvido.text = 'Falta Envido'
                self.ids.tipo.text == 'Envido'
            elif self.pontosenvido == 5:
                self.pontosenvido = max(int(self.ids.tentos1.text),int(self.ids.tentos1.text))
                self.ids.pontos.text = str(self.pontosenvido)
                self.ids.benvido.text = 'Ta na Mesa'
                self.ids.tipo.text == 'Envido'

    def Flor(self):
        if self.pontosflor == 0:
            self.pontosenvido = 3
            self.ids.pontos.text = str(self.pontosenvido)
            self.ids.bflor.text = 'Tem para contra-flor?'
            self.ids.tipo.text == 'Flor'
        elif self.pontosflor == 3:
            self.pontosenvido = 6
            self.ids.pontos.text = str(self.pontosenvido)
            self.ids.bflor.text = 'E o resto?'
            self.ids.tipo.text == 'Flor'
        elif self.pontosflor == 6:
            self.pontosenvido = max(int(self.ids.tentos1.text),int(self.ids.tentos1.text))
            self.ids.pontos.text = str(self.pontosenvido)
            self.ids.btruco.text = 'quem vailevar o boi?'
            self.ids.tipo.text == 'Flor'
    
    def Menos(self,time):
        if time == 'time1':
            self.ids.tentos1.text = str(int(self.ids.tentos1.text)-1)
        if time == 'time2':
            self.ids.tentos2.text = str(int(self.ids.tentos2.text)-1)

class Application(App):
    def build(self):
        return TrucoApp()
    


if __name__ == '__main__':
    Application().run()




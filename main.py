from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class TrucoApp(BoxLayout):
    def __init__(self):
        super().__init__()
        self.pontostruco = 1
        self.pontosenvido = 0
        self.pontosflor = 0

    def ganhou(self,time):
        if self.ids.tipo.name == 'Envido' or self.ids.tipo.name == 'Flor':
            if time == 'time1':
                self.ids.tentos1.text = str(int(self.ids.tentos1.text)+int(self.ids.pontos.text))
                if int(self.ids.tentos1.text) >= 15:
                    self.ids.bois1.text = str(int(self.ids.bois1.text) + 1)
                    self.ids.tentos1.text = '0'
                    self.ids.tentos2.text = '0'
            elif time == 'time2':
                self.ids.tentos2.text = str(int(self.ids.tentos2.text)+int(self.ids.pontos.text))
                if int(self.ids.tentos2.text) >= 15:
                    self.ids.bois2.text = str(int(self.ids.bois2.text) + 1)
                    self.ids.tentos1.text = '0'
                    self.ids.tentos2.text = '0'
            self.pontosenvido = 0
            self.pontosflor = 0
            self.ids.tipo.text == 'Truco'
            self.ids.pontos.text = str(self.pontostruco)

        elif self.ids.tipo.name == 'Truco' or self.ids.tipo.name == '':
            if time == 'time1':
                self.ids.tentos1.text = str(int(self.ids.tentos1.text)+self.pontostruco)
                if int(self.ids.tentos1.text) >= 15:
                    self.ids.bois1.text = str(int(self.ids.bois1.text) + 1)
                    self.ids.tentos1.text = '0'
                    self.ids.tentos2.text = '0'
            elif time == 'time2':
                self.ids.tentos2.text = str(int(self.ids.tentos2.text)+self.pontostruco)
                if int(self.ids.tentos2.text) >= 15:
                    self.ids.bois2.text = str(int(self.ids.bois2.text) + 1)
                    self.ids.tentos1.text = '0'
                    self.ids.tentos2.text = '0'

            self.ids.tipo.text = '-----'
            self.pontostruco = 1
            self.pontosenvido = 0
            self.pontosflor = 0
            self.ids.pontos.text = str(self.pontostruco)

        self.ids.tipo.text = '-----'
        self.ids.btruco.text = 'Truco'
        self.ids.benvido.text = 'Envido'
        self.ids.bflor.text = 'Flor'

        

    def Truco(self):
        if self.pontostruco == 1:
            self.pontostruco = 2
            self.ids.pontos.text = str(self.pontostruco)
            self.ids.btruco.text = 'Retruco'
            self.ids.tipo.text = 'Truco'
            self.ids.tipo.name = 'Truco'
        elif self.pontostruco == 2:
            self.pontostruco = 3
            self.ids.pontos.text = str(self.pontostruco)
            self.ids.btruco.text = 'Vale 4'
            self.ids.tipo.text = 'Retruco'
            self.ids.tipo.name = 'Truco'
        elif self.pontostruco == 3:
            self.pontostruco = 4
            self.ids.pontos.text = str(self.pontostruco)
            self.ids.btruco.text = 'Vale o jogo'
            self.ids.tipo.text = 'valendo 4'
            self.ids.tipo.name = 'Truco'
        elif self.pontostruco == 4:
            self.pontostruco = 15
            self.ids.pontos.text = 'X'
            self.ids.btruco.text = 'valendo o jogo'
            self.ids.tipo.text = 'valendo o jogo'
            self.ids.tipo.name = 'Truco'

    def Envido(self):
        if self.ids.tipo.text != 'Flor':
            if self.pontosenvido == 0:
                self.pontosenvido = 1
                self.ids.pontos.text = str(self.pontosenvido)
                self.ids.benvido.text = 'Aceita?'
                self.ids.tipo.text = 'Envido'
                self.ids.tipo.name = 'Envido'
            elif self.pontosenvido == 1:
                self.pontosenvido = 2
                self.ids.pontos.text = str(self.pontosenvido)
                self.ids.benvido.text = 'Real Envido'
                self.ids.tipo.text = 'Envido'
                self.ids.tipo.name = 'Envido'
            elif self.pontosenvido == 2:
                self.pontosenvido = 5
                self.ids.pontos.text = str(self.pontosenvido)
                self.ids.benvido.text = 'pede a falta'
                self.ids.tipo.text = 'Real Envido'
                self.ids.tipo.name = 'Envido'

    def Flor(self):
        if self.pontosflor == 0:
            self.pontosflor= 3
            self.ids.pontos.text = str(self.pontosflor)
            self.ids.bflor.text = 'Tem para contra-flor?'
            self.ids.tipo.text = 'Flor'
            self.ids.tipo.name = 'Flor'
        elif self.pontosflor == 3:
            self.pontosenvido = 6
            self.ids.pontos.text = str(self.pontosenvido)
            self.ids.bflor.text = 'E o resto?'
            self.ids.tipo.text = 'contra-flor'
            self.ids.tipo.name = 'Flor'
        elif self.pontosflor == 6:
            self.pontosenvido = max(int(self.ids.tentos1.text),int(self.ids.tentos2.text))
            self.ids.pontos.text = str(self.pontosenvido)
            self.ids.btruco.text = 'quem vai levar o boi?'
            self.ids.tipo.text = 'contra flor e o resto'
            self.ids.tipo.name = 'Flor'
    
    def Menos(self,time):
        if time == 'time1' and int(self.ids.tentos1.text) > 0:
            self.ids.tentos1.text = str(int(self.ids.tentos1.text)-1)
        if time == 'time2' and int(self.ids.tentos2.text) > 0:
            self.ids.tentos2.text = str(int(self.ids.tentos2.text)-1)

    def FaltaEnvido(self):
        self.ids.pontos.text = str(15 - max(int(self.ids.tentos1.text),int(self.ids.tentos2.text)))
        self.ids.benvido.text = 'quem vai levar o boi'
        self.ids.tipo.text = 'Falta Envido'
        self.ids.tipo.name = 'Envido'

    def FaltaFlor(self):
        self.ids.pontos.text = str(15 - max(int(self.ids.tentos1.text),int(self.ids.tentos2.text)))
        self.ids.bflor.text = 'quem vai levar o boi'
        self.ids.tipo.text = 'Falta Flor'
        self.ids.tipo.name = 'Flor'

    def Clear(self):
        self.ids.pontos.text = '1'
        self.ids.tipo.text = '-----'
        self.ids.btruco.text = 'Truco'
        self.ids.benvido.text = 'Envido'
        self.ids.bflor.text = 'Flor'
        self.pontostruco = 1
        self.pontosenvido = 0
        self.pontosflor = 0


class Application(App):
    def build(self):
        return TrucoApp()
    


if __name__ == '__main__':
    Application().run()




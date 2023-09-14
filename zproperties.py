from kivy.uix.textinput import TextInput
from kivy.uix.label import Label




a = Label()
b = a.properties()
for x in b:
    print(f'{x} : {b[x]}')

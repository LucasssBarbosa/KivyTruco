<Time@TextInput>:
    padding_x: (self.width - self._get_text_width(self.text, self.tab_width, self._label_cached)) / 2
    padding_y: (self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0)
    multiline: False
    background_color: 1, 1, 1, .5
    foreground_color: 0, 0, 0, 1
    cursor_color: 1, 1, 1, 1

<Titulos@Label>:
    color: 1, 1, 1, 1
    canvas.before:
        Color:
            rgba: 1, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size

<Pontos@Label>:
    color: 1, 1, 1, 1
    canvas.after:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size

<Ganhou@Button>:
    text: 'Ganhou'
from manim import *

class Array(Scene):
    def __init__(self, values, **kwargs):
        super().__init__(**kwargs)
        self.values = values
        self.rects = []
        self.texts = []
        for i, value in enumerate(values):
            rect = Rectangle(width=1, height=1)
            rect.move_to(i*RIGHT)
            text = Text(str(value))
            text.move_to(i*RIGHT)
            self.add(rect, text)
            self.rects.append(rect)
            self.texts.append(text)

    def swap(self, i, j):
        self.play(
            self.rects[i].animate.move_to(j*RIGHT),
            self.rects[j].animate.move_to(i*RIGHT),
            self.texts[i].animate.move_to(j*RIGHT),
            self.texts[j].animate.move_to(i*RIGHT),
        )
        self.values[i], self.values[j] = self.values[j], self.values[i]
        self.rects[i], self.rects[j] = self.rects[j], self.rects[i]
        self.texts[i], self.texts[j] = self.texts[j], self.texts[i]

arr = Array([4, 2, 5, 1, 3])
arr.swap(0, 3)
arr.swap(1, 4)
arr.swap(2, 3)
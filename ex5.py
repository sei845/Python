class Stationary:

    def __init__(self, title="Что то рисуем"):
        self.title = title

    def draw(self):
        print(f'Начинаем рисовать! {self.title}')


class Pen(Stationary):

    def draw(self):
        print(f'Начинаем рисовать ручкой! {self.title}')


class Pencil(Stationary):

    def draw(self):
        print(f'Начинаем рисовать карандашом! {self.title}')


class Marker(Stationary):

    def draw(self):
        print(f'Начинаем рисовать маркером! {self.title}')


stat = Stationary()
stat.draw()

pen = Pen()
pencil = Pencil()
mark = Marker()

pen.draw()
pencil.draw()
mark.draw()
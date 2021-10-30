class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f"Введите текст ручкой {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Нарисуйте кружок  {self.title}")
class Handle(Stationery):
    def draw(self):
        print(f"Подчеркните текст {self.title}")

pen = Pen("ДОМ")
pencil = Pencil("карандашом")
handle = Handle("маркером")
for r in (pen, pencil, handle):
    r.draw()
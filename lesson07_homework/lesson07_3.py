class Cell:
    def __init__(self, cellule):
        self.cellule = cellule    #количество ячеек клетки

    def __add__(self, other):
        return Cell(self.cellule + other.cellule)

    def __sub__(self, other):
        diff = self.cellule - other.cellule
        if diff >= 0:
            return Cell(diff)
        else:
            print(f'Ошибка')

    def __mul__(self, other):
        return Cell(self.cellule * other.cellule)

    def __truediv__(self, other):
        return Cell(self.cellule // other.cellule)

    def make_order(self, nums):          #принимающий экземпляр класса и количество  ячеек в ряду
        s = ""
        for i in range(self.cellule // nums):
            s += "*" * nums + "\n"
        s += "*" * (self.cellule % nums) + "\n"
        return s

    def __str__(self):
        return f"{self.cellule}"

cell = Cell(18)
print(cell.make_order(7))
cell_2 = Cell(20)
print(cell_2.make_order(5))

print(cell - cell_2)
print(cell + cell_2)
print(cell * cell_2)
print(cell / cell_2)
print(cell_2 - cell)





    #** ** * \n ** ** * \n ** **
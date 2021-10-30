from random import randint

class Matrix:

    def __init__(self, param):
        self.param = param

    def __str__(self):
        s = ""
        for i in range(len(self.param)):
            for j in range(len(self.param[i])):
                s += f'{self.param[i][j]:02} '
            s += "\n"
        return s

    def __add__(self, other):
        param = [
           [self.param[i][j] + other.param[i][j] for j in range(len(self.param[i]))] for i in range(len(self.param))]
        return Matrix(param)

m_1 = Matrix([[randint(0, 100) for _ in range(10)] for _ in range(10)])
m_2 = Matrix([[randint(0, 100) for _ in range(10)] for _ in range(10)])
print(m_1)
print(m_2)
print(m_1 + m_2)


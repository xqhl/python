# 类的继承:

class Jx:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def getArea(self):
        return self.l * self.w

    def getCor(self):
        return (self.l + self.w) * 2


class Zfx(Jx):
    def __init__(self, l, w):
        super(Zfx, self).__init__(l, w)


zfx = Zfx(2, 2)
area = zfx.getArea()
print(area)

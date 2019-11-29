# class define: 三要素:class attribute functions

class Jx:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def getArea(self):
        return self.l * self.w

    def getCor(self):
        return (self.l + self.w) * 2


jx01 = Jx(10, 5)
area = jx01.getArea()
print("jx01's area: {}".format(area))
cor = jx01.getCor()
print("jx01's cor: {}".format(cor))

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self,1)

    def findArea(self):
        a= self.sides
        area = a[0] ** 2
        print('The area of the square is %0.2f' %area)
t = Square()
t.inputSides()
t.dispSides()
t.findArea()

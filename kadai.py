'''
課題1:円オブジェクト
次のコードが正しく動作するようなCircleクラスを実装すること
areaは面積、perimeterは周囲長という意味

#半径1の円
Circle1 = Circle(radius=1)
print(circle1.area()) #3.14
print(circle1.perimeter()) #6.28

#半径3の円
Circle3 = Circle(radius=3)
print(circle3.area()) #28.27
print(circle3.perimeter()) #18.85
'''


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 3.14 * (self.radius * 2)


circle1 = Circle(radius=1)
print(circle1.area())
print(circle1.perimeter())
circle3 = Circle(radius=3)
print(circle3.area())
print(circle3.perimeter())

'''
課題2:長方形オブジェクト
次のコードが正しく動作するようなRectangleクラスを実装すること
diagonalは対角線（の長さ）という意味

rectangle1 = Rectangle(height=5, width=6)
rectangle1.area() #30.00
rectangle1.diagonal() #7.81

rectangle2 = Rectangle(height=3, width=3)
rectangle2.area() #9.00
rectangle2.diagonal() #4.24

'''
class Rectangle:
    def __init__(self, height, width):
        self.height= height
        self.width = width

    def area(self):
        return self.height*self.width

    def diagonal(self):
        return  (self.height**2 + self.width**2)


assert circle1.area()==30.00

rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())
print(rectangle1.diagonal())
rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())
print(rectangle2.diagonal())

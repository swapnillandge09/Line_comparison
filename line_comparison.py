print("Welcome to Line Comparison Computation Program on Master Branch")
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)

    
    def __lt__(self, other):
        return self.length() < other.length()

    def __gt__(self, other):
        return self.length() > other.length()


if __name__ == "__main__":
    x1 = Point(1, 2)  
    x2 = Point(4, 6)  

    x3 = Point(0,1)
    x4 = Point(3,4)

    line1 = Line(x1, x2)
    line2 = Line(x3 , x4)

    if line1 == line2:
        print("the two lines are equal")
    else :
        print("The two lines are not equal")

    print(f"Length of the line: {line1.length()}")
    print(f"Length of the line: {line2.length()}")

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
    # uc1
    def length(self):
        return math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)
    

if __name__ == "__main__":
    x1 = Point(1, 2)  
    x2 = Point(4, 6)  
   
    line1 = Line(x1, x2)

    
    print(f"Length of the line: {line1.length()}")
import math
class Shape(object):
    def __init__(self, sides):
        self.sides = sides

    def shape_check(self):
        try:
            for val in self.sides:
                val = float(val)
                if val <= 0:
                    return False
                    break
        except TypeError:
            return False
        except ValueError:
            return False
        return True

    def print_error(self):
        if self.shape_check():
            pass
        else:
            print "Make sure all side lengths are numerical values that are greater than 0"
            return "Not applicable"


    def name(self):
        if self.shape_check():
            if len(self.sides) == 4:
                set1 = set(self.sides)
                if len(set1) == 4:
                    print "Polygon"
                if len(set1) == 2:
                    print "Rectangle"
                if len(set1) == 1:
                    print "Square"
            else:
		        dict1 = {3: "Triangle", 5: "Pentagon", 6: "Hexagon", 7: "Heptagon", 8: "Octagon"}
		        print dict1[len(self.sides)]
            if len(self.sides) < 3:
                print "This is not a valid shape"
            if len(self.sides) > 8:
                print "This shape is too large"
        else:
            self.print_error()
    def area(self):
        if self.shape_check():
            set2 = set(self.sides)
            if len(set2) == 1:
                apothem = self.sides[0]/(math.tan(math.radians(180/len(self.sides))) * 2)
                perimi = self.perimeter()
                area = (apothem * perimi)/2
                print area
                return area
        else:
            self.print_error()
            

    def perimeter(self):
        if self.shape_check():
            perim = 0
            for val in self.sides:
                perim += val
            print perim
            return perim
        else:
            self.print_error()


# the length of the side (s) divided by 2 times the tangent (tan) of 180 degrees divided by the number of sides (n).
    
shape1 = Shape([3,4,3,])    #rectangle
shape2 = Shape([4,4,4,4,4,4])    #square
shape3 = Shape([1,2,3,4,5])    #polygon

shape1.name()
shape2.name()
shape3.name()
shape4 = Shape([10,10,10,10,10,10])
shape4.area()

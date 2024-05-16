class findArea():
    def area(self,a=None,b=None):
        if a is  None and b is None:
            print("0")
        elif a is not None and b is None:
            print("area of square is",a*a)
        elif a is not None and b is not None:
            print("area of rectangle",a*b)
Ar=findArea()
Ar.area()
Ar.area(10)
Ar.area(10,5)

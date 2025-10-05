import math
def wall(height,weight):
    a=height*weight
    paint=a/7
    math.ceil(paint)
    print(f"Your wall need {math.ceil(paint)} can of paint ")


h=float(input("Your wall height: "))
w=float(input("Your wall weight: "))
wall(height=h,weight=w)
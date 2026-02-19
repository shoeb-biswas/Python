class area:
  def Rectangle(self,w,h):
    area= w * h
    print(f"Area: {area:.2f}")

  def Circle(self,r):
    area = 3.1416 *(r*r)
    print(f"Area: {area:.2f}")

shape = area()
shape.Rectangle(5,10)
shape.Circle(7)

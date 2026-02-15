class camera:
  def __init__(self,name):
    self.name = name

# method
  def capture(self):
    print("A photo is captured")

class Smart(camera):
  def __init__(self,name,resolution):
    super().__init__(name)
    self.resolution = resolution

# Method Overriding
  def capture(self):
    print("Photo is captured by Phone")


class DSLR(camera):
  def __init__(self,name,resolution):
    super().__init__(name)
    self.resolution = resolution

# Method Overriding
  def capture(self):
    print("Photo is captured by DSLR")

class Drone(camera):
  def __init__(self,name,resolution):
    super().__init__(name)
    self.resolution = resolution

# Method Overriding
  def capture(self):
    print("Photo is captured by Drone")

phone = Smart("Iphone","48MP")
dslr = DSLR("Nicon","4K")
drone = Drone("Amazon","1080p")

phone.capture()
dslr.capture()
drone.capture()

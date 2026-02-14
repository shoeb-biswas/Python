# Class
class Phone:
  category = "Electronics"

  # Constructor
  def __init__(self, battry, camera, model, battry_level=100):
    self.battry = battry
    self.camera = camera
    self.model = model
    self.battry_level = battry_level
# Method
  def charge(self,hour):
    print(f"Charge completed by {hour}")
  def capture(self,photo):
    if (self.battry_level)<=0:
      print("No Charge")
    else:
      self.battry_level-=photo
      print(f"Captured on {self.model}")

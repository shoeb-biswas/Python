class cooling_mechanism:
  def __init__(self,cooling_method):
    self.cooling_method = cooling_method
  def cooling_on(self):
    print(f"The system is being cool by {self.cooling_method}")

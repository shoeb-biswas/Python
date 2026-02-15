# Inharitance
class smartphone(Phone):
  def __init__(self, battry, camera, model, processor):
    super().__init__(battry, camera, model)
    self.processor = processor
  def charge(self,hour):
    print("Fast charging in process")
    super().charge(hour)

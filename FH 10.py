class Phone:
  def __init__(self,model, battery=100):
    self.model = model
    self.battery = battery

class SmartPhone(Phone):
  def __init__(self,model, battery,operatingsystem):
    super().__init__(model,battery)
    self.operatingsystem = operatingsystem

class GamingPhone(SmartPhone):
  def __init__(self,model, battery,operatingsystem,cooling_system):
    super().__init__(model, battery,operatingsystem)
    self.cooling_system = cooling_system

  def start_game(self,name):
    print(f"Playing {name} on {self.model}")

phone = GamingPhone("Iphone","85","ios","Vapping Pannel")
phone.start_game("Freefire")

class smartphone_cooling_mode(smartphone,cooling_mechanism):
  def __init__(self, battry, camera, model, processor, cooling_method):
    smartphone.__init__(self,battry, camera, model, processor)
    cooling_mechanism.__init__(self, cooling_method)

pro_cooling = smartphone_cooling_mode("300mAh","72MP","Safari","Apple Bionic","Lequid Nitrogen")

print(pro_cooling.battry) # from phone class
print(pro_cooling.processor) # from smartphone class
print(pro_cooling.cooling_method) # from cooling_mechanism class
print(pro_cooling.cooling_on()) # Method of cooling_mechanism
print(pro_cooling.charge(20)) # Smartphone's modified charge inharited from phone class

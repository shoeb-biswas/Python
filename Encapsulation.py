class mobile:
  def __init__(self,name,model,imei):
    self.__name = name
    self.__model = model
    self.__imei = imei #private

  def charge(self):
    print("Phone is charging")

  # To access IMEI
  def imei_gatter(self):
    return self.__imei

  def model_gatter(self):
    return self.__model

  def name_gatter(self):
    return self.__name

  def name_setter(self,name):
    self.__name = name


iphone = mobile("Phone",17,"1x343")

print(iphone.name_setter("Iphone"))
print(iphone.model_gatter())
print(iphone.imei_gatter())
print(iphone.name_gatter())

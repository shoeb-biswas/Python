from abc import ABC, abstractmethod
class telephone(ABC):
  @abstractmethod
  def make_call(self):
    pass

class Sphone(telephone):
  def make_call(self):
      print("making a call")

class Iphone(telephone):
  def make_call(self):
      print("making a call")

ip = Iphone()

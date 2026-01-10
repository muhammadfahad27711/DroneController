from abc import ABC, abstractmethod
#Latency Moniter
def timer(func):
  def wrapper(*args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    t = end - start
    print(f" LATENCY : accomplished in {t:.2f} sec")
    return result
  return wrapper
#Safety
class PercentLimit:
  def __init__(self, max):
    self.max = max
  def __set_name__(self, owner, name):
    self.name = name
  def __get__(self, obj, objtype):
    return obj.__dict__.get(self.name)
  def __set__(self, obj, percent):
    if percent > self.max:
      raise ValueError(f"OVER HEATING :SYSTEM is heated above {self.max}")
    obj.__dict__[self.name] = percent
#AI Programming
class AI(type(ABC)):
  def __new__(cls, name, bases, attrs):
    if "navigation" in attrs:
      attrs["navigation"] = timer(attrs["navigation"])
    new_class = super().__new__(cls, name, bases, attrs)
    print(f"Model :{name} validated")
    return new_class
#Controller
class DroneBrain(ABC, metaclass=AI):
  thrust = PercentLimit(100)

  @abstractmethod
  def navigation(self, sensor_data):
    pass
class Drone(DroneBrain):
  def navigation(self, sensor_data):

    print("SENSOR ON :Finding a safe path")
    self.thrust = 80
    time.sleep(1)
    return "Path found"
drone = Drone()  
print(drone.navigation("sensor_data"))

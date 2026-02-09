import numpy as np
celsius = [0, 10, 20, 30, 40]
celsius_array = np.array(celsius)
Farenheit = celsius_array * 1.8 + 32
print("Fahrenheit temperatures:", Farenheit)

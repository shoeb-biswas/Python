import numpy as np
lap_times = [75, 82, 78, 80, 77]
lap_times_array = np.array(lap_times)
print(lap_times_array.shape)
print(lap_times_array.size)
print(lap_times_array.dtype)

Minutes = lap_times_array/60

print(Minutes)

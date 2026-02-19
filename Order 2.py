import numpy as np

# একটি তালিকায় ৭ জনের বেতন ২৫-৩৫ হাজারের মধ্যে, কিন্তু ১ জনের বেতন ৫ লাখ
data = [25, 27, 28, 29, 30, 31, 35, 500] # 500 হল আউটলায়ার

print("গড় (Mean):", np.mean(data)) # Output: ~76.88
print("মধ্যমান (Median):", np.median(data)) # Output: 29.5

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

lst = [ 1 ,2 ,3 ,4 ,5 ,6 ]

def square(x):
    return x**2

lst = list(map(square ,lst))

print(lst)

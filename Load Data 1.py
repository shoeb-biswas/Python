import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("default")
sns.set(font_scale=1.1)

from google.colab import files

uploaded = files.upload()
df = pd.read_csv("heart.csv")
df.head(10)

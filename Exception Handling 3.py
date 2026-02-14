from logging import exception
# Train model

try:
  file = open("./sample_data/meri_marji.txt","r")
except Exception as e:
  print(e)
else:
  print(file.read())
finally:
  print("GPU is Stopped")

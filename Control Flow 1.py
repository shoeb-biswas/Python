# --- DEMO: Control flow ---
for i in range(10, 51):
    if i == 0:
        label = "zero"
    elif i % 2 == 0:
        label = "even"
    else:
        label = "odd"
    print(i, "→", label)

for i in range(5):
  for j in range(5):
    print(i)
    print(j)

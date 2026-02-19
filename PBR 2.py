nums = [10, 20, 30, 40, 50, 60]
print(nums[1:4])   # middle slice
print(nums[-3:])   # last 3
print(nums[::2])   # step slice
print(nums[::-1])  # reverse
print(nums[:-3])

# --- DEMO: Truthiness ---
samples = [0, 1, "", "text", [], [1], {}, {"k": 1}, None]
for item in samples:
    if item:
        print(repr(item), "→ Truthy")
    else:
        print(repr(item), "→ Falsy")

# --- DEMO: f-strings ---
name = "John"
score = 95
print(f"{name} scored {score}% (next: {score + 1}%)")

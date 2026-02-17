def to_int(s):
    try:
        return int(s)
    except ValueError as e:
        print("ValueError:", e)
        return None

print(to_int("ABC"))
# print("to_int('abc'):", to_int("abc"))

# --- DEMO: raising custom errors ---
def require_positive(n):
    if n <= 0:
        raise ValueError("n must be > 0")
    return n

def dividedbyn(n):
  if n==0:
    raise ZeroDivisionError("0 diye vag kora jabe nah")
  return 100/n;

try:
    # print(require_positive(-1))
    print(dividedbyn(0))
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print("Caught:", e)

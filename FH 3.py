N = int(input())
A= list(map(int, input().split()))
I = int(input("Enter a index number: "))

try:
  print(A[I])
except IndexError:
  print("Invalid index")
except ValueError:
  print("Please enter a valid integer index")

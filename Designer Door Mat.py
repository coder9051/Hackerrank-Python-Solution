a = input().split()
N = int(a[0])
M = int(a[1])
a = N//2
s = '.|.'
for i in range(1, a+1):
  print((s*(2*i - 1)).center(M, "-"))
print("WELCOME".center(M, "-"))
for i in range(a, 0, -1):
  print((s*(2*i - 1)).center(M, "-"))

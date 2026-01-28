n = int(input("Enter n: "))
x = int(input("Enter first number from you start: "))
if x < 1:
    print("Entered invalid number !!")
else:
    for i in range(x, n+1):
        print(i)
print("Sum of these natural numbers will be...")
s = 0
for i in range(1, n+1):
    s += i
print("Sum =", s)

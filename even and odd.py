print("1) Print Even numbers")
print("2) Print Odd numbers")

x = int(input("Enter choice: "))

if x == 1:
    n = int(input("Enter n: "))
    print("\nEven numbers:")
    for i in range(2, n + 1, 2):
        print(i)

elif x == 2:
    n = int(input("Enter n: "))
    print("\nOdd numbers:")
    for i in range(1, n + 1, 2):
        print(i)

else:
    print("Invalid choice")
    exit()

print("\nDo you want the sum?")
print("1) Yes")
print("2) No")

choice = int(input("Enter your decision: "))

if choice == 1:
    s = 0

    if x == 1:   # Even case
        for i in range(2, n + 1, 2):
            s += i
        print("Sum of even numbers =", s)

    elif x == 2:  # Odd case
        for i in range(1, n + 1, 2):
            s += i
        print("Sum of odd numbers =", s)

elif choice == 2:
    print("Thank you!")

else:
    print("Invalid decision")

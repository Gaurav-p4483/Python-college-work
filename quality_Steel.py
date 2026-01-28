hardness = float(input("Enter hardness (BHN): "))
carbon = float(input("Enter carbon content (%): "))
tensile = float(input("Enter tensile strength (kg/cm^2): "))

c1 = hardness > 50
c2 = carbon < 0.7
c3 = tensile > 5600

if c1 and c2 and c3:
    grade = 10
    statement = "Excellent quality steel"
elif c1 and c2:
    grade = 9
    statement = "Very good quality steel"
elif c2 and c3:
    grade = 8
    statement = "Good quality steel"
elif c1 and c3:
    grade = 7
    statement = "Above average quality steel"
elif c1 or c2 or c3:
    grade = 6
    statement = "Average quality steel"
else:
    grade = 5
    statement = "Poor quality steel"

print("\n--- Steel Quality Report ---")
print("1) Hardness:", hardness, "BHN")
print("2) Carbon Content:", carbon, "%")
print("3) Tensile Strength:", tensile, "kg/cm^2")
print("4) Grade:", grade)
print("5) Remark:", statement)

# Vendor Annual Purchase Report Program
name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = int(input("Enter Contact Number: "))
email = input("Enter Email ID: ")

# Monthly purchases
monthly = []
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

print("\nEnter monthly purchase amounts:")
for m in months:
    amt = float(input("Enter amount for " + m + ": "))
    monthly.append(amt)

# Calculate annual purchase
total = 0
for amt in monthly:
    total = total + amt

# Display report
print("\n-----------------------------")
print("ANNUAL PURCHASE REPORT")
print("-----------------------------")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("-----------------------------")

for i in range(12):
    print(months[i], ":", monthly[i])

print("-----------------------------")
print("Total Annual Purchase:", total)
print("-----------------------------")

# 1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.
print("\t\tfind a leap year using if else")
year = int(input("Enter a year: ",))

# Check if it's a leap year
if year % 4 == 0 :
    print(f"{year} is a leap year.", 'red')
else:
    print(f"{year} is not a leap year.")

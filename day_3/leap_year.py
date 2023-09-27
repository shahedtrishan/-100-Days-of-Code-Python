# 3.3
# leap_year

year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

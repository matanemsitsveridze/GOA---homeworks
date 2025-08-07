monday = input("Enter")
tuesday = input("Enter")
wednsday = input("Enter")
thursday = input("Enter")
friday = input("Enter")
saturday = input("Enter")
sunday = input("Enter")
week_days = [monday, tuesday, wednsday, thursday, friday, saturday, sunday]
res = []
for i in week_days:
    res += i[2]
print(res)

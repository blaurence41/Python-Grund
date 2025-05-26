def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True
        
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

def is_year_leap(year):
    if year % 4 != 0:
            return False
    elif year % 100 == 0 and year % 400 != 0:
            return False
    else:
            return True

def days_in_month(year, month):
    days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    answer = days_in_month[month - 1]
    if is_year_leap(year)==True and month == 2:
        answer += 1
    return int(answer)    
    

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
            

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    answer = days_in_month[month - 1]
    if is_year_leap(year)==True and month == 2:
        answer += 1
    return int(answer)   

def day_of_year(year, month, day):
    days_in_Year = 0
    while month > 0:
        days_in_Year += days_in_month(year, month)
        month -= 1
    days_in_Year -= days_in_month(year, month) - day
    return days_in_Year
    
    
print(day_of_year(2000, 12, 31))
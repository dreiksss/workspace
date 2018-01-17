
def is_leap(year):
	"""is_leap(year) -- return True if year is leap"""

	return year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0 )

def day_of_week(year, month, day):
	"""day_of_week(year, month, day) -- return day of week for some date (1 - monday, 7 - sunday)"""

	#Lets use Zeller's congruence
	if month == 1:
		month = 13
		year -= 1
	if month == 2:
		month = 14
		year -= 1
	k = year % 100
	j = year // 100
	h = (day + ((13*(month+1))//5) + k + (k//4) + (j//4) - 2*j) % 7
	return ((h+5)%7) + 1

def get_next_date(year, month, day):
	"""get_next_date(year, month, day) -- return date of next day"""

	if month == 2:
		if (is_leap(year) and day == 29) or day == 28:
			return year, month + 1, 1
	if month in {1, 3, 5, 7, 8, 10} and day == 31:
		return year, month + 1, 1
	if month in {4, 6, 9, 11} and day == 30:
		return year, month + 1, 1
	if month == 12 and day == 31:
		return year + 1, 1, 1
	return year, month, day + 1



def worked_days(year1, month1, day1, year2, month2, day2):
	"""worked_days(year1, month1, day1, year2, month2, day2) -- 
	return number of working days between date1 and date2

	"""

	res = 0
	while year1 != year2 or month1 != month2 or day1 != day2:
		if day_of_week(year1, month1, day1) in {1, 2, 3, 4, 5}:
			res += 1
		year1, month1, day1 = get_next_date(year1, month1, day1)
	return res


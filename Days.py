
def isLeap(year):
	"""isLeap(year) -- return True if year is leap"""
	return year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0 )

def dayOfWeek(year, month, day):
	"""dayOfWeek(year, month, day) -- return day of week for some date (1 - monday, 7 - sunday)"""
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

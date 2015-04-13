# import modules which will be used
from datetime import *
import calendar

"""
function create calendar page particular month and year; 
if one parameter is transfered, current year and particular month;
if parameters aren't transfered - current year and month
"""
def create_calendar_page(month = None, year = None):
	week_days = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']
	now = datetime.now()
	if year == None:
		year = now.year
	if month == None:
		month = now.month
	calen = calendar.monthrange(year, month)
	s = ''
	s += "-" * 20
	s += "\n"
	t = " " * calen[0]
	t += " " * (calen[0] * 2)

	for i in week_days:
		s += i + " "
	s = s[:-1]
	s += "\n"
	s += "-" * 20
	s += "\n"
	s += t
	count = len(t) + 1
	for i in range(1, calen[1] + 1):
		if len(t) == 21:
			s = s[:-1]
			s += "\n"
			t = ''
		if len(str(i)) == 1:
			s += "0"+str(i) + " "
		else:
			s += str(i) + " "
		t += '1' + '1' + '1' 
	s = s.replace("\s", '')
	return s[:-1]


print create_calendar_page(7, 1996)
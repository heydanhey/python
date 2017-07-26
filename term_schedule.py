import calendar

term_loan = 4
day = 15
month = 8
year = 2017
amort = []

for i in range(term_loan * 12):
    last_day = calendar.monthrange(year, month)[1]
    amort.append({'month':month, 'last_day':last_day, 'year':year})
    if month < 12:
        month += 1
    else:
        month = 1
        year += 1
        
print amort
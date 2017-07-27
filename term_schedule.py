import calendar
import datetime

term_loan_amort_start_date = datetime.datetime.now()
term_loan_term = 4

# Calculate MONTHLY Term Loan Schedule
if term_loan_amort_start_date.month == 12:
  month = 1
else:
  month = term_loan_amort_start_date.month + 1
year = term_loan_amort_start_date.year
term_schedule = []
for i in range(term_loan_term * 12):
  last_day = calendar.monthrange(year, month)[1]
  term_schedule.append("%s %d, %d" % (calendar.month_name[month], last_day, year))
  if month < 12:
    month += 1
  else:
    month = 1
    year += 1
        
print term_schedule

# Calculate QUARTERLY Term Loan Schedule
if term_loan_amort_start_date.month == 12:
  month = 1
else:
  month = term_loan_amort_start_date.month + 1
year = term_loan_amort_start_date.year
term_schedule = []
for i in range(term_loan_term * 4):
  last_day = calendar.monthrange(year, month)[1]
  term_schedule.append("%s %d, %d" % (calendar.month_name[month], last_day, year))
  month += 3
  if month > 12:
    month = month - 12
    year += 1
        
print term_schedule
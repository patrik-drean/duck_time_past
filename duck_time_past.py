from datetime import datetime, timedelta
from dateutil import parser

def past_time(old_date):
  # Convert from a string into a datetime field
  old_date = parser.parse(old_date)

  # Find the difference in time between now and the old date
  date_difference = datetime.now() - old_date

  # Split the time difference into the different measurements
  years, months, weeks, days, hours, minutes = (
    date_difference.days // 365,
    date_difference.days // 30,
    date_difference.days // 7,
    date_difference.days,
    date_difference.seconds // 3600,
    date_difference.seconds // 60 % 60
  )

  # Determine most accurate time measurement depending on how long ago
  if years > 0:
    time_elapsed = years
    time_measure = 'year'
  elif months > 0:
    time_elapsed = months
    time_measure = 'month'
  elif weeks > 0:
    time_elapsed = weeks
    time_measure = 'week'
  elif days > 0:
    time_elapsed = days
    time_measure = 'day'
  elif hours > 0:
    time_elapsed = hours
    time_measure = 'hour'
  elif minutes > 0:
    time_elapsed = minutes
    time_measure = 'minute'
  else:
    time_elapsed = ''
    time_measure = 'A few seconds'

  # Determine if time_measure needs to be pluralized
  if time_elapsed != '' and time_elapsed > 1:
   time_measure += 's'

  return '{} {} ago'.format(time_elapsed, time_measure)

 # Main program to run the function
 old_date = '2018-03-23T21:44:23.404'
 past_time(old_date) # Output: '2 weeks ago'
 

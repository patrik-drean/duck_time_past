from datetime import datetime, timedelta
from dateutil import parser

def past_time(old_date):
    # Convert into a datetime field, find the difference in time from now, and then split it up in time measurements
    old_date = parser.parse(old_date)
    date_difference = datetime.now() - old_date
    years, months, weeks, days, hours, minutes =  (date_difference.days // 365,
                                                    date_difference.days // 30,
                                                    date_difference.days // 7,
                                                    date_difference.days,
                                                    date_difference.seconds // 3600,
                                                    date_difference.seconds // 60 % 60)

    # Determine most accurate time measurement
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
        time_measure = 'Just now'

    # Determine if time_measure needs to be pluralized
    if time_elapsed != '' and time_elapsed > 1:
        time_measure += 's'

    # print('Time past is {} {}'.format(time_elapsed, time_measure))

    return '{} {} ago'.format(time_elapsed, time_measure)

# Main program
old_date = '2018-03-23T21:44:23.404'
past_time(old_date)

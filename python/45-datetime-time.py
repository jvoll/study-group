from time import localtime, strftime, mktime, strptime

'''
# time module is okay for this UTC and back in my timezone only!
now = 1407694710
local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)
print(time_str)

time_tuple = strptime(time_str, time_format)
utc_now = mktime(time_tuple)
print(utc_now)

# not good for this though PDT and EDT mix
parse_format = '%Y-%m-%d %H:%M:%S %Z'
depart_sfo = '2014-05-01 15:45:16 PDT'
time_tuple = strptime(depart_sfo, parse_format)
time_str = strftime(time_format, time_tuple)
print('depart sfo', time_str)

print('let\'s convert arrival time with timezones: EDT to my local time PDT')
arrival_nyc = '2014-05-01 23:33:24 EDT'
time_tuple = strptime(arrival_nyc, time_format)
'''

from datetime import datetime, timezone

now = datetime(2014, 8, 10, 18, 18, 30)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(now_local)

time_str = '2014-08-10 11:18:30'
time_format = '%Y-%m-%d %H:%M:%S'
now = datetime.strptime(time_str, time_format)
time_tuple = now.timetuple()
utc_now = mktime(time_tuple)
print(utc_now)


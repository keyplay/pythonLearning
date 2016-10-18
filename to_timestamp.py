#! python3.4
# -*- coding: utf-8 -*-
# to_timestamp.py - change the time to timestamp.

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    # match the datetime
    re_datetime = re.compile(r'''
        (\d{4})
        -
        (\d|1[0-2]|0[0-9])
        -
        (\d|0[0-9]|1[0-9]|2[0-9]|3[0-1])
        \s
        (0[0-9]|1[0-9]|2[0-3]|[0-9])
        \:
        (0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])
        \:
        (0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])
        ''', re.VERBOSE)
    
    result = re_datetime.match(dt_str).groups()
    result = list(map(int, result))
    dt = datetime(result[0], result[1], result[2], result[3], result[4], result[5])
    
    # match the timezone
    tz_groups = re.match(r'UTC([+|-]\d+)\:00', tz_str)
    h = int(tz_groups.group(1))
        
    tz_utc = timezone(timedelta(hours=h))
    dt = dt.replace(tzinfo=tz_utc)
    
    return dt.timestamp()


# test:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')

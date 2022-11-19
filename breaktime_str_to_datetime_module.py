from datetime import datetime, timedelta
from weekly_schedule_module import *

def breaktime_str_to_datetime(date_string, breaktime_string):

    d = datetime.strptime(date_string, "%d %b %y")
    t = datetime.strptime(breaktime_string, "%I:%M %p")
    
    delta = timedelta(hours=t.hour, minutes=t.minute)
    
    full = d + delta
    
    return full
    

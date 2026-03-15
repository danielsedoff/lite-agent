from datetime import datetime, timedelta

#print_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# date_str = "2345-01-01 00:00:01"

def get_time_diff(date_str): 
    try:
        date_now = datetime.now()
        date_then = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        difference_object = date_then - date_now
        difference_seconds = difference_object.total_seconds()
        if difference_seconds >= 0:
            return difference_seconds
        return None
    except:
        return None

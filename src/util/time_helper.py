from datetime import datetime, timedelta
"""! @brief This function returns current UTC datetime in ISO format."""
def get_iso_utc_time():
    return datetime.utcnow().isoformat()

def get_time_diff_timedelta(t1, t2):
    time_pattern = '%Y-%m-%dT%H:%M:%S.%f'
    return datetime.strptime(t1, time_pattern) - datetime.strptime(t2, time_pattern)

def get_time_obj_from_str(time):
    time_pattern = '%Y-%m-%dT%H:%M:%S.%f'
    return datetime.strptime(time, time_pattern)

def get_days_ago_time_str(days):
    now = datetime.utcnow()
    days_ago = now - timedelta(days=days)
    return days_ago.isoformat()


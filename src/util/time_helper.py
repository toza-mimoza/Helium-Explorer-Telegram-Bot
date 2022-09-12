from datetime import datetime
"""! @brief This function returns current UTC datetime in ISO format."""
def get_iso_utc_time():
    return datetime.utcnow().isoformat()

def get_time_diff_timedelta(t1, t2):
    time_pattern = '%Y-%m-%dT%H:%M:%S.%f'
    return datetime.strptime(t1, time_pattern) - datetime.strptime(t2, time_pattern)
    
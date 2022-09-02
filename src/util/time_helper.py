from datetime import datetime
"""! @brief This function returns current UTC datetime in ISO format."""
def get_iso_utc_time():
    return datetime.utcnow().isoformat()

from datetime import datetime

def format_timediff(start_time, end_time):
    try:
        diff = end_time - start_time
    except:
        diff = "undefined"

    return {
        "start": start_time,
        "start_readable": datetime.fromtimestamp(start_time).isoformat(),
        "end": end_time,
        "end_readable": datetime.fromtimestamp(end_time).isoformat(),
        "duration": diff
    }
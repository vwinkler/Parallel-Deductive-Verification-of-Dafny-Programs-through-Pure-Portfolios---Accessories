from datetime import datetime


def format_timediff(start_time, end_time):
    diff = try_format_readable_time_difference(end_time, start_time)

    return {
        "start": start_time,
        "start_readable": try_format_readable_time_point(start_time),
        "end": end_time,
        "end_readable": try_format_readable_time_point(end_time),
        "duration": diff
    }


def try_format_readable_time_difference(end_time, start_time):
    try:
        return end_time - start_time
    except Exception:
        return "undefined"


def try_format_readable_time_point(end_time):
    try:
        return datetime.fromtimestamp(end_time).isoformat()
    except Exception:
        return "undefined"

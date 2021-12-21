
def format_timediff(start_time, end_time):
    try:
        return end_time - start_time
    except:
        return "undefined"
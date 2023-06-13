def military_time_to_12(time: str) -> str:
    # time passed in should look like "2312" for "11:12pm"
    hour = time[:2]
    altered_time = f"""{int(hour) + 12}:{time[2:]}am"""
    if int(hour) > 12:
        altered_time = f"""{int(hour) - 12}:{time[2:]}pm"""
    return altered_time

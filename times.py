import datetime
from zoneinfo import ZoneInfo

def current_time():
    central_tz = ZoneInfo("US/Central")

    origins = datetime.datetime.now(central_tz)

    pretty_time = origins.strftime("%A %B %d %Y %I:%M:%S %p")

    return pretty_time

if __name__ == "__main__":
    print(current_time)


def time_convertor(num):
    minutes_in_an_hour = 60

    hours = num // minutes_in_an_hour
    minutes = num % minutes_in_an_hour

    hours_descriptor = "hour" if hours == 1 else "hours"
    minutes_descriptor = "minute" if minutes == 1 else "minutes"

    return f"{hours} {hours_descriptor}, {minutes} {minutes_descriptor}"

print(time_convertor(00))

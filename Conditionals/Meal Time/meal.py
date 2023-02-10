# a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. 
# If it’s not time for a meal, don’t output anything at all. 
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. 
# And assume that each meal’s time range is inclusive. 
# For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
# Structure your program per the below, wherein convert is a function (that can be called by main) 
# that converts time, a str in 24-hour format, to the corresponding number of hours as a float. 
# For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
# optionally add support for 12-hour times, allowing the user to input a.m. and p.m.



def main():
    the_time = convert(input("What time is it? "))
    if 7.00 <= the_time <= 8.00:
        print("breakfast time")
    if 12.00 <= the_time <= 13.00:
        print("lunch time")
    if 18.00 <= the_time <= 19.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    if minutes.endswith(" a.m."):
        am_minutes = float(minutes.strip(" a.m."))/60
        am_conversion =float(hours)+float(am_minutes)
        return float(am_conversion)
    elif minutes.endswith(" p.m."):
        pm_minutes = float(minutes.strip(" p.m."))/60
        if float(hours) == 12.00:
            return float(hours)+float(pm_minutes)
        else:
            pm_conversion = float(hours)+float(pm_minutes)+12.00
            return float(pm_conversion)
    else:
        float_minute_conversion = float(minutes)/60
        float_hours = float(hours)
        return float_minute_conversion+float_hours

main()
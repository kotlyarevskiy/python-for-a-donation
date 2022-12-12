# Practical lesson No. 2, task No. 1.
# This program displays a list of weekdays and a set of weekend days of the week.

DAYS_OF_THE_WEEK = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

WEEKDAY = [*range(1, 6)]
WEEKENDS = [*range(6, 8)]

print([DAYS_OF_THE_WEEK[x] for x in WEEKDAY])
print({DAYS_OF_THE_WEEK[x] for x in WEEKENDS})

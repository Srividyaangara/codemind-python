def calculate_angle(time):
    hour, minute = map(int, time.split(':'))
    hour_angle = (hour % 12) * 30 + (minute * 0.5)
    minute_angle = minute * 6

    angle = abs(hour_angle - minute_angle)

    return min(angle, 360 - angle)

time = input()
angle = calculate_angle(time)
print(angle)

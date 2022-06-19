hour, minute = map(int, input().split())

if hour == 0 and minute > 45:
    hour = 0
elif hour == 0 and minute == 45:
    hour == 24
elif hour == 0 and minute < 45:
    hour = 24

hour, minute = divmod(((hour * 60) + minute) - 45, 60)
print(hour, minute)

hour, minute = tuple(map(int, input().split()))

needed_minute = int(input())

total_minute = minute + needed_minute

if total_minute >= 60:
    hour += total_minute // 60
    total_minute = total_minute % 60

if hour >= 24:
    hour = hour % 24


print(f"{hour} {total_minute}")

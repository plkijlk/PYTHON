city_name = input("city")
temp = float(input("what is the temp of the" + city_name))
if temp > 35:
  print("too hot!")
elif temp > 25:
  print("great day to go out")
else:
  print("grab a jacket before you go out!")

if temp > 35:
  print("weather: scorching hot")
elif temp > 25:
  print("weather: warm and sunny ")
elif temp > 15:
  print("weather; cool and breezy") 
else:
  print("weather: cold - stay warm!")

import datetime
import calendar

now = datetime.datetime.now()
print("City;", now)
print("Time now:", now)

print(calendar.calendar(now.year))
weekday_ordinal = int(input("Enter week day ordinal: "))
message = "Today is "
if weekday_ordinal == 1: message += "Sunday"
elif weekday_ordinal == 2: message += "Monday"
elif weekday_ordinal == 3: message += "Tuesday"
elif weekday_ordinal == 4: message += "Wednesday"
elif weekday_ordinal == 5: message += "Thursday"
elif weekday_ordinal == 6: message += "Friday"
elif weekday_ordinal == 7: message += "Saturday"
else: message += "Cancelled"
print(message + ".");

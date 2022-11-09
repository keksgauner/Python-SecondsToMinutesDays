# 60 seconds = 1 minute
# 3600 seconds = 1 hour
# 86400 seconds = 1 day
# 604800 seconds = 1 week
# 2592000 seconds = 1 month
# 31536000 seconds = 1 year

# 619 seconds = 10 minutes and 19 seconds
# 521 seconds = 8 minutes and 41 seconds
# 23131 seconds = 6 hours and 25 minutes and 31 seconds
# 123456 seconds = 1 day and 10 hours and 17 minutes and 36 seconds
# 1234567 seconds = 14 days and 6 hours and 56 minutes and 7 seconds

# Input
seconds = 86400
print("Input: " + str(seconds) + " seconds")

# With divided by the number of years, days, hours, minutes and seconds was determined
# Mit Geteilt durch wurd die Anzahl der Jahre, Tage, Stunden, Minuten und Sekunden ermittelt
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
months = days / 30
years = months / 12

# With modulo % the rest number will contain the exact seconds, minutes, hours and days
# Mit Modulo % wird die Restzahl die genauen Sekunden, Minuten, Stunden und Tage enthalten
restSeconds = seconds % 60
restMinutes = minutes % 60
restHours = hours % 24
restDays = days % 30
restMonths = months % 12
restYears = years % 360

# delete all decimal places because everything after the decimal point is not needed
# Lösche alle Nachkommastellen weil alles was nach dem Komma kommt nicht benötigt wird
restSeconds = int(restSeconds)
restMinutes = int(restMinutes)
restHours = int(restHours)
restDays = int(restDays)
restMonths = int(restMonths)
restYears = int(restYears)


# Output
print(str(restSeconds) + " seconds")
print(str(restMinutes) + " minutes")
print(str(restHours) + " Hours")
print(str(restDays) + " Days")
print(str(restMonths) + " Months")
print(str(restYears) + " Years")

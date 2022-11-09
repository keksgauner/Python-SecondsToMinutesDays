# Examples

# 60 Sekunden = 1 Minute
# 3600 Sekunden = 1 Stunde
# 86400 Sekunden = 1 Tag
# 604800 Sekunden = 1 Woche
# 2592000 Sekunden = 1 Monat
# 31536000 Sekunden = 1 Jahr

# 619 Sekunden = 10 Minuten und 19 Sekunden
# 521 Sekunden = 8 Minuten und 41 Sekunden
# 23131 Sekunden = 6 Stunden und 25 Minuten und 31 Sekunden
# 123456 Sekunden = 1 Tag und 10 Stunden und 17 Minuten und 36 Sekunden
# 1234567 Sekunden = 14 Tage und 6 Stunden und 56 Minuten und 7 Sekunden

# Eingabe
sekunden = 86400
print("Input: " + str(sekunden) + " Sekunden")

# Mit Geteilt durch wurd die Anzahl der Jahre, Tage, Stunden, Minuten und Sekunden ermittelt
minuten = sekunden / 60
stunden = minuten / 60
tage = stunden / 24
monate = tage / 30
jahre = monate / 12

# Mit Modulo % wird die Restzahl die genauen Sekunden, Minuten, Stunden und Tage enthalten
restSekunden = sekunden % 60
restMinuten = minuten % 60
restStunden = stunden % 24
restTage = tage % 30
restMonate = monate % 12
restJahre = jahre % 360

# Lösche alle Nachkommastellen weil alles was nach dem Komma kommt nicht benötigt wird
restSekunden = int(restSekunden)
restMinuten = int(restMinuten)
restStunden = int(restStunden)
restTage = int(restTage)
restMonate = int(restMonate)
restJahre = int(restJahre)


# Ausgabe
print(str(restSekunden) + " Sekunden")
print(str(restMinuten) + " Minuten")
print(str(restStunden) + " Stunden")
print(str(restTage) + " Tage")
print(str(restMonate) + " Monate")
print(str(restJahre) + " Jahre")

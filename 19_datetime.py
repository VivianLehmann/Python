import datetime as dt

# modul datetime : menschliche kalenderlogik (tage,wochen,zeitzonen)
# zeitzonen - steuerung
# ideal für : datenbankeinträge, terminplanungen, fristen berechnen , benutzerinformationen

# wichtig : zeitpunkt, zeitinterval

# timedelta : representiert zeitspanne oder dauer(zeitinterval)

duration = dt.timedelta(
    weeks = 12,
    days = 50,
    hours = 4,
    minutes = 2,
    seconds = 27,
    milliseconds = 45,
    microseconds = 12
)
print(duration)
print(duration.days)
print(duration.seconds)
print(duration.microseconds)
print(duration.total_seconds())

duration1 = dt.timedelta(weeks=4)
duration2 =dt.timedelta(days=22)
duration3 = dt.timedelta(weeks=1,days=4)
print(duration1 + duration2 + duration3)
print(duration*5)

# date objects

datum = dt.date(year = 1997,month=3,day=12)
print(datum)
heute = dt.date.today()
print(heute)
time_difference = heute - datum
print(type(time_difference))
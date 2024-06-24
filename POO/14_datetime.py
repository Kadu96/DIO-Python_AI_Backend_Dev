from datetime import date, datetime, timedelta
import pytz

d = date(2024, 6, 24)
print(f"{d}\n")

e = date.today()
print(f"{e}\n")

f = datetime.now()   #(2024, 6, 24, 9, 16)
print(f"{f}")

g = f + timedelta(weeks=1)
print(f"{g}")

f = f.strftime("%d/%m/%Y %H:%M:%S")
print(f"{f}")

dt = "24/06/2024 09:30"
print(f"{dt}")
h = datetime.strptime(dt, "%d/%m/%Y %H:%M")
print(f"{h}")

data = datetime.now(pytz.timezone("Europe/Oslo"))
print(f"{data}")
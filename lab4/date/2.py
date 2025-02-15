#Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta
today = datetime.today()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("yesterday: ", yesterday.strftime("%a, %d.%m.%Y"))
print("today: ", today.strftime("%a, %d.%m.%Y"))
print("tomorrow: ", tomorrow.strftime("%a, %d.%m.%Y"))
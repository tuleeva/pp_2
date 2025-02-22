#Write a Python program to calculate two date difference in seconds.
from datetime import datetime
def difference(date1_str, date2_str, format="%Y-%m-%d %H:%M:%S"):
    date1=datetime.strptime(date1_str, format)
    date2=datetime.strptime(date2_str, format)

    res=date1-date2
    return abs(res.total_seconds())

date1 = "2025-02-16 12:15:00"
date2 = "2025-02-16 15:30:00"
 
result=difference(date1, date2)
print(f"difference in seconds: {result}")
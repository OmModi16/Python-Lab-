from datetime import datetime
date1 = (15, 5, 2020)  
date2 = (25, 12, 2021)  
date1 = datetime(date1[2], date1[1], date1[0])
date2 = datetime(date2[2], date2[1], date2[0])
days_difference = (date2 - date1).days
print(days_difference)

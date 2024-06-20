from datetime import datetime, date, timedelta
from sqlalchemy import DateTime
print(datetime.today())
d = date(2024, 6, 14)
print(d)
print(d - timedelta(days=15))

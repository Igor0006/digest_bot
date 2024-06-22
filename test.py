from datetime import datetime, date, timedelta
from sqlalchemy import DateTime
print(datetime.today())
d = datetime(2024, 6, 20)
print((d - timedelta(days=7))<= datetime.today())


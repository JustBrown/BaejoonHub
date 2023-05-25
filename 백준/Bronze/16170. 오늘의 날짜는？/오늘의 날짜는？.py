from datetime import datetime
now = datetime.utcnow()
print(now.year, str(now.month).zfill(2), str(now.day).zfill(2), sep='\n')
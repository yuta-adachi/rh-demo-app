import datetime
from app import save_data, load_data

save_data("新宿", "渋谷", "テスト",datetime.datetime(2020,10,31, 0))

print(load_data())
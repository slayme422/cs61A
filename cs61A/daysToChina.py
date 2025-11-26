from datetime import date
from unicodedata import lookup
today=date(2025,7,18)
print('今天的日子'+str(today))
smile_face=lookup('WHITE SMILING Face')
snow_man=lookup('SNOWMAN')
backToChina=date(2025,8,19)
length=backToChina-today
print(f'{snow_man}回中国的日子{smile_face}还差{length}')



import time
import random

ran = (25,26,27,28,29,30,31,32,33,34,35)
print(ran)
now = time.localtime()

current_day=time.strftime("%A",now)
current_month=time.strftime("%B",now)
current_numday=time.strftime("%d",now)

print("The lucky numbers for",current_day,",",current_month,current_numday,"are --->", random.choice(ran),random.choice(ran),random.choice(ran),random.choice(ran),random.choice(ran),random.choice(ran),random.choice(ran))



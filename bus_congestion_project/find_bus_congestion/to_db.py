import csv
import pandas as pd
from find_bus_congestion.models import Stock



with open(‘bus_list.csv’,‘r’) as f:
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
ss = []
for i in range(len(s)):
    st = (s[‘BUS’][i], s[‘ARS’][i], s[‘terminal’][i])
    ss.append(st)
for i in range(len(s)):
    Stock.objects.create(bus_number=ss[i][0], bus_ars_number=ss[i][1], bus_stop=ss[i][2])
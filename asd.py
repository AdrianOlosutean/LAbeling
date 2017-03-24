import pandas as pd
from datetime import timedelta
import time
from sklearn.preprocessing import MultiLabelBinarizer

df = pd.read_csv("OrdonezA_ADLs.csv",header="infer", error_bad_lines=False)
df['startTime'] = pd.to_datetime(df['startTime'])
df['endTime'] = pd.to_datetime(df['endTime'])

t1 = df['startTime']
t2 = df['endTime']
diff = t2 - t1
df['period'] = diff / timedelta(minutes=1)

start_hour = t1.map(lambda x: x.hour)
df['startHour'] = start_hour
df = df[['period','activity','startHour']]

dummies = pd.get_dummies(df)

print()
import pandas as pd

df = pd.read_csv('data.csv')
data = df.values.tolist()
print(data)

for index, row in df.iterrows():
    print(row.tolist())
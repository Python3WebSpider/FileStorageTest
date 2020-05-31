import pandas as pd

data = [
    {'id': '10001', 'name': 'Mike', 'age': 20},
    {'id': '10002', 'name': 'Bob', 'age': 22},
    {'id': '10003', 'name': 'Jordan', 'age': 21},
]

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)
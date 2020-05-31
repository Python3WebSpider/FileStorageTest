import json

with open('data.json', encoding='utf-8') as file:
    str = file.read()
    data = json.loads(str)
    print(data)
    
data = json.load(open('data.json', encoding='utf-8'))
print(data)
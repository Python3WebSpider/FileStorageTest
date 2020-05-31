import json

data = [{
    'name': ' 王伟 ',
    'gender': ' 男 ',
    'birthday': '1992-10-18'
}]

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2))
    
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
    
json.dump(data, open('data.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
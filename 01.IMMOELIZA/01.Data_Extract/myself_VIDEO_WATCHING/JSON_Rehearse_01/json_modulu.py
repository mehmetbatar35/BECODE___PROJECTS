import json

person_string = '{"name": "Gurcan", "languages": ["Python", "C#"]}'
person_dict = {"name": "Naim", "languages": ["Python", "C#"]}

# results = json.loads(person_string)

#JSON TO DICT
'''
with open("person.json") as f:
    data = json.load(f)
    print(data)
    print(data['name'])
    print(data['languages'])
    print(data['languages'][0])
'''

#DICT TO JSON (BUNU YAPMADAN ONCE JSON'UN ICINI BOSALT.)
'''
person_dict = {
    "name": "Naim",
    "languages": ["Python", "C#"]
}

result = json.dumps(person_dict)

print(type(result), '\n',
result)

with open('person.json', 'w') as f:
    json.dump(person_dict, f)
'''

person_dict = json.loads(person_string)

result = json.dumps(person_dict, indent= 4, sort_keys = True)

print(result)

# print(type(person_dict), '\n', person_dict)
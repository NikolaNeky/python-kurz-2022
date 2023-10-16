import json
with open('body.json', encoding='utf-8') as file:
    students_body = json.load(file)
print(students_body)

import json
with open('bonusy.json', encoding='utf-8') as file:
    students_bonusy = json.load(file)
print(students_bonusy)


novy_slovnik_znamky = {}

for key, value in students_body.items():

    if key in students_bonusy:
        body_bonusy = students_bonusy[key]
    else:
        body_bonusy = 0
    
    celkem = value + body_bonusy

    if celkem >= 90:
        novy_slovnik_znamky[key] = 1
    elif celkem >= 70:
        novy_slovnik_znamky[key] = 2
    elif celkem >= 50:
        novy_slovnik_znamky[key] = 3
    elif celkem >= 30:
        novy_slovnik_znamky[key] = 4
    else:
        novy_slovnik_znamky[key] = 5

print(novy_slovnik_znamky)


with open('znamky.json', 'w', encoding='utf-8') as file:
    json.dump(novy_slovnik_znamky, file, ensure_ascii=False)

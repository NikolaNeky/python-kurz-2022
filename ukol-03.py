import json
with open('body.json', encoding='utf-8') as file:
    students = json.load(file)
print(students)

novy_slovnik = {}

for key, value in students.items():

    if value >= 60:
        novy_slovnik[key] = "Pass"

    else:
        novy_slovnik[key] = "Fail"

with open('prospech.json', 'w', encoding='utf-8') as file:
    json.dump(novy_slovnik, file, ensure_ascii=False)
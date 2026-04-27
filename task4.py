import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

best = students[0]
worst = students[0]
count = 0
sum = 0

for student in students:
    if student["grade"] > best["grade"]:
        best = student
    if student["grade"] < worst["grade"]:
        worst = student
    sum+=student["grade"]
    count+=1

average = round(sum / count, 1)

print(f"Eng yaxshi talaba: {best['name']} — {best['grade']}")
print(f"Eng past baho: {worst['name']} — {worst['grade']}")
print(f"O'rtacha baho: {average}")
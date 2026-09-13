studentsScore = [98, 79, 59, 66, 93, 52, 61, 74, 74, 74, 65, 56, 77]
studensNames = ['amir', 'ahmad', 'hasib', 'enayat', 'zabih', 'adnan']
min = 100
max = 1
average = 0
total = 0
for studentscore in studentsScore:
    total += studentscore
    if studentscore < min:
        min = studentscore
    if studentscore > max:
        max = studentscore
average = total / len(studentsScore)

print(f"average is: {average} , min is: {min} , max is: {max} , and total scores is: {total}")

for name, score in zip(studensNames, studentsScore):
    print(name, score)
#===================================================================================
passing_score = [score for score in studentsScore if score >= 60]

print(passing_score)
#===================================================================================
unique_scores = set(passing_score)

print(unique_scores)
#=================================================================================
Students1 = {
    101: "Amir",
    102: "Ahmad",
    103: "Adnan",
    104: "Sharif"
}

s1 = Students1[101]
print(s1)

for index, student in enumerate(Students1, start=1):
    print(index, Students1[student])
#=================================================================================

Students = [
    {"id": 101, "name": "Amir", "score": 99},
    {"id": 102, "name": "Adnan", "score": 92},
    {"id": 103, "name": "Sharif", "score": 93},
    {"id": 104, "name": "Ahmad", "score": 94}
]

sorted_students_by_score = sorted(Students, key=lambda student : student["score"], reverse=True)

print(sorted_students_by_score)










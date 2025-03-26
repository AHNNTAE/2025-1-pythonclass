score = int(input("Enter your score: "))

if score > 60:
    grade = 'Pass'

print(grade)

score = int(input("Enter your score: "))

if score > 60:
    grade = 'Pass'
else:
		grade = 'Fail'

print(grade)

score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'
if score >= 80:
    grade = 'B'
if score >= 70:
    grade = 'C'
if score >= 60:
    grade = 'D'
if score < 60:
    grade = 'F'

print(grade)

score = int(input("Enter your score: "))

if score >= 90: grade = 'A'         # 90 이상일 경우 A
elif score >= 80: grade = 'B'       # 80 이상일 경우 B
elif score >= 70: grade = 'C'       # 70 이상일 경우 C
elif score >= 60: grade = 'D'       # 60 이상일 경우 D
else: grade = 'F'                   # 모든 조건에 만족하지 못할 경우 F

print(grade)
students = [
    {
        "name": "Alice",
        "age": 17,
        "gender": "Female",
        "address": {
            "city": "Phnom Penh",
            "district": "Chamkarmon"
        },
        "subjects": [
            {"name": "Math", "score": 85},
            {"name": "Physics", "score": 78},
            {"name": "Biology", "score": 90}
        ]
    },
    {
        "name": "Sokha",
        "age": 16,
        "gender": "Male",
        "address": {
            "city": "Siem Reap",
            "district": "Svay Dangkum"
        },
        "subjects": [
            {"name": "English", "score": 75},
            {"name": "Computer", "score": 88},
            {"name": "Art", "score": 92}
        ]
    },
    {
        "name": "Dara",
        "age": 18,
        "gender": "Male",
        "address": {
            "city": "Battambang",
            "district": "Battambang"
        },
        "subjects": [
            {"name": "History", "score": 60},
            {"name": "Geography", "score": 70},
            {"name": "Math", "score": 80}
        ]
    }
]
#Q1
count = 0
for student in students:
    if student["gender"] == "Male":
        count += 1
print(count)

#Q2
count = 0
for student in students:
    for subject in student["subjects"]:
        if subject["name"] == "Math":
            count += 1
print(count)

#Q3
total_score = 0
average_score = 0
for student in students:
    for subject in student["subjects"]:
        if student["name"] == "Sokha":
            total_score += subject["score"]
            average_score += 1
print(total_score/average_score)

#Q4
total_score = 0
for student in students:
     for subject in student["subjects"]:
        if student["name"] == "Dara":
            total_score += subject["score"]
print(total_score)
        



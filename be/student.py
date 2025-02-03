import random
import createData
class Student:
    def __init__(self, id, name, address, phone, language):
        self.id = id  # Căn cước công dân
        self.name = name
        self.address = address
        self.phone = phone
        self.language = language

class EnglishStudent(Student):
    def __init__(self, id, name, address, phone, initial_level, exam_score, target_score):
        super().__init__(id, name, address, phone, "English")
        self.initial_level = initial_level  # Trình độ ban đầu (IELTS/TOEFL)
        self.exam_score = exam_score  
        self.target_score = target_score 

class JapaneseStudent(Student):
    def __init__(self, id, name, address, phone, initial_level, exam_result, target_level):
        super().__init__(id, name, address, phone, "Japanese")
        self.initial_level = initial_level  # Trình độ ban đầu (N5, N4, ...)
        self.exam_result = exam_result  
        self.target_level = target_level  

class KoreanStudent(Student):
    def __init__(self, id, name, address, phone, initial_level, exam_result, target_level):
        super().__init__(id, name, address, phone, "Korean")
        self.initial_level = initial_level  # Trình độ ban đầu (Sơ cấp, Trung cấp, ...)
        self.exam_result = exam_result  
        self.target_level = target_level  

def creat_initial_goal(language):
    if language == 'English':
        listLevelEn = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
        return random.choice(listLevelEn)
    elif language == 'Japanese':
        listLevelJa = ['N5', 'N4', 'N3', 'N2', 'N1']
        return random.choice(listLevelJa)
    else:
        listLevelKo = ['Sơ cấp', 'Trung cấp', 'Cao cấp']
        return random.choice(listLevelKo)
    # Tạo một sinh viên
def create_student():
    id = random.randint(10000000, 99999999)
    name = createData.createName()
    address = createData.createLocal()
    phone = createData.createPhone()
    language = random.choice(['English', 'Japanese', 'Korean'])
    if language == 'English':
        initial_level = creat_initial_goal(language)
        exam_score = random.randint(0, 100)
        target_score = random.randint(0, 100)
        return EnglishStudent(id, name, address, phone, initial_level, exam_score, target_score)
    elif language == 'Japanese':
        initial_level = creat_initial_goal(language)
        exam_result = random.randint(0, 100)
        target_level = creat_initial_goal(language)
        return JapaneseStudent(id, name, address, phone, initial_level, exam_result, target_level)
    else:
        initial_level = creat_initial_goal(language)
        exam_result = random.randint(0, 100)
        target_level = creat_initial_goal(language)
        return KoreanStudent(id, name, address, phone, initial_level, exam_result, target_level)
# Tạo danh sách sinh viên
def create_students(n):
    students = []
    for _ in range(n):
        students.append(create_student())
    return students
# students = create_students(10)
# for student in students:
#     print(student.__dict__)
#     print()
# students = create_students(10)
# for student in students:
#     print(student.__dict__)
#     print()
# students = create_students(10)
# for student in students:
#     print(student.__dict__)
#     print()
# students = create_students(10)
# for student in students:
#     print(student.__dict__)

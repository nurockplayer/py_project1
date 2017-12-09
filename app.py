import sys, json


class Class:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    @staticmethod
    def from_students_json(data):
        if data is None:
            return
        class_tmp = Class()
        for item in data:
            student = Student.from_json(item)
            class_tmp.add_student(student)
        return class_tmp

    def print_all_student(self):
        for student in self.students:
            student.print()

    def to_json(self):
        data = []
        for student in self.students:
            data.append(student.to_json())
        return data

    def write_json(self, path):
        with open(path, 'w') as file:
            json.dump(self.to_json(), file)


class Student:
    def __init__(self, id=-1, name=""):
        self.id = id
        self.name = name

    @staticmethod #decorator
    def from_json(data):
        student = Student()
        if data is None:
            return
        student.id = str(data['id'])
        student.name = data['name']
        return student

    def to_json(self):
        data = {
            'id': self.id,
            'name': self.name
        }
        return data

    def print(self):
        print("Student id: {}, name: {}".format(self.id, self.name))



def main():
    class_a = Class()
    with open('./config.json', 'r') as file:
        data = json.loads(file.read())
        class_a = Class.from_students_json(data)

    if sys.argv[1] == "add_student":
        id = sys.argv[2]
        name = sys.argv[3]
        student = Student(id, name)
        class_a.add_student(student)
        class_a.write_json('./config.json')
    elif sys.argv[1] == 'print_students':
        class_a.print_all_student()


if __name__ == "__main__":
    main()

# class_b = Class.from_students_json([
#     {
#         "id": 1234,
#         "name": "sxxx"
#     },
#     {
#         "id": 1234,
#         "name": "sxxx"
#     }
# ])

#
#
# a = Student(100, "redhuang")
# b = Student(120, "chocolate")
# c = Student(123, "123")
# d = Student.from_json({
#     "id": 1234,
#     "name": 'rexhuang'
# })
#
# class_a = Class()
# class_a.add_student(a)
# class_a.add_student(b)
# class_a.add_student(c)
# class_a.add_student(d)
#
# class_a.print_all_student()
#
# class_b = Class.from_students_json([
#     {
#         "id": 1234,
#         "name": "sxxx"
#     },
#     {
#         "id": 1234,
#         "name": "sxxx"
#     }
# ])
# class_b.print_all_student()
#

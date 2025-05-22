class student:
    count = 0
    total_gpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.total_gpa += gpa


        #instance method
    def get_info(self):
        return f"Name: {self.name},has  GPA: {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number  of students: {cls.count}"
    @classmethod
    def get_total_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa/cls.count:.2f}"



student1 = student("Alex",3.5)
student2 = student("John",3.7)

print(student.get_count())
print(student.get_total_gpa())
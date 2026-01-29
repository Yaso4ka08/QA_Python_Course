"""Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент", який дозволяє змінювати
 середній бал студента.
 Виведіть інформацію про студента та змініть його середній бал."""


class Student:
    def __init__(self, name, last_name, age, overall_grade):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.overall_grade = overall_grade

    def change_grade(self, new_grade):
        self.overall_grade = new_grade

    def get_info(self):
        return(
            f"Name: {self.name}\n"
            f"Last Name: {self.last_name}\n"
            f"Age: {self.age}\n"
            f"Overall Grade: {self.overall_grade}"
        )

new_student = Student("Yana","Revenkova", 34, 80)
new_student.change_grade(87)
print(new_student.get_info())


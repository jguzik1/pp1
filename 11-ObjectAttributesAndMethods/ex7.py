class student():
    university = "UEK Krakow"
    id = 100000
    def __init__(self,name,surname,field_of_study):
        self.name = name
        self.surname = surname
        self.field_of_study = field_of_study
        self.id = student.id
        student.id += 1
    

    def __str__(self):
        return f'{self.name} {self.surname} ({self.id}), {self.field_of_study}, {student.university}'

example1 = student('Anna', 'Maj', 'Appliied Informatics')
example2 = student('Anna', 'Maj', 'Appliied Informatics')
print(example1)
print(example2)
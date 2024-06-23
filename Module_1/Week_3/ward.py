class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f"Name: {self.name}")
        print(f"Year of birth: {self.yob}")
        print(f"Grade: {self.grade}")


class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(f"Name: {self.name}")
        print(f"Year of birth: {self.yob}")
        print(f"Specialist: {self.specialist}")


class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(f"Name: {self.name}")
        print(f"Year of birth: {self.yob}")
        print(f"Subject: {self.subject}")


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def count_doctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)

    def compute_average(self):
        total_yob = 0
        teacher_count = 0
        for person in self.people:
            if isinstance(person, Teacher):
                total_yob += person.yob
                teacher_count += 1

        if teacher_count == 0:
            return 0  # Avoid division by zero if no teachers
        else:
            return total_yob / teacher_count

    def describe(self):
        print(f"Ward name: {self.name}")
        print("People in the ward:")
        for person in self.people:
            person.describe()
            print("-" * 20)


# Create a ward object
my_ward = Ward("Ward A")

# Create people objects
student1 = Student("Alice", 2005, "10th Grade")
teacher1 = Teacher("Bob", 1980, "Math")
teacher2 = Teacher("Carol", 1985, "Science")
doctor1 = Doctor("David", 1975, "Cardiologist")
doctor2 = Doctor("Emily", 1982, "Pediatrician")

# Add people to the ward
my_ward.add_person(student1)
my_ward.add_person(teacher1)
my_ward.add_person(teacher2)
my_ward.add_person(doctor1)
my_ward.add_person(doctor2)

# Soft
my_ward.sort_age()

# Describe the ward
my_ward.describe()

# Count doctor:
num_doctors = my_ward.count_doctor()
print(f"Number of doctors in the ward: {num_doctors}")

# Compute average year of birth for teachers
average_yob = my_ward.compute_average()
print(f"Average year of birth for teachers: {average_yob}")

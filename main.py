from school import School
from person import Teacher, Student
from subject import Subject
from classroom import Classroom

# Create an school object 
school = School("ABC", "India")

# create some classroom 
eight = Classroom("Eight")
nine = Classroom("Nine")
ten = Classroom("Ten")

# add classrooms to the school 
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# add students to the school
std1 = Student("Bluyi", eight)
std2 = Student("Priya", nine)
std3 = Student("Sabana", eight)
std4 = Student("Firoza", ten)
std5 = Student("Afreen", nine)

# make admission of these students
school.student_admission(std1)
school.student_admission(std2)
school.student_admission(std3)
school.student_admission(std4)
school.student_admission(std5)

# Add teachers
teacher1 = Teacher("AB Sir")
teacher2 = Teacher("BD Sir")
teacher3 = Teacher("JM Mam")
teacher4 = Teacher("MP Mam")
teacher5 = Teacher("MSB Sir")

# adding subjects with assiging the teachers 
bengali = Subject("Bangla", teacher1)
english = Subject("English", teacher2)
physics = Subject("Physics", teacher3)
chemistry = Subject("Chemistry", teacher2)
mca = Subject("MCA", teacher4)
maths = Subject("Mathematics", teacher5)
biology = Subject("Biology", teacher1)

# assiging subjects to the classroom 
eight.add_subject(bengali)
eight.add_subject(physics)
eight.add_subject(chemistry)
eight.add_subject(maths)
nine.add_subject(bengali)
nine.add_subject(biology)
nine.add_subject(maths)
ten.add_subject(physics)
ten.add_subject(mca)
ten.add_subject(english)
ten.add_subject(biology)

# Take exam 
eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

# print the school 
print(school)

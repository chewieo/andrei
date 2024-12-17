import os

class StudentInfo:
    def __init__(self, name, age, student_id, email, phone):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.email = email
        self.phone = phone

# Load students from the database
students = [
    StudentInfo("Condez", "19", "07531", "condez.kenjo@lpunetwork.edu.ph", "09584371562"),
    StudentInfo("Fajarillo", "20", "94367", "fajarillo.Jlouisse@lpunetwork.edu.ph", "09375816427"),
    StudentInfo("Dy", "19", "49103", "dy.shane@lpunetwork.edu.ph", "09185672402"),
    StudentInfo("Cadiz", "20", "05732", "cadiz.mark@lpunetwork.edu.ph", "09457796348"),
    StudentInfo("Al Zarouni", "20", "03348", "takamura.yosh@lpunetwork.edu.ph", "09997531598"),
    StudentInfo("Valzado", "23", "67134", "valzado.aeron@lpunetwork.edu.ph", "09732511631"),
    StudentInfo("Lee", "21", "17926", "lee.val@lpunetwork.edu.ph", "09753654159"),
    StudentInfo("Torres", "20", "92573", "torres.dominic@lpunetwork.edu.ph", "09890123456"),
    StudentInfo("Mariano", "19", "02192", "mariano.andrei@lpunetwork.edu.ph", "09901234567"),
    StudentInfo("Fortuno", "25", "74218", "fortuno.renz@lpunetwork.edu.ph", "09324862495"),
]

database_path = "database.txt"
if os.path.exists(database_path):
    with open(database_path, "r") as file:
        for line in file:
            # Ensure the line has all required fields
            fields = line.strip().split(", ")
            if len(fields) == 5:  # Only process valid lines
                name, age, student_id, email, phone = fields
                students.append(StudentInfo(name, age, student_id, email, phone))
            else:
                print(f"Skipping malformed line: {line.strip()}")

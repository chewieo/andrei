def save_student():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    student_id = id_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()

    # Collect missing fields
    missing_fields = []
    if not name:
        missing_fields.append("Name")
    if not age:
        missing_fields.append("Age")
    if not student_id:
        missing_fields.append("Student ID")
    if not email:
        missing_fields.append("Email")
    if not phone:
        missing_fields.append("Phone")

    # Show error if there are missing fields
    if missing_fields:
        messagebox.showerror("Error", f"The following fields are empty: {', '.join(missing_fields)}")
        return

    # Add student to the list
    new_student = StudentInfo(name, age, student_id, email, phone)
    students.append(new_student)

    # Save student to the database file
    with open(database_path, "a") as file:
        file.write(f"{name}, {age}, {student_id}, {email}, {phone}\n")

    messagebox.showinfo("Success", f"Student {name} added successfully!")

    # Clear input fields
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    id_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)

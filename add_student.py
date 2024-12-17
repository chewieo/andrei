from tkinter import *
from tkinter import messagebox
from student import students, StudentInfo
import os

database_path = "database.txt"

def display_add_student_form(content_frame):
    def clear_content():
        for widget in content_frame.winfo_children():
            widget.destroy()

    def save_student():
        name = name_entry.get().strip()
        age = age_entry.get().strip()
        student_id = id_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()

        # Collect specific error messages for missing fields
        error_messages = []
        if not name:
            error_messages.append("- You forgot to add the Name.")
        if not age:
            error_messages.append("- You forgot to add the Age.")
        if not student_id:
            error_messages.append("- You forgot to add the Student ID.")
        if not email:
            error_messages.append("- You forgot to add the Email.")
        if not phone:
            error_messages.append("- You forgot to add the Phone.")

        # Show error messages if there are missing fields
        if error_messages:
            error_text = "The following errors occurred:\n" + "\n".join(error_messages)
            messagebox.showerror("Error", error_text)
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

    clear_content()

    Label(content_frame, text="Add Student Form", font=("Segoe UI", 16), bg="white").pack(pady=10)

    # Form fields
    Label(content_frame, text="Name:", font=("Segoe UI", 12), bg="white").pack(pady=5)
    name_entry = Entry(content_frame, width=40, font=("Segoe UI", 12), relief="solid", bd=1)
    name_entry.pack(pady=5)

    Label(content_frame, text="Age:", font=("Segoe UI", 12), bg="white").pack(pady=5)
    age_entry = Entry(content_frame, width=40, font=("Segoe UI", 12), relief="solid", bd=1)
    age_entry.pack(pady=5)

    Label(content_frame, text="Student ID:", font=("Segoe UI", 12), bg="white").pack(pady=5)
    id_entry = Entry(content_frame, width=40, font=("Segoe UI", 12), relief="solid", bd=1)
    id_entry.pack(pady=5)

    Label(content_frame, text="Email:", font=("Segoe UI", 12), bg="white").pack(pady=5)
    email_entry = Entry(content_frame, width=40, font=("Segoe UI", 12), relief="solid", bd=1)
    email_entry.pack(pady=5)

    Label(content_frame, text="Phone:", font=("Segoe UI", 12), bg="white").pack(pady=5)
    phone_entry = Entry(content_frame, width=40, font=("Segoe UI", 12), relief="solid", bd=1)
    phone_entry.pack(pady=5)

    # Save button
    Button(content_frame, text="Save", font=("Segoe UI", 12), bg="#3b3b3b", fg="white", relief="flat", command=save_student).pack(pady=20)

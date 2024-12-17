from tkinter import *
from tkinter import messagebox
from student import students
from add_student import display_add_student_form

def open_admin_window():
    def clear_content():
        for widget in content_frame.winfo_children():
            widget.destroy()

    def view_all_students_admin():
        clear_content()

        Label(content_frame, text="All Students", font=("Segoe UI", 16), bg="white").pack(pady=10)

        # Scrollable frame setup
        canvas = Canvas(content_frame, bg="white", highlightthickness=0)
        scrollbar = Scrollbar(content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="white")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")

        # Add table headers
        headers = ["Name", "Age", "Student ID", "Email", "Phone"]
        for col, header in enumerate(headers):
            Label(scrollable_frame, text=header, font=("Segoe UI", 12, "bold"), bg="white", anchor="w", width=15).grid(row=0, column=col, padx=5, pady=5, sticky="w")

        # Populate student information in aligned rows
        for row, student in enumerate(students, start=1):
            Label(scrollable_frame, text=student.name, font=("Segoe UI", 12), bg="white", anchor="w", width=15).grid(row=row, column=0, padx=5, pady=5, sticky="w")
            Label(scrollable_frame, text=student.age, font=("Segoe UI", 12), bg="white", anchor="w", width=5).grid(row=row, column=1, padx=5, pady=5, sticky="w")
            Label(scrollable_frame, text=student.student_id, font=("Segoe UI", 12), bg="white", anchor="w", width=15).grid(row=row, column=2, padx=5, pady=5, sticky="w")
            Label(scrollable_frame, text=student.email, font=("Segoe UI", 12), bg="white", anchor="w", width=25).grid(row=row, column=3, padx=5, pady=5, sticky="w")
            Label(scrollable_frame, text=student.phone, font=("Segoe UI", 12), bg="white", anchor="w", width=15).grid(row=row, column=4, padx=5, pady=5, sticky="w")

    def edit_student_admin():
        clear_content()

        Label(content_frame, text="Edit Student Info", font=("Segoe UI", 16), bg="white").pack(pady=10)
        Label(content_frame, text="Enter Student ID to Edit:", font=("Segoe UI", 12), bg="white").pack(pady=5)
        student_id_entry = Entry(content_frame, font=("Segoe UI", 12), relief="solid", bd=1)
        student_id_entry.pack(pady=5)

        def fetch_and_edit():
            student_id = student_id_entry.get().strip()
            for student in students:
                if student.student_id == student_id:
                    clear_content()

                    Label(content_frame, text="Edit Student Info", font=("Segoe UI", 16), bg="white").pack(pady=10)

                    Label(content_frame, text="Name:", font=("Segoe UI", 12), bg="white").pack(pady=5)
                    name_entry = Entry(content_frame, font=("Segoe UI", 12), relief="solid", bd=1)
                    name_entry.insert(0, student.name)
                    name_entry.pack(pady=5)

                    Label(content_frame, text="Age:", font=("Segoe UI", 12), bg="white").pack(pady=5)
                    age_entry = Entry(content_frame, font=("Segoe UI", 12), relief="solid", bd=1)
                    age_entry.insert(0, student.age)
                    age_entry.pack(pady=5)

                    Label(content_frame, text="Email:", font=("Segoe UI", 12), bg="white").pack(pady=5)
                    email_entry = Entry(content_frame, font=("Segoe UI", 12), relief="solid", bd=1)
                    email_entry.insert(0, student.email)
                    email_entry.pack(pady=5)

                    Label(content_frame, text="Phone:", font=("Segoe UI", 12), bg="white").pack(pady=5)
                    phone_entry = Entry(content_frame, font=("Segoe UI", 12), relief="solid", bd=1)
                    phone_entry.insert(0, student.phone)
                    phone_entry.pack(pady=5)

                    def save_changes():
                        student.name = name_entry.get().strip()
                        student.age = age_entry.get().strip()
                        student.email = email_entry.get().strip()
                        student.phone = phone_entry.get().strip()

                        with open("database.txt", "w") as file:
                            for s in students:
                                file.write(f"{s.name}, {s.age}, {s.student_id}, {s.email}, {s.phone}\n")

                        messagebox.showinfo("Success", f"Student {student_id} updated successfully!")
                        view_all_students_admin()

                    Button(content_frame, text="Save Changes", font=("Segoe UI", 12), bg="#3b3b3b", fg="white", command=save_changes).pack(pady=20)
                    return
            messagebox.showerror("Error", "Student not found!")

        Button(content_frame, text="Fetch Info", font=("Segoe UI", 12), bg="#3b3b3b", fg="white", command=fetch_and_edit).pack(pady=10)

    def delete_student_admin():
        clear_content()

        Label(content_frame, text="Delete Student", font=("Segoe UI", 16), bg="white").pack(pady=10)
        Label(content_frame, text="Enter Student ID to Delete:", font=("Segoe UI", 12), bg="white").pack(pady=5)
        student_id_entry = Entry(content_frame, font=("Segoe UI", 12), relief="solid", bd=1)
        student_id_entry.pack(pady=5)

        def delete_student():
            student_id = student_id_entry.get().strip()
            for student in students:
                if student.student_id == student_id:
                    students.remove(student)

                    with open("database.txt", "w") as file:
                        for s in students:
                            file.write(f"{s.name}, {s.age}, {s.student_id}, {s.email}, {s.phone}\n")

                    messagebox.showinfo("Success", f"Student {student_id} deleted successfully!")
                    view_all_students_admin()
                    return
            messagebox.showerror("Error", "Student not found!")

        Button(content_frame, text="Delete", font=("Segoe UI", 12), bg="#3b3b3b", fg="white", command=delete_student).pack(pady=10)

    admin_window = Tk()
    admin_window.title("Admin Panel")
    admin_window.geometry("1280x800")
    admin_window.configure(bg="#2b2b2b")

    menu_frame = Frame(admin_window, bg="#3b3b3b", width=220)
    menu_frame.pack(side="left", fill="y")

    content_frame = Frame(admin_window, bg="white")
    content_frame.pack(side="right", fill="both", expand=True)

    def create_menu_button(text, command):
        button = Button(menu_frame, text=text, font=("Segoe UI", 14), bg="#444444", fg="white", command=command)
        button.pack(fill="x", padx=10, pady=10)
        button.bind("<Enter>", lambda e: button.config(bg="#575757"))
        button.bind("<Leave>", lambda e: button.config(bg="#444444"))

    Label(menu_frame, text="Admin Menu", font=("Segoe UI", 16, "bold"), bg="#3b3b3b", fg="white").pack(pady=20)

    create_menu_button("View All Students", view_all_students_admin)
    create_menu_button("Add Student", lambda: display_add_student_form(content_frame))
    create_menu_button("Edit Student Info", edit_student_admin)
    create_menu_button("Delete Student", delete_student_admin)
    create_menu_button("Exit", admin_window.destroy)

    clear_content()
    Label(content_frame, text="Welcome to Admin Panel!", font=("Segoe UI", 20), bg="white").pack(pady=50)

    admin_window.mainloop()

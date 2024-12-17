from tkinter import *
from tkinter import messagebox
from student import students

def open_main_window(student):
    def clear_content():
        for widget in content_frame.winfo_children():
            widget.destroy()

    def create_menu_button(text, command):
        button = Button(menu_frame, text=text, font=("Segoe UI", 14), bg="#3b3b3b", fg="white", 
                        activebackground="#575757", activeforeground="white", relief="flat", command=command)
        button.pack(fill="x", padx=10, pady=10)
        button.bind("<Enter>", lambda e: button.config(bg="#575757"))
        button.bind("<Leave>", lambda e: button.config(bg="#3b3b3b"))

    def add_student():
        from add_student import display_add_student_form
        display_add_student_form(content_frame)

    def view_student_info():
        clear_content()
        Label(content_frame, text=f"Name: {student.name}", font=("Segoe UI", 16), bg="white").pack(pady=5)
        Label(content_frame, text=f"Age: {student.age}", font=("Segoe UI", 16), bg="white").pack(pady=5)
        Label(content_frame, text=f"Student ID: {student.student_id}", font=("Segoe UI", 16), bg="white").pack(pady=5)
        Label(content_frame, text=f"Email: {student.email}", font=("Segoe UI", 16), bg="white").pack(pady=5)
        Label(content_frame, text=f"Phone: {student.phone}", font=("Segoe UI", 16), bg="white").pack(pady=5)

    def search_student_info():
        clear_content()
        Label(content_frame, text="Search Student Info", font=("Segoe UI", 16), bg="white").pack(pady=10)

        Label(content_frame, text="Enter Student ID:", font=("Segoe UI", 12), bg="white").pack(pady=5)
        search_entry = Entry(content_frame, width=40, font=("Segoe UI", 12), relief="solid", bd=1)
        search_entry.pack(pady=5)

        def perform_search():
            student_id = search_entry.get()
            for s in students:
                if s.student_id == student_id:
                    clear_content()
                    Label(content_frame, text=f"Name: {s.name}", font=("Segoe UI", 16), bg="white").pack(pady=5)
                    Label(content_frame, text=f"Age: {s.age}", font=("Segoe UI", 16), bg="white").pack(pady=5)
                    Label(content_frame, text=f"Student ID: {s.student_id}", font=("Segoe UI", 16), bg="white").pack(pady=5)
                    Label(content_frame, text=f"Email: {s.email}", font=("Segoe UI", 16), bg="white").pack(pady=5)
                    Label(content_frame, text=f"Phone: {s.phone}", font=("Segoe UI", 16), bg="white").pack(pady=5)
                    return
            messagebox.showinfo("Not Found", "No student found with that ID!")

        Button(content_frame, text="Search", font=("Segoe UI", 12), bg="#3b3b3b", fg="white", relief="flat", command=perform_search).pack(pady=10)

    def view_all_students():
        clear_content()
        Label(content_frame, text="All Students", font=("Segoe UI", 16), bg="white").pack(pady=10)
        for s in students:
            Label(content_frame, text=f"{s.name} ({s.student_id})", font=("Segoe UI", 12), bg="white").pack(pady=2)

    def exit_app():
        main_window.destroy()

    main_window = Tk()
    main_window.title("Student Info GUI")
    main_window.geometry(f"1280x800+{(main_window.winfo_screenwidth() - 1280) // 2}+{(main_window.winfo_screenheight() - 800) // 2}")

    menu_frame = Frame(main_window, bg="#2b2b2b", width=220, relief="sunken")
    menu_frame.pack(side="left", fill="y")

    content_frame = Frame(main_window, bg="white")
    content_frame.pack(side="right", fill="both", expand=True)

    Label(menu_frame, text="Menu", font=("Segoe UI", 16, "bold"), bg="#2b2b2b", fg="white").pack(pady=20)

    create_menu_button("Add Student", add_student)
    create_menu_button("View Student Info", view_student_info)
    create_menu_button("Search Student Info", search_student_info)
    create_menu_button("View All Students", view_all_students)
    create_menu_button("Exit", exit_app)

    clear_content()
    Label(content_frame, text=f"Welcome, {student.name}!", font=("Segoe UI", 20), bg="white").pack(pady=50)

    main_window.mainloop()

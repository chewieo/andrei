from tkinter import *
from tkinter import ttk
from student import students

def view_all_students(content_frame):
    def clear_content():
        for widget in content_frame.winfo_children():
            widget.destroy()

    clear_content()

    Label(content_frame, text="All Students", font=("Segoe UI", 16), bg="white").pack(pady=10)

    # Create a canvas and a frame for scrolling
    canvas = Canvas(content_frame, bg="white", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    scrollable_frame = Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Configure scrolling
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", on_frame_configure)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Populate the scrollable frame with student details
    if not students:
        Label(scrollable_frame, text="No students found!", font=("Segoe UI", 12), bg="white").pack(pady=5)
    else:
        for s in students:
            student_info = (
                f"Name: {s.name}\n"
                f"Age: {s.age}\n"
                f"Student ID: {s.student_id}\n"
                f"Email: {s.email}\n"
                f"Phone: {s.phone}\n"
            )
            Label(scrollable_frame, text=student_info, font=("Segoe UI", 12), bg="white", justify="left", anchor="w").pack(pady=10, padx=10)

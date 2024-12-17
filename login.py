from tkinter import *
from tkinter import messagebox
from gui import open_main_window
from admin import open_admin_window
from student import students

def login():
    entered_id = txtboxlogin_username.get().strip()
    for student in students:
        if entered_id == student.student_id:
            messagebox.showinfo("Login Success", f"Welcome, {student.name}!")
            login_window.destroy()  # Automatically close login window
            open_main_window(student)  # Redirect to Student Menu
            return
    messagebox.showerror("Login Failed", "Invalid Student ID!")

def admin_login():
    login_window.destroy()  # Automatically close login window

    # Open the Admin Login window
    admin_login_window = Tk()
    admin_login_window.title("Admin Login")
    admin_login_window.geometry("400x300")
    admin_login_window.configure(bg="#222222")

    # Center the Admin Login window
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    center_window(admin_login_window, 400, 300)

    Label(admin_login_window, text="Admin Login", fg="#FFFFFF", bg="#222222", font=("Segoe UI", 20)).pack(pady=20)
    Label(admin_login_window, text="Admin ID:", fg="#FFFFFF", bg="#222222", font=("Segoe UI", 12)).pack(pady=5)
    admin_user_entry = Entry(admin_login_window, font=("Segoe UI", 12), relief="solid", bd=1)
    admin_user_entry.pack(pady=5)

    def validate_admin():
        entered_id = admin_user_entry.get().strip()
        try:
            # Read admin credentials from the database file
            with open("database.txt", "r") as file:
                admins = [line.strip() for line in file.readlines()]
            if entered_id in admins:
                messagebox.showinfo("Login Success", "Welcome, Admin!")
                admin_login_window.destroy()  # Close the Admin Login window
                open_admin_window()  # Redirect to Admin Menu
            else:
                messagebox.showerror("Error", "Invalid Admin ID!")
        except FileNotFoundError:
            messagebox.showerror("Error", "Admin database file not found!")

    Button(admin_login_window, text="Login", font=("Segoe UI", 12), bg="#444444", fg="#FFFFFF", command=validate_admin).pack(pady=20)

    admin_login_window.mainloop()

def login_window():
    global txtboxlogin_username, login_window
    login_window = Tk()
    login_window.title("Login")
    login_window.geometry("400x300")
    login_window.configure(bg="#222222")

    # Center the Login window
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    center_window(login_window, 400, 300)

    Label(login_window, text="Enter Student ID", fg="#FFFFFF", bg="#222222", font=("Segoe UI", 20)).pack(pady=20)

    txtboxlogin_username = Entry(login_window, width=30, font=("Segoe UI", 14), justify="center", relief="solid", bd=1)
    txtboxlogin_username.pack(pady=10)

    Button(login_window, text="Login", fg="#FFFFFF", bg="#444444", font=("Segoe UI", 14), command=login).pack(pady=10)
    Button(login_window, text="Admin Login", fg="#FFFFFF", bg="#444444", font=("Segoe UI", 12), command=admin_login).pack(pady=10)

    login_window.mainloop()

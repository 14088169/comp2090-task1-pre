import tkinter as tk
from tkinter import ttk, messagebox
from main_admin import AdminPage
from main_user import UserPage


class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        # Initialize the home page frame with admin login and user access options
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        
        ttk.Label(self, text="Please select login role", font=("Arial", 20)).pack(pady=30)

        admin_frame = ttk.LabelFrame(self, text="Admin Login", padding=20)
        admin_frame.pack(pady=15, padx=40, fill=tk.X)

        ttk.Label(admin_frame, text="Password (demo password: admin123):", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.admin_password_entry = ttk.Entry(admin_frame, width=22, show="*")
        self.admin_password_entry.grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(admin_frame, text="Login as Admin", command=self.admin_login, width=18).grid(row=1, column=0, columnspan=2, pady=10)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)
        ttk.Button(button_frame, text="Staff", command=lambda: controller.show_frame(UserPage), width=20).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Quit", command=controller.quit, width=20).pack(side=tk.LEFT, padx=10)

    def admin_login(self):
        # Handle admin login by checking the entered password and navigating to the admin page if correct
        password = self.admin_password_entry.get()
        if password == "admin123":
            self.controller.show_frame(AdminPage)
            self.admin_password_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Login Failed", "Incorrect password")


class MainApp(tk.Tk):
    def __init__(self):
        # Initialize the main application window and set up the frame container for navigation
        tk.Tk.__init__(self)
        self.title("Inventory Management System")
        self.geometry("760x480")
        
        # Enable high DPI support for better font rendering
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
        
        # Set scaling for better font clarity
        self.tk.call('tk', 'scaling', 1.7)
        
        container = ttk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (HomePage, AdminPage, UserPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(HomePage)
    
    def show_frame(self, cont):
        # Show the specified frame and refresh its content if applicable
        frame = self.frames[cont]
        frame.tkraise()
        if hasattr(frame, 'refresh_list'):
            frame.refresh_list()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

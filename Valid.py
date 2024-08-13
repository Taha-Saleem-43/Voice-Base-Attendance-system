import customtkinter as ctk
from tkinter import messagebox
import aaa as main_logic
from PIL import Image

class Application(ctk.CTk):
    def __init__(self, wtitle):
        super().__init__()
        self.title(wtitle)
        self.geometry("600x150")

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20)

        lis_image = Image.open('realmicrophone.png')
        add_image = Image.open('add.png')
        present_image = Image.open('Present.png')
        absent_image = Image.open('absent.png')
        data_image=Image.open('data.png')

        self.lis_btn = ctk.CTkImage(lis_image)
        self.add_btn = ctk.CTkImage(add_image)
        self.data_btn  = ctk.CTkImage(data_image)
        self.prst_btn  = ctk.CTkImage(present_image)
        self.abs_btn  = ctk.CTkImage(absent_image)

        self.button1 = ctk.CTkButton(self.frame, image=self.lis_btn, text="Attendance Call", width=140, height=40, command=self.Start)
        self.button1.grid(row=0,column=0, padx=10, pady=10)

        self.button2 = ctk.CTkButton(self.frame, image=self.add_btn, text="Add Student", width=140, height=40,  command=self.add)
        self.button2.grid(row=0,column=1, padx=10, pady=10)

        self.button3 = ctk.CTkButton(self.frame, image=self.data_btn , text="Show Present", width=140, height=40, command=self.show)
        self.button3.grid(row=0,column=2, padx=10, pady=10)

        self.button4 = ctk.CTkButton(self.frame, image=self.prst_btn, text="Show Prtc present", width=140, height=40, command=self.present)
        self.button4.grid(row=1,column=0, padx=10, pady=10)

        self.button5 = ctk.CTkButton(self.frame, image=self.abs_btn, text="Show Prtc  Absent", width=140, height=40, command=self.Absent)
        self.button5.grid(row=1,column=1, padx=10, pady=10)

        self.button5 = ctk.CTkButton(self.frame, image=self.data_btn , text="Show Absent", width=140, height=40, command=self.All_absent)
        self.button5.grid(row=1,column=2, padx=10, pady=10)

    def Start(self):
        try:
            main_logic.Start()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start main logic: {e}")

    def show(self):
        try:
            data = main_logic.show_data()
            if data:
                app2 = ctk.CTk()
                app2.title("Present-Students")
                self.frame_1 = ctk.CTkScrollableFrame(master=app2, width=320, height=400)
                self.frame_1.pack(padx=10, pady=10, side="left", anchor="nw",fill="both",expand=True)
                self.label_0 = ctk.CTkLabel(self.frame_1, text="Rollno\t||  Name\t         ||  Date", font=ctk.CTkFont(size=16, weight="bold"))
                self.label_0.pack(side="top", anchor="nw")
                self.label_2 = ctk.CTkLabel(self.frame_1, text="================================", font=ctk.CTkFont(size=14, weight="bold"))
                self.label_2.pack(side="top", anchor="nw")
                for row in data:
                    self.label = ctk.CTkLabel(self.frame_1, text=f"{str(row[0]).ljust(20)}{str(row[1]).ljust(15)}\t{row[2]}", font=ctk.CTkFont(size=14, weight="bold"))
                    self.label.pack(anchor="nw")
                app2.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show data: {e}")

    def All_absent(self):
        try:
            data = main_logic.show_all_Absents()
            if data:
                app9 = ctk.CTk()
                app9.title("Present-Students")
                self.frame_4 =ctk.CTkScrollableFrame(master=app9, width=320, height=400)
                self.frame_4.pack(padx=10, pady=10, side="left", anchor="nw",fill="both",expand=True)
                self.label_0 = ctk.CTkLabel(self.frame_4, text="Rollno\t||  Name\t         ||  Date", font=ctk.CTkFont(size=16, weight="bold"))
                self.label_0.pack(side="top", anchor="nw")
                self.label_2 = ctk.CTkLabel(self.frame_4, text="================================", font=ctk.CTkFont(size=14, weight="bold"))
                self.label_2.pack(side="top", anchor="nw")
                for row in data:
                    self.label = ctk.CTkLabel(self.frame_4, text=f"{str(row[0]).ljust(20)}{str(row[1]).ljust(15)}\t{row[2]}", font=ctk.CTkFont(size=14, weight="bold"))
                    self.label.pack(anchor="nw")
                app9.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show data: {e}")

    def present(self):
        try:
            data = main_logic.stu_present()
            if data:
                app3 = ctk.CTk()
                app3.title("Particular-Present-Student")
                self.frame_2 = ctk.CTkScrollableFrame(master=app3, width=320, height=400)
                self.frame_2.pack(padx=10, pady=10, side="left", anchor="nw",fill="both",expand=True)
                self.label_3 = ctk.CTkLabel(self.frame_2, text="Rollno\t ||  Name\t         ||  Date", font=ctk.CTkFont(size=14, weight="bold"))
                self.label_3.pack(side="top", anchor="nw")
                self.label_4 = ctk.CTkLabel(self.frame_2, text="===============================", font=ctk.CTkFont(size=14, weight="bold"))
                self.label_4.pack(side="top", anchor="nw")
                for row in data:
                    self.label = ctk.CTkLabel(self.frame_2, text=f"{str(row[0]).ljust(20)}{str(row[1]).ljust(15)}\t{row[2]}", font=ctk.CTkFont(size=12, weight="bold"))
                    self.label.pack(anchor="nw")
                app3.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show data: {e}")


    def Absent(self):
        try:
            data = main_logic.show_absent()
            if data:
                app5 = ctk.CTk()
                app5.title("Particular-Absent-Student")
                self.frame = ctk.CTkScrollableFrame(master=app3, width=320, height=400)
                self.frame.pack(padx=10, pady=10, side="left", anchor="nw",fill="both",expand=True)
                self.label_1 = ctk.CTkLabel(self.frame, text="Rollno\t ||  Name\t         ||  Date", font=ctk.CTkFont(size=14, weight="bold"))
                self.label_1.pack(side="top", anchor="nw")
                self.label_2 = ctk.CTkLabel(self.frame, text="===============================", font=ctk.CTkFont(size=14, weight="bold"))
                self.label_2.pack(side="top", anchor="nw")
                for row in data:
                    self.label = ctk.CTkLabel(self.frame, text=f"{str(row[0]).ljust(20)}{str(row[1]).ljust(15)}\t{row[2]}", font=ctk.CTkFont(size=12, weight="bold"))
                    self.label.pack(anchor="nw")
                app5.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show data: {e}")

    def add(self):
        app4 = ctk.CTk()
        app4.title("Add Student")
        self.label_5 = ctk.CTkLabel(app4, text="Name:", font=ctk.CTkFont(size=14, weight="bold"))
        self.label_5.grid(row=0, column=0, padx=10, pady=10)
        self.name = ctk.CTkEntry(app4)
        self.name.grid(row=0, column=1, padx=10, pady=10)
        self.label_6 = ctk.CTkLabel(app4, text="Rollno:", font=ctk.CTkFont(size=14, weight="bold"))
        self.label_6.grid(row=1, column=0, padx=10, pady=10)
        self.roll = ctk.CTkEntry(app4)
        self.roll.grid(row=1, column=1, padx=10, pady=10)
        self.bt = ctk.CTkButton(app4, text="Add", width=80, height=30, command=self.get)
        self.bt.grid(row=2, column=1, padx=10, pady=10)
        app4.mainloop()

    def get(self):
        name = self.name.get()
        rollno = self.roll.get()
        if name and rollno:
            main_logic.add_stu(name, rollno)
        else:
            messagebox.showinfo('INFO', "You must write the Name and Rollno to add the student")

def main():
    app = Application('Listening')
    app.mainloop()

if __name__ == '__main__':
    main()

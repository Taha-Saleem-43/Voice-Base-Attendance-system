import speech_recognition as sr
import win32com.client as w                #for Talking purpose
import sqlite3 as sq
from tkinter import messagebox
from word2number import w2n
from datetime import datetime
speaker=w.Dispatch("SAPI.SPVoice")     # Built in speaker class calling a function Dispatch
r = sr.Recognizer()  #Recognizer built in class in speech_recognition module


def record_text():
    with sr.Microphone() as source:
        print("Listening.....")
        # Adjust the duration of speaking before going for further processing
        try:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source,timeout=10,phrase_time_limit=5)
            return r.recognize_google(audio,language="en-pak")
        except sr.UnknownValueError:
            speaker.speak("Audio is not understandable")
            raise Exception("Check your Mic or reduce Background noice")
        except sr.RequestError:
            speaker.speak(f"Could not proceed the request check your Internet Connection")
            raise Exception(f"Could not proceed the request check your Internet Connection")


def stu_present():
    speaker.Speak("Say!  The ROLL Number to see attendance of that student")
    text = record_text()
    n=Validity_check(text)
    if n:
        con=sq.connect("Attendance.db")
        cur=con.cursor()
        cur.execute("Select * from Present_students where Rollno=?",(n,))
        r=cur.fetchall()
        if r:
            return r
        else:
            speaker.speak(f"Roll number {n} is not a Regular Student,No presents marked")
        con.close()

def add_stu(n,r):
    con=sq.connect("Attendance.db")
    cur=con.cursor()
    cur.execute("Select 1 from Data where Rollno=? ", (r,))
    valid=cur.fetchone()
    if valid:
        speaker.Speak("This Rollno is already in the Database")
    else:
        cur.execute("Insert into Data (Name , Rollno) Values (?,?) ",(n,r))
        speaker.Speak(f"{n}, Succesfully Added ")
        messagebox.showinfo('Success', f"{n} Succesfully Added ")
    con.commit()


def show_data():
    con=sq.connect("Attendance.db")
    cur=con.cursor()
    cur.execute("Select * from Present_students order by Rollno")
    rows=cur.fetchall()
    return rows

def show_all_Absents():
    con=sq.connect("Attendance.db")
    cur=con.cursor()
    cur.execute("Select * from Absent_students order by Date")
    rows=cur.fetchall()
    return rows

def absent_stu():
    con=sq.connect("Attendance.db")
    cur=con.cursor()
    d=datetime.now().strftime("%d-%m-%Y")
    cur.execute("Create Table if not Exists Absent_students (Rollno int, Name Text, Date Text)")
    cur.execute("Select Name,Rollno from Data")
    r=cur.fetchall()
    for row in r:
        name,rollno=row
        cur.execute("Select 1 from Present_students where Rollno=? And Date=?",(rollno,d))
        val=cur.fetchone()
        if not val:
            cur.execute("Select 1 from Absent_students where Rollno=? And Date=?",(rollno,d))
            var=cur.fetchone()
            if not var:
                cur.execute("Insert into Absent_students (Name , Rollno, Date) Values (?,?,?) ",(name,rollno,d))
                con.commit()


def show_absent():
    speaker.Speak("Say!  The ROLL Number to see Attendance of that student")
    text = record_text()
    n=Validity_check(text)
    if n:
        con=sq.connect("Attendance.db")
        cur=con.cursor()
        cur.execute("Select * from Absent_students where Rollno=?",(n,))
        r=cur.fetchall()
        if r:
            return r
        else:
            speaker.speak(f"Roll number {n} is a Regular Student, No Absents are Marked")
        con.close()


def Validity_check(text):
    r=False
    a=text.split(" ")
    n=None

    for i in a:
        if i.isdigit():
            n=int(i)
            r=True
    if r:
        print("Roll_NO : ", n)
        return n

    if not r:
        try:
            n=w2n.word_to_num(text)
            print("Roll_NO : ", n)
        except ValueError:
            speaker.speak("Please Say Clearly Cannot get your audio ")
            raise Exception("Say a Clear Roll no")
        return n


def database(n):
    con=sq.connect("Attendance.db")
    cur=con.cursor()
    d=datetime.now().strftime("%d-%m-%Y")
    absent_stu()

    cur.execute("Create Table if not Exists Present_students (Rollno int, Name Text, Date Text)")

    cur.execute("Select Rollno,Name from Data where Rollno = ?", (n,))
    student=cur.fetchone()

    if student:
        rollno,name =student
        cur.execute("Select 1 from Present_students where Rollno=? And Date=?", (rollno, d))
        attendance_marked=cur.fetchone()

        if attendance_marked:
            speaker.speak(f"{name} Your attendance is already marked for today.")
        else:
            cur.execute("Insert into Present_students (Rollno, Name, Date) VALUES (?, ?, ?)", (rollno, name, d))
            cur.execute("Delete from Absent_students where Rollno=? And Date=?",(rollno,d))
            con.commit()
            speaker.speak(f"{name} Your attendance is marked successfully.")
    else:
        speaker.speak(f"Roll number {n} is not found in the database. Please try again.")

    con.close()


def Start():
    speaker.Speak("Say! Your ROLL Number to mark Your attendance")    # Anything written in it will be spoken
    text = record_text()
    n=Validity_check(text)
    if n:
        database(n)



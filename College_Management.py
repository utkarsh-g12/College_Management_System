from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import pymysql
from tkcalendar import DateEntry
import re


root = Tk()
root.title("College Management")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("%dx%d" % (screen_width, screen_height))

# ----------------------------------Variable-------------------------------------------
# ----------------------------New Teacher Registration-----------------------
tnameentryv = StringVar()
tfnameentryv = StringVar()
tmnameentryv = StringVar()
tdobentryv = StringVar()
tqualificationentryv = StringVar()
tmobilenumberv = StringVar()
temailidv = StringVar()
# ---------------------------End of  New Teacher Registration Variable----------------------
# ----------------------------Teaher Login Variable---------------------------------------------
tuseridentryv = StringVar()
tpassentryv = StringVar()
# ----------------------------End of Teaher
#  Variable---------------------------------------------
# ---------------------------New Student Entry Variable-------------------------------------
entrancenamev = StringVar(root, value="JEECUP")
totalmarksentryv = StringVar(root, value="600")
obtainmarksentryv = IntVar()
admissiontypeentryv = StringVar()
nameentryv = StringVar()
fnameentryv = StringVar()
mnameentryv = StringVar()
qualificationentryv = StringVar()
mobilenumberv = IntVar()
emailidv = StringVar()
# ---------------------------End of New Student Entry Variable-------------------------------------
# ------------------------------Student Login Variable--------------------------------------
rollentryv = IntVar()
dobloginentryv = StringVar()
# ------------------------------End of Student Login Variable--------------------------------------
# -------------------------------Admin Login Variable-----------------------------------------------
adminidentryv = StringVar()
adminpassentryv = StringVar()
# --------------------------------End of Admin Login Variable----------------------------------------
# --------------------------------End of Variables-------------------------------------------------
# ----------------------------------Mobile Number Checker---------------------------------------


def mobile_checker(p):
    if p.isdigit() and len(p) <= 10 or p == "":
        return True
    return False


callback = root.register(mobile_checker)

# --------------------------------------DataBase Connectivity Code-------------------------------


def dbconfig():
    global mycurosor, con
    con = pymysql.connect(host="localhost", user="root", db="college_management")
    mycurosor = con.cursor()

# ------------------------------------All Widget Removal-----------------------------------------


def removeallwidget():
    for widget in root.winfo_children():
        widget.grid_remove()

# ------------------------------------Main Heading-------------------------------------------------


def mainheading():
    lab = Label(root, text="College Management System", bg="green", font=("Ariel", 40, "bold"), padx=400)
    lab.grid(row=0, column=0, columnspan=10)


def back1():
    removeallwidget()
    student1()

# ---------------------------Student New Registration---------------------------------------


def deleteallvalues():
    admissiontypeentryv.set("")
    obtainmarksentryv.set(0)
    nameentryv.set("")
    fnameentryv.set("")
    mnameentryv.set("")
    qualificationentryv.set("")
    mobilenumberv.set(0)
    addressentry.delete(1.0, END)


def registeredstdata():
    admissiontypeentryva = admissiontypeentryv.get()
    entrancenameva = entrancenamev.get()
    totalmarksentryva = totalmarksentryv.get()
    obtainmarksentryva = obtainmarksentryv.get()
    nameentryva = nameentryv.get()
    fnameentryva = fnameentryv.get()
    mnameentryva = mnameentryv.get()
    dobentryva = dobentry.get()
    qualificationentryva = qualificationentryv.get()
    mobilenumberva = mobilenumberv.get()
    emailidva = emailidv.get()
    addressentryva = addressentry.get(1.0, END)
    x = len(re.findall('[\w@_.A-Za-z0-9]{1,40}@gmail.com', emailidva))
    if admissiontypeentryva == "" or obtainmarksentryva == "" or nameentryva == "" or \
            fnameentryva == "" or mnameentryva == "" or dobentryva == "" or qualificationentryva == "" \
            or mobilenumberva == "" or addressentryva == "":
        messagebox.showerror("ERROR IN FORM", "Please!!!! Fill the required Field.")
        y = messagebox.askokcancel("Please Click Ok or Cancel", "Do You Want To Know The Required Field")
        if y == True:
            messagebox.showinfo("Required List", "All The Fields Are Reqiured")
            deleteallvalues()
        else:
            deleteallvalues()
    elif obtainmarksentryva > 600:
        messagebox.showerror("Obtain Marks Error", "Obtain Marks Not Enough Than Total Marks")
        obtainmarksentryv.set(0)
    elif x == 0:
        messagebox.showerror("Incorect Email", "Only Gmail Account Is Valid")
        emailidv.set("")
    else:
        dbconfig()
        que = "insert into student_detail(Addmission_Type,EntranceExam_Name,Total_Marks,Obtain_Marks," \
            "Name,FatherName,MotherName,DateOfBirth,Qualification,Mobile_Number,Email_ID,Address)" \
            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (admissiontypeentryva, entrancenameva, totalmarksentryva, obtainmarksentryva, nameentryva, fnameentryva, mnameentryva, dobentryva, qualificationentryva, mobilenumberva, emailidva, addressentryva)
        mycurosor.execute(que, val)
        con.commit()
        tofetchdata = "select Roll_No from student_detail;"
        rollnumber = mycurosor.execute(tofetchdata)

        quetologintable = "insert into student_login(Roll_No,DateOfBirth) values(%s,%s);"
        valforlogintable = (rollnumber, dobentryva)
        mycurosor.execute(quetologintable, valforlogintable)
        con.commit()
        messagebox.showinfo("Successfull", "Data Inserted Successfully")
        deleteallvalues()
        emailidv.set("")

# ------------------------ComboBox Selection Event--------------------------------------


def conditional(event):
    a = admissiontypeentryv.get()
    if a == "Entrance":
        lab = Label(root, text="Entrance Exam Name", font=("Ariel", 20))
        lab.grid(row=6, column=3)
        entrancename = Entry(root, textvar=entrancenamev, state="readonly")
        entrancename.grid(row=7, column=3)

        lab1 = Label(root, text="Total Marks", font=("Ariel", 20))
        lab1.grid(row=6, column=4)
        totalmarksentry = Entry(root, textvar=totalmarksentryv, state="readonly")
        totalmarksentry.grid(row=7, column=4)
        lab2 = Label(root, text="Obtain Marks", font=("Ariel", 20))
        lab2.grid(row=6, column=5)
        obtainmarksentry = Entry(root, textvar=obtainmarksentryv)
        obtainmarksentry.grid(row=7, column=5)
        obtainmarksentry.configure(validate="key", validatecommand=(callback, "%P"))
    elif a == "Direct":
        lab = Label(root, text="Entrance Exam Name", font=("Ariel", 20))
        lab.grid(row=6, column=3)
        entrancename = Entry(root, state="readonly")
        entrancename.grid(row=7, column=3)

        lab1 = Label(root, text="Total Marks", font=("Ariel", 20))
        lab1.grid(row=6, column=4)
        totalmarksentry = Entry(root, state="readonly")
        totalmarksentry.grid(row=7, column=4)
        lab2 = Label(root, text="Obtain Marks", font=("Ariel", 20))
        lab2.grid(row=6, column=5)
        obtainmarksentry = Entry(root, state="readonly")
        obtainmarksentry.grid(row=7, column=5)

# --------------------------------Student Registration Form------------------------------------------


def studentregistration():
    removeallwidget()
    mainheading()
    btn = Button(root, text="Back", bd=5, font=("Ariel", 10), command=back1)
    btn.grid(row=3, column=0)
    lab = Label(root, text="New Student Registration", font=("Ariel", 20, "bold"))
    lab.grid(row=4, column=4)
    lab8 = Label(root, text="Admission Type", font=("Ariel", 20))
    lab8.grid(row=5, column=3)
    admissiontypeentry = Combobox(root, values=["Entrance", "Direct"], textvar=admissiontypeentryv, state="readonly")
    admissiontypeentry.grid(row=5, column=5)
    admissiontypeentry.bind("<<ComboboxSelected>>", conditional)
    lab1 = Label(root, text="Full Name", font=("Ariel", 20))
    lab1.grid(row=8, column=3)
    nameentry = Entry(root, textvar=nameentryv, border=10)
    nameentry.grid(row=8, column=5)
    lab2 = Label(root, text="Father's Name", font=("Ariel", 20))
    lab2.grid(row=9, column=3)
    fnameentry = Entry(root, textvar=fnameentryv, border=10)
    fnameentry.grid(row=9, column=5)
    lab3 = Label(root, text="Mother's Name", font=("Ariel", 20))
    lab3.grid(row=10, column=3)
    mnameentry = Entry(root, textvar=mnameentryv, border=10)
    mnameentry.grid(row=10, column=5)
    lab4 = Label(root, text="Date Of Birth", font=("Ariel", 20))
    lab4.grid(row=11, column=3)
    global dobentry
    dobentry = DateEntry(root, background="blue", border=10, date_pattern="YYYY-MM-DD", state="readonly")
    dobentry.grid(row=11, column=5)
    lab5 = Label(root, text="Qualification", font=("Ariel", 20))
    lab5.grid(row=12, column=3)
    qualificationentry = Combobox(root, values=["10th", "12th"], textvar=qualificationentryv, state="readonly")
    qualificationentry.grid(row=12, column=5)
    lab6 = Label(root, text="Mobile Number", font=("Ariel", 20))
    lab6.grid(row=13, column=3)
    mobilenumber = Entry(root, textvar=mobilenumberv)
    mobilenumber.grid(row=13, column=5)
    mobilenumber.configure(validate="key", validatecommand=(callback, "%P"))
    lab7 = Label(root, text="Email ID", font=("Ariel", 20))
    lab7.grid(row=14, column=3)
    emailid = Entry(root, textvar=emailidv)
    emailid.grid(row=14, column=5)
    lab8 = Label(root, text="Address", font=("Ariel", 20))
    lab8.grid(row=15, column=3)
    global addressentry
    addressentry = Text(root, border=10, insertwidth=1, width=50, height=5, wrap=WORD)
    addressentry.grid(row=15, column=5)
    btn1 = Button(root, text="Submit", bd=10, font=("Ariel", 20, "bold"), command=registeredstdata)
    btn1.grid(row=17, column=4)

# -----------------------------End of Student Registration Form--------------------------------------------------


def back():
    removeallwidget()
    homepage()


def backtologinpage():
    removeallwidget()
    student1()


def updatestdata():
    pass

def studentlogin():
    global rollnumber,dob
    rollnumber = rollentryv.get()
    dob = dobloginentry.get()
    if(rollnumber=="" or dob==""):
        messagebox.showerror("Data Filling Error", "Please Fill user Name and Password both")
    else:
        dbconfig()
        que = "select * from student_login where Roll_No=%s and DateOfBirth=%s"
        val = (rollnumber, dob)
        mycurosor.execute(que, val)
        data = mycurosor.fetchall()
        # print(data)

        flag = False
        for row in data:
            flag = True

        con.close()
        if flag == True:
            studentdetail()

        else:
            messagebox.showerror("Invalid User Credential", 'either User Name or Password is incorrect')
            rollentryv.set(0)
            dobloginentryv.set("")

def studentdetail():
    dbconfig()
    que = "select * from student_detail where Roll_No=%s,DateOfBirth=%s"
    val = (rollnumber, dob)
    rawdata = mycurosor.execute(que, val)
    print(rawdata)
    con.close()
    removeallwidget()
    mainheading()

    lab = Label(root, text="Student Details", font=("Ariel", 30))
    lab.grid(row=3, column=4)
    btn2 = Button(root, text="Back", bd=5, command=backtologinpage)
    btn2.grid(row=3, column=1)
    lab8 = Label(root, text="Admission Type", font=("Ariel", 20))
    lab8.grid(row=5, column=3)
    admissiontypeentry = Entry(root, textvar=admissiontypeentryv, state="disabled")
    admissiontypeentry.grid(row=5, column=5)
    lab1 = Label(root, text="Full Name", font=("Ariel", 20))
    lab1.grid(row=8, column=3)
    nameentry = Entry(root, textvar=nameentryv, border=10, state="disabled")
    nameentry.grid(row=8, column=5)
    lab2 = Label(root, text="Father's Name", font=("Ariel", 20))
    lab2.grid(row=9, column=3)
    fnameentry = Entry(root, textvar=fnameentryv, border=10)
    fnameentry.grid(row=9, column=5)
    lab3 = Label(root, text="Mother's Name", font=("Ariel", 20))
    lab3.grid(row=10, column=3)
    mnameentry = Entry(root, textvar=mnameentryv, border=10)
    mnameentry.grid(row=10, column=5)
    lab4 = Label(root, text="Date Of Birth", font=("Ariel", 20))
    lab4.grid(row=11, column=3)
    global dobentry
    dobentry = DateEntry(root, background="blue", border=10, date_pattern="YYYY-MM-DD", state="readonly")
    dobentry.grid(row=11, column=5)
    lab5 = Label(root, text="Qualification", font=("Ariel", 20))
    lab5.grid(row=12, column=3)
    qualificationentry = Entry(root, textvar=qualificationentryv, state="disabled")
    qualificationentry.grid(row=12, column=5)
    lab6 = Label(root, text="Mobile Number", font=("Ariel", 20))
    lab6.grid(row=13, column=3)
    mobilenumber = Entry(root, textvar=mobilenumberv)
    mobilenumber.grid(row=13, column=5)
    mobilenumber.configure(validate="key",validatecommand=(callback,"%P"))
    lab7 = Label(root, text="Email ID", font=("Ariel", 20))
    lab7.grid(row=14, column=3)
    emailid = Entry(root, textvar=emailidv)
    emailid.grid(row=14, column=5)
    lab8 = Label(root, text="Address", font=("Ariel", 20))
    lab8.grid(row=15, column=3)
    global addressentry
    addressentry = Text(root, border=10, insertwidth=1, width=50, height=5, wrap=WORD)
    addressentry.grid(row=15, column=5)
    lab9 = Label(root)
    lab9.grid(row=17, column=4)
    btn1 = Button(root, text="Update Mobile Number and EmailID", bd=10, font=("Ariel", 15, "bold"), command=updatestdata)
    btn1.grid(row=18, column=4)


def student1():
    removeallwidget()
    mainheading()
    lab = Label(root, text="Student LogIn Form", font=("Ariel", 30))
    lab.grid(row=3, column=4)
    btn2 = Button(root, text="Back", bd=5, command=back)
    btn2.grid(row=3, column=1)
    lab1 = Label(root, text="RollNo", font=("Ariel", 20))
    lab1.grid(row=4, column=3)
    lab2 = Label(root, text="Date Of Birth", font=("Ariel", 20))
    lab2.grid(row=5, column=3)
    rollentry = Entry(root, textvar=rollentryv)
    rollentry.grid(row=4, column=5)
    global dobloginentry
    dobloginentry = DateEntry(root, date_pattern="YYYY-MM-DD", state="readonly")
    dobloginentry.grid(row=5, column=5)
    btn = Button(root, text="LogIN", font=("Ariel", 20, "bold"), bd=10, command=studentlogin)
    btn.grid(row=6, column=4)
    btn1 = Button(root, text="New Registration", font=("Ariel", 20, "bold"), bd=10, command=studentregistration)
    btn1.grid(row=7, column=4)


def registertdata():
    tnameentryva = tnameentryv.get()
    tfnameentryva = tfnameentryv.get()
    tmnameentryva = tmnameentryv.get()
    tdobentryva = tdobentry.get()
    tqualificationentryva = tqualificationentryv.get()
    tmobilenumberva = tmobilenumberv.get()
    temailidva = temailidv.get()
    taddressentryva = taddress.get(1.0,END)
    
    x = len(re.findall('[\w@_.A-Za-z0-9]{1,40}@gmail.com', temailidva))
    if tnameentryva == "" or tfnameentryva == "" or tmnameentryva == "" or tdobentryva == "" or tqualificationentryva == "" or tmobilenumberva == "" or taddressentryva == "":
        messagebox.showerror("ERROR IN FORM", "Please!!!! Fill the required Field.")
        y = messagebox.askokcancel("Please Click Ok or Cancel", "Do You Want To Know The Required Field")
        if y == True:
            messagebox.showinfo("Required List", "All The Fields Are Reqiured")
        else:
            tnameentryv.set("")
            tfnameentryv.set("")
            tmnameentryv.set("")
            tqualificationentryv.set("")
            tmobilenumberv.set("")
            taddress.delete(1.0, END)
    if x == 0:
        messagebox.showerror("Incorect Email", "Only Gmail Account Is Valid")
        temailidv.set("")
    else:
        pass


# --------------------------------------------New Teacher Entry----------------------------------------


def newteacherentry():
    removeallwidget()
    mainheading()
    head = Label(root, text="New Teacher Entry", font=("Ariel", 30, "bold"))
    head.grid(row=3, column=4)
    btn = Button(root, text="Back", bd=5, command=institute1)
    btn.grid(row=3, column=1)
    lab = Label(root, text="Full Name", font=("Ariel", 20))
    lab.grid(row=4, column=3)
    tnameentry = Entry(root, textvar=tnameentryv)
    tnameentry.grid(row=4, column=5)
    lab1 = Label(root, text="Father's Name", font=("Ariel", 20))
    lab1.grid(row=5, column=3)
    tfnameentry = Entry(root, textvar=tfnameentryv)
    tfnameentry.grid(row=5, column=5)
    lab2 = Label(root, text="Mother's Name", font=("Ariel", 20))
    lab2.grid(row=6, column=3)
    tmnameentry = Entry(root, textvar=tmnameentryv)
    tmnameentry.grid(row=6, column=5)
    lab3 = Label(root, text="Date Of Birth", font=("Ariel", 20))
    lab3.grid(row=7, column=3)
    global tdobentry
    tdobentry = DateEntry(root, date_pattern="YYYY-MM-DD", state="readonly")
    tdobentry.grid(row=7, column=5)
    lab4 = Label(root, text="Qualification", font=("Ariel", 20))
    lab4.grid(row=8,column=3)
    tqualificationentry = Combobox(root, values=["B.Tech", "M.Tech", "Ph.D"], state="readonly", textvar=tqualificationentryv)
    tqualificationentry.grid(row=8, column=5)
    lab5 = Label(root, text="Mobile Number", font=("Ariel", 20))
    lab5.grid(row=9, column=3)
    tmobilenumberentry = Entry(root, textvar=tmobilenumberv)
    tmobilenumberentry.grid(row=9, column=5)
    tmobilenumberentry.configure(validate="key", validatecommand=(callback, "%P"))
    lab6 = Label(root, text="Email ID", font=("Ariel", 20))
    lab6.grid(row=10, column=3)
    temailid = Entry(root, textvar=temailidv)
    temailid.grid(row=10, column=5)
    lab7 = Label(root, text="Address", font=("Ariel", 20))
    lab7.grid(row=11, column=3)
    global taddress
    taddress = Text(root, width=50, height=5)
    taddress.grid(row=11, column=5)
    btn1 = Button(root, text="Register", bd=10, font=("Ariel", 20, "bold"), command=registertdata)
    btn1.grid(row=13, column=4)


# ------------------------------Home Page Institute Button-----------------------------------------------


def institute1():
    removeallwidget()
    mainheading()
    lab = Label(root, text="Teacher LogIn Form", font=("Ariel", 30))
    lab.grid(row=3, column=4)
    btn = Button(root, text="Back", bd=5, command=homepage)
    btn.grid(row=3, column=1)
    lab1 = Label(root, text="UserId", font=("Ariel", 20))
    lab1.grid(row=4, column=3)
    lab2 = Label(root, text="Password", font=("Ariel", 20))
    lab2.grid(row=5, column=3)
    tuseridentry = Entry(root, textvar=tuseridentryv)
    tuseridentry.grid(row=4, column=5)
    tpassentry = Entry(root, textvar=tpassentryv)
    tpassentry.grid(row=5, column=5)
    btn1 = Button(root, text="LogIN", font=("Ariel", 20, "bold"), bd=10)
    btn1.grid(row=6, column=4)
    btn2 = Button(root, text="New Entry", font=("Ariel", 20, "bold"), bd=10, command=newteacherentry)
    btn2.grid(row=7, column=4)

# -----------------------------------Admin Login---------------------------------------------------------------------


def adminlogin():
    removeallwidget()
    mainheading()
    lab = Label(root, text="Admin Login", font=("Ariel", 30))
    lab.grid(row=3, column=4)
    btn = Button(root, text="Back", bd=5, command=homepage)
    btn.grid(row=3, column=1)
    lab1 = Label(root, text="Admin ID", font=("Ariel", 20))
    lab1.grid(row=4, column=3)
    lab2 = Label(root, text="Password", font=("Ariel", 20))
    lab2.grid(row=5, column=3)
    adminidentry = Entry(root, textvar=adminidentryv)
    adminidentry.grid(row=4, column=5)
    adminpassentry = Entry(root, textvar=adminpassentryv)
    adminpassentry.grid(row=5, column=5)
    btn1 = Button(root, text="LogIN", font=("Ariel", 20, "bold"), bd=10)
    btn1.grid(row=6, column=4)

# ------------------------------------Exit Window--------------------------------------------------------


def Exit_Window():
    exit()
# -------------------------------------Home Page------------------------------------------------------------


def homepage():
    removeallwidget()
    mainheading()
    btn = Button(root, text="Student", font=("Ariel", 20, "bold"), bd=10, command=student1)
    btn.grid(row=1, column=3)
    btn = Button(root, text="Institute", font=("Ariel", 20, "bold"), bd=10, command=institute1)
    btn.grid(row=1, column=5)
    btn = Button(root, text="Admin Login", font=("Ariel", 20, "bold"), bd=10, command=adminlogin)
    btn.grid(row=2, column=4)
    lab = Label(root)
    lab.grid(row=3, column=4)
    lab = Label(root)
    lab.grid(row=4, column=4)
    lab = Label(root)
    lab.grid(row=5, column=4)
    lab = Label(root)
    lab.grid(row=6, column=4)
    lab = Label(root)
    lab.grid(row=7, column=4)
    btn = Button(root, text="Exit", font=("Ariel", 20, "bold"), bd=10, command=Exit_Window)
    btn.grid(row=8, column=4)


mainheading()
homepage()
mainloop()

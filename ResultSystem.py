# NAME = C.DILAKSHI KAUMADI ABEYSINGHE
# AR   = 96301
# AF   = 18 / 14335
# First Year First Semester Project


import tkinter as tk

import SystemDB as backEnd

from tkinter import *

from PIL import ImageTk, Image

# import tkinter.messagebox as MessageBox
# import mysql.connector as mysql
# import self as self


my_Window = Tk().withdraw()


# GLOBAL VARIABLES
email = tk.StringVar()
password = tk.StringVar()

get_ar = tk.IntVar()
sem_tablename = tk.StringVar()
sem_name = tk.StringVar()
sem_gpa = tk.DoubleVar()
sem_credits = tk.IntVar()

sem_sub1code = tk.StringVar()
sem_sub2code = tk.StringVar()
sem_sub3code = tk.StringVar()
sem_sub4code = tk.StringVar()
sem_sub5code = tk.StringVar()

sem_sub1result = tk.StringVar()
sem_sub2result = tk.StringVar()
sem_sub3result = tk.StringVar()
sem_sub4result = tk.StringVar()
sem_sub5result = tk.StringVar()

final_gpa = tk.DoubleVar()
final_class = tk.StringVar()
final_credits = tk.IntVar()


# Window 1

class FirstPage(tk.Frame):
    # global a_label, my_image, my_button
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")

        self.a_label = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue", font="Algerian 30 bold")
        self.a_label.place(x=250, y=150)

        # Add Button
        self.my_button = tk.Button(self, text="Lets Go..!", background="brown",
                                   command=lambda: controller.show_frame(SecondPage))
        self.my_button.place(x=400, y=500)


# Window 2

class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        global email, password

        tk.Frame.__init__(self, parent, background="#95eddf")

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue", font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="#c9d4d1", text="WELCOME TO THE ERS..!", fg="maroon", font="Arial 16 bold")
        self.a_label2.place(x=329, y=200)

        self.a_label3 = tk.Label(self, background="#e8dd3f", text="EMAIL ADDRESS", fg="black", font="Arial 12 bold")
        self.a_label3.place(x=300, y=350)

        self.a_label4 = tk.Label(self, background="#e8dd3f", text="PASSWORD", fg="black", font="Arial 12 bold")
        self.a_label4.place(x=300, y=450)

        self.label = tk.Label(self)

        mail = tk.StringVar()
        pw = tk.StringVar()

        # Add Text Box
        self.mailentry = tk.Entry(self, width=20, textvariable=mail)
        self.mailentry.place(x=500, y=350)
        # e.insert(0, "Enter Your Email")

        # Add Entry Box
        self.pwentry = tk.Entry(self, width=20, textvariable=pw, show="*")
        self.pwentry.place(x=500, y=450)
        # self.e.insert(0, "Enter Your Password")

        # Add Button
        self.my_button = tk.Button(self, text="Log In", background="brown", command=lambda: login())
        self.my_button.place(x=400, y=550)

        self.my_button = tk.Button(self, text="Sign Up", background="brown", command=lambda: controller.show_frame(ThirdPage))
        self.my_button.place(x=395, y=600)

        def login():
            m = self.mailentry.get()
            p = self.pwentry.get()

            success = backEnd.login(m, p)
            if (success==1):
                email.set(m)
                password.set(p)
                # mail.set("")
                # pw.set("")
                controller.show_frame(ForthPage)
            else:
                self.label['text'] = "email or password is incorrect! Please try again"
                self.label.place(x=300, y=500)

# Window 3


class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        global email, password

        tk.Frame.__init__(self, parent, background="#95eddf")

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="#c9d4d1", text="Sign Up For Your Account", fg="maroon",
                                 font="Arial 16 bold")
        self.a_label2.place(x=329, y=200)

        self.a_label3 = tk.Label(self, background="#e8dd3f", text="EMAIL ADDRESS", fg="black", font="Arial 10 bold")
        self.a_label3.place(x=300, y=300)

        self.a_label4 = tk.Label(self, background="#e8dd3f", text="USER NAME", fg="black", font="Arial 10 bold")
        self.a_label4.place(x=300, y=400)

        self.a_label3 = tk.Label(self, background="#e8dd3f", text="PASSWORD", fg="black", font="Arial 10 bold")
        self.a_label3.place(x=300, y=500)

        mail = tk.StringVar()
        name = tk.StringVar()
        pswd = tk.StringVar()

        self.emailentry = tk.Entry(self, width=20, textvariable=mail)
        self.emailentry.place(x=500, y=300)
        # self.e.insert(0, "Enter Your Email")

        self.nameentry = tk.Entry(self, width=20, textvariable=name)
        self.nameentry.place(x=500, y=400)
        # self.e.insert(0, "Enter Your User Name")

        self.pswdentry = tk.Entry(self, width=20, textvariable=pswd, show="*")
        self.pswdentry.place(x=500, y=500)
        # self.e.insert(0, "Enter Your Password")

        self.label = tk.Label(self)

        self.my_button = tk.Button(self, text="Sign Up", background="brown", command=lambda: signup())
        self.my_button.place(x=700, y=625)

        self.back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(ForthPage))
        self.back_button.place(x=650, y=600)

        def signup():
            mail1 = self.emailentry.get()
            name1 = self.nameentry.get()
            pswd1 = self.pswdentry.get()
            success = backEnd.signup(mail1, name1, pswd1)
            if success==1:
                email.set(mail.get())
                controller.show_frame(ForthPage)
            else:
                self.label['text'] = "Could not signup. Please check details again"
                self.label.place(x=500,y=650)


# Window 4

class ForthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label1 = tk.Label(self, background="#e8dd3f", text="RESULT", fg="black", font="Arial 10 bold")
        self.a_label1.place(x=300, y=400)

        option = [
            "Student Individual Result",
            "Overall Result"
        ]

        self.clicked = tk.StringVar()
        self.clicked.set(option[0])

        self.drop = tk.OptionMenu(self, self.clicked, *option)
        self.drop.place(x=400, y=400)

        def selectPage(val):

            if (val == "Student Individual Result"):
                selectedpage = FifthPage
            else:
                selectedpage = TwelvethPage

            return selectedpage

        page = self.clicked.get()

        z = selectPage(page)

        self.my_button = Button(self, text="View", command=lambda: controller.show_frame(selectPage(self.clicked.get())))
        self.my_button.place(x=600, y=400)

        # self.back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(ForthPage))
        # self.back_button.place(x=650, y=600)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)


# Window 5


class FifthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")
        global get_ar

        # Add Label
        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="STUDENT INDIVIDUAL RESULT", fg="maroon",
                                 font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        self.a_label3 = tk.Label(self, background="#e8dd3f", text="STUDENT AR NUMBER", fg="black", font="Arial 10 bold")
        self.a_label3.place(x=300, y=400)

        # global get_ar
        x_var = tk.IntVar()

        self.arentry = tk.Entry(self, width=20, textvariable=x_var)
        self.arentry.place(x=500, y=400)
        # # e.insert(0, "")

        self.view_button = tk.Button(self, text="View", command=lambda: passValue(SixthPage))
        self.view_button.place(x=450, y=500)

        self.back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(ForthPage))
        self.back_button.place(x=500, y=500)

        self.logout_button = tk.Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.logout_button.place(x=750, y=50)

        def passValue(page):
            val = self.arentry.get()
            get_ar.set(val)
            controller.show_frame(page)


# Window 6

class SixthPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")
        global get_ar, sem_gpa, sem_name, sem_credits, sem_sub1code, sem_sub1result, \
            sem_sub2code, sem_sub2result, sem_sub3code, sem_sub3result, sem_sub4code, \
            sem_sub4result, sem_sub5code, \
            sem_sub5result, final_class, final_credits, final_gpa

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="#c9d4d1", text="STUDENT INDIVIDUAL RESULT", fg="maroon",
                                 font="Arial 12 bold")
        self.a_label2.place(x=335, y=200)

        self.a_label1 = tk.Label(self, background="#e8dd3f", text="SEMESTER RESULT", fg="black", font="Arial 10 bold")
        self.a_label1.place(x=290, y=300)

        option = [
            "1ST YEAR 1ST SEMESTER",
            "1ST YEAR 2ND SEMESTER",
            "2ND YEAR 1ST SEMESTER",
            "2ND YEAR 2ND SEMESTER",
        ]

        clicked = tk.StringVar()
        clicked.set(option[0])

        self.drop = tk.OptionMenu(self, clicked, *option)
        self.drop.place(x=450, y=300)

        self.my_button = Button(self, text="View", command=lambda: showSemResults())
        self.my_button.place(x=650, y=300)

        self.a_label2 = tk.Label(self, background="#e8dd3f", text="FINAL RESULT", fg="black", font="Arial 10 bold")
        self.a_label2.place(x=290, y=450)

        self.my_button = Button(self, text="View", command=lambda: showFinalResults())
        self.my_button.place(x=650, y=450)

        self.back_button = tk.Button(self, text="Back", command=lambda: controller.show_frame(FifthPage))
        self.back_button.place(x=750, y=500)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        def showSemResults():
            optVal = clicked.get()
            ar = get_ar.get()
            sem_name.set(optVal)

            if (optVal == "1ST YEAR 1ST SEMESTER"):
                calcSem(ar, "yr1_sem1_table")

            elif (optVal == "1ST YEAR 2ND SEMESTER"):
                calcSem(ar, "yr1_sem2_table")

            elif (optVal == "2ND YEAR 1ST SEMESTER"):
                calcSem(ar, "yr2_sem1_table")

            elif (optVal == "2ND YEAR 2ND SEMESTER"):
                calcSem(ar, "yr2_sem2_table")

        def calcSem(ar_num, table_name):
            val = backEnd.calcGpa(ar_num, table_name)
            sem_gpa.set(val)
            val1 = backEnd.total_sem_credits
            sem_credits.set(val1)
            results = backEnd.sem_results

            sem_sub1code.set(results[0][0])
            sem_sub2code.set(results[1][0])
            sem_sub3code.set(results[2][0])
            sem_sub4code.set(results[3][0])
            sem_sub5code.set(results[4][0])

            sem_sub1result.set(results[0][1])
            sem_sub2result.set(results[1][1])
            sem_sub3result.set(results[2][1])
            sem_sub4result.set(results[3][1])
            sem_sub5result.set(results[4][1])

            controller.show_frame(SeventhPage)

        def showFinalResults():
            ar = get_ar.get()

            val = backEnd.getOneFinalGpa(ar)
            final_gpa.set(val)

            val1 = backEnd.getOneFinalCredits(ar)
            final_credits.set(val1)

            val2 = backEnd.getOneClass(ar)
            final_class.set(val2)

            controller.show_frame(EleventhPage)


# Window 7

class SeventhPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")
        global sem_gpa, sem_name, sem_credits, sem_sub1code, sem_sub1result, \
            sem_sub2code, sem_sub2result, sem_sub3code, sem_sub3result, sem_sub4code, sem_sub4result, sem_sub5code, sem_sub5result

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="Semester Name", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        self.a_lbl1 = tk.Label(self, text="Sub 1 Code")
        self.a_lbl1.place(x=350, y=300)

        self.a_lbl1a = tk.Label(self, text="Sub 1 Grade")
        self.a_lbl1a.place(x=500, y=300)

        self.a_lbl2 = tk.Label(self, text="Sub 2 Code")
        self.a_lbl2.place(x=350, y=350)

        self.a_lbl2a = tk.Label(self, text="Sub 2 Grade")
        self.a_lbl2a.place(x=500, y=350)

        self.a_lbl3 = tk.Label(self, text="Sub 3 Code")
        self.a_lbl3.place(x=350, y=400)

        self.a_lbl3a = tk.Label(self, text="Sub 3 Grade")
        self.a_lbl3a.place(x=500, y=400)

        self.a_lbl4 = tk.Label(self, text="Sub 4 Code")
        self.a_lbl4.place(x=350, y=450)

        self.a_lbl4a = tk.Label(self, text="Sub 4 Grade")
        self.a_lbl4a.place(x=500, y=450)

        self.a_lbl5 = tk.Label(self, text="Sub 5 Code")
        self.a_lbl5.place(x=350, y=500)

        self.a_lbl5a = tk.Label(self, text="Sub 5 Grade")
        self.a_lbl5a.place(x=500, y=500)

        self.my_button = tk.Button(self, text="Click here to see results!", background="red", command=lambda: refresh())
        self.my_button.place(x=250, y=600)

        self.a_lab1 = tk.Label(self, text="Semester GPA")
        self.a_lab1.place(x=250, y=550)

        self.a_lab1a = tk.Label(self, background="white", text="GPA", fg="black", font="Arial 10 bold")
        self.a_lab1a.place(x=250, y=570)

        self.a_lab2 = tk.Label(self, text="Semester Credits")
        self.a_lab2.place(x=450, y=550)

        self.a_lab2a = tk.Label(self, background="white", text="No. of Credits", fg="black", font="Arial 10 bold")
        self.a_lab2a.place(x=450, y=570)

        self.my_button = tk.Button(self, text="CLOSE", command=lambda: close())
        self.my_button.place(x=750, y=500)

        self.my_button = tk.Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        def refresh():
            self.a_lab1['text'] = sem_gpa.get()
            self.a_label2['text'] = sem_name.get()
            self.a_lab2['text'] = sem_credits.get()

            self.a_lbl1['text'] = sem_sub1code.get()
            self.a_lbl2['text'] = sem_sub2code.get()
            self.a_lbl3['text'] = sem_sub3code.get()
            self.a_lbl4['text'] = sem_sub4code.get()
            self.a_lbl5['text'] = sem_sub5code.get()

            self.a_lbl1a['text'] = sem_sub1result.get()
            self.a_lbl2a['text'] = sem_sub2result.get()
            self.a_lbl3a['text'] = sem_sub3result.get()
            self.a_lbl4a['text'] = sem_sub4result.get()
            self.a_lbl5a['text'] = sem_sub5result.get()

            for item in (self.a_lbl1, self.a_lbl2, self.a_lbl3, self.a_lbl4, self.a_lbl4, self.a_lab1, self.a_lab2):
                item['background'] = "white"
                item['fg'] = "black"
                item['font'] = "Arial 10 bold"

        def close():
            self.a_lab1['text'] = "Semester GPA"
            self.a_label2['text'] = "Semester Name"
            self.a_lab2['text'] = "Semester Credits"

            self.a_lbl1['text'] = "Sub 1 Code"
            self.a_lbl2['text'] = "Sub 2 Code"
            self.a_lbl3['text'] = "Sub 3 Code"
            self.a_lbl4['text'] = "Sub 4 Code"
            self.a_lbl5['text'] = "Sub 5 Code"

            self.a_lbl1a['text'] = "Sub 1 Grade"
            self.a_lbl2a['text'] = "Sub 2 Grade"
            self.a_lbl3a['text'] = "Sub 3 Grade"
            self.a_lbl4a['text'] = "Sub 4 Grade"
            self.a_lbl5a['text'] = "Sub 5 Grade"

            controller.show_frame(SixthPage)


# Window 11

class EleventhPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")
        global get_ar, final_class, final_credits, final_gpa

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="FINAL RESULT", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=400, y=200)

        self.a_lbl1 = tk.Label(self, background="white", text="GPA", fg="black", font="Arial 12 bold")
        self.a_lbl1.place(x=200, y=300)

        self.a_lbl1 = tk.Label(self, background="white", text="Final GPA", fg="black", font="Arial 12 bold")
        self.a_lbl1.place(x=200, y=400)

        self.a_lbl2 = tk.Label(self, background="white", text="TOTAL CREDITS", fg="black", font="Arial 12 bold")
        self.a_lbl2.place(x=400, y=300)

        self.a_lbl2 = tk.Label(self, background="white", text="Final Credits", fg="black", font="Arial 12 bold")
        self.a_lbl2.place(x=400, y=400)

        self.a_lbl3 = tk.Label(self, background="white", text="CLASS", fg="black", font="Arial 12 bold")
        self.a_lbl3.place(x=600, y=300)

        self.a_lbl3 = tk.Label(self, background="white", text="Final Class", fg="black", font="Arial 12 bold")
        self.a_lbl3.place(x=600, y=400)

        self.my_button = tk.Button(self, text="Click here to see results!",  background="red", command=lambda: refresh())
        self.my_button.place(x=250, y=250)

        self.my_button = Button(self, text="CLOSE", command=lambda: close())
        self.my_button.place(x=750, y=500)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        def refresh():
            self.a_lbl1['text'] = final_gpa.get()
            self.a_lbl2['text'] = final_credits.get()
            self.a_lbl3['text'] = final_class.get()

        def close():
            self.a_lbl1['text'] = "Final GPA"
            self.a_lbl2['text'] = "Final Credits"
            self.a_lbl3['text'] = "Final Class"

            controller.show_frame(SixthPage)


# Window 12

class TwelvethPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="#c9d4d1", text="OVERALL RESULT", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=400, y=200)

        self.a_label1 = tk.Label(self, background="white", text="GPA DISTRIBUTION", fg="black", font="Arial 10 bold")
        self.a_label1.place(x=290, y=400)

        self.my_button = Button(self, text="View", command=lambda: gpa_distribution())
        self.my_button.place(x=600, y=400)

        self.a_label2 = tk.Label(self, background="white", text="CLASS DISTRIBUTION", fg="black", font="Arial 10 bold")
        self.a_label2.place(x=290, y=500)

        self.my_button = Button(self, text="View", command=lambda: class_distribution())
        self.my_button.place(x=600, y=500)

        self.a_label3 = tk.Label(self, background="white", text="SUBJECT ANALYSIS", fg="black", font="Arial 10 bold")
        self.a_label3.place(x=290, y=600)

        option = [
            "1001",
            "1002",
            "1003",
            "1004",
            "1005"
        ]

        clicked = tk.StringVar()
        clicked.set(option[0])

        self.drop = tk.OptionMenu(self, clicked, *option)
        self.drop.place(x=500, y=600)

        self.my_button = Button(self, text="View", command=lambda: controller.show_frame(FifteenthPage))
        self.my_button.place(x=600, y=600)

        self.a_label4 = tk.Label(self, background="white", text="OVERALL RANKING SUMMARY", fg="black", font="Arial 10 bold")
        self.a_label4.place(x=290, y=700)

        self.my_button = Button(self, text="View", command=lambda: controller.show_frame(FifteenthPage))
        self.my_button.place(x=600, y=700)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(SixthPage))
        self.my_button.place(x=750, y=500)

        def gpa_distribution():
            controller.show_frame(ThirteenthPage)

        def class_distribution():
            controller.show_frame(FourteenthPage)


# Window 13

class ThirteenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="GPA DISTRIBUTION", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=400, y=200)

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=500)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)


# Window 14

class FourteenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="CLASS DISTRIBUTION", fg="maroon", font="Arial 12 bold")
        self.a_label2.place(x=400, y=200)

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=500)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)


# Window 15

class FifteenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="SUBJECT ANALYSIS - Sub 1", fg="maroon",
                                 font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=500)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(SixteenthPage))
        self.my_button.place(x=750, y=50)


# Window 16

class SixteenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="SUBJECT ANALYSIS - Sub 2", fg="maroon",
                                 font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=500)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)


# Window 17

class SeventeenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="SUBJECT ANALYSIS - Sub 3", fg="maroon",
                                 font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=500)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)


# Window 18

class EighteenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="SUBJECT ANALYSIS - Sub 4", fg="maroon",
                                 font="Arial 12 bold")
        self.a_label2.place(x=350, y=200)

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=500)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)


# Window 19

class NineteenthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#95eddf")

        self.a_label1 = tk.Label(self, background="#c9d4d1", text="EXAM RESULT SYSTEM", fg="darkblue",
                                 font="Arial 20 bold")
        self.a_label1.place(x=300, y=100)

        self.a_label2 = tk.Label(self, background="white", text="OVERALL RANKING SUMMARY", fg="maroon",
                                 font="Arial 12 bold")
        self.a_label2.place(x=335, y=200)

        self.my_button = Button(self, text="CLOSE", command=lambda: controller.show_frame(ThirteenthPage))
        self.my_button.place(x=750, y=500)

        self.my_button = Button(self, text="Log Out", command=lambda: controller.show_frame(FirstPage))
        self.my_button.place(x=750, y=50)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        # my_window = tk.Tk()
        my_window = tk.Frame(self)
        my_window.pack()

        my_window.grid_rowconfigure(0, minsize=700)
        my_window.grid_columnconfigure(0, minsize=900)
        my_window.configure(background="white")

        self.frames = {}

        for F in (FirstPage, SecondPage, ThirdPage, ForthPage, FifthPage, SixthPage, SeventhPage, EleventhPage,
                  TwelvethPage, ThirteenthPage, FourteenthPage, FifteenthPage, SixteenthPage, SeventeenthPage,
                  EighteenthPage, NineteenthPage):
            frame = F(my_window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()
app.mainloop()

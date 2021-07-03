from tkinter import*

# import mysql.connector as mysql
import itertools

# Check the database connection
# import FROM as FROM
# import FROM as FROM
# import INNER as INNER
# import JOIN as JOIN
import mysql.connector
import sql as sql
from mysql.connector import Error

# Exception handling
try:
    conn=mysql.connector.connect(host='localhost', user='root', password='')
    if conn.is_connected():
        print("Successfully Connected")
except Error as e:
    print("Oopss..!")
    print(e)

# open database connection
conDict = {'host': 'localhost', 'database': 'db 1', 'user': 'root', 'password': ''}

db = mysql.connector.connect(**conDict)

# Prepare a cursor object using cursor() method.
cursor = db.cursor()

total_sem_credits = 0
sem_results = []
final_credits = 0

get_ar = 0
final_gpalist= []
final_classlist = []
final_creditlist = []
ar_list = []
value = []


def login(mail, pswd):
    # print(mail, " ", pswd)
    cursor.execute(f"SELECT password FROM usertable WHERE email='{mail}'")
    pw = cursor.fetchall()
    #print(pw)
    if (pw[0][0] == pswd):
        return 1
    else:
        return 0


def signup(mail, name, pswd):
    if(mail!=""):
        cursor.execute(f"INSERT INTO usertable VALUES ('{name}','{mail}','{pswd}')")
        db.commit()

    if login(mail, pswd) == 1:
        return 1
    else:
        return 0
    # print(s)


def calcGpa(reg, table_name):

    global total_sem_credits, sem_results

    l1 = []

    cursor.execute(f"SELECT sem.result, crt.credits, sem.sub_code FROM {table_name} as sem INNER JOIN credit_table as crt ON sem.sub_code = crt.sub_code WHERE sem.stu_ar = {reg}")
    # Fetch results using fetchall() method.
    data = cursor.fetchall()

    sem_results = []
    for item in data:
        l1 = (item[2], item[0])
        sem_results.append(l1)

    # calculate GPA
    gpa = 0.00
    tot = 0
    tot_credit = 0

    for item in data:
        gpv = 0.00
        # print(item)
        if item[0] == "A+":
            gpv = 4.00
        elif item[0] == "A":
            gpv = 4.00
        elif item[0] == "A-":
            gpv = 3.70
        elif item[0] == "B+":
            gpv = 3.30
        elif item[0] == "B":
            gpv = 3.00
        elif item[0] == "B-":
            gpv = 2.70
        elif item[0] == "C+":
            gpv = 2.30
        elif item[0] == "C":
            gpv = 2.00
        elif item[0] == "C-":
            gpv = 1.70
        elif item[0] == "D+":
            gpv = 1.30
        elif item[0] == "D":
            gpv = 1.00
        elif item[0] == "E":
            gpv = 0.00

        tot = gpv * item[1] + tot
        tot_credit = item[1] + tot_credit

    gpa = (tot / tot_credit)
    gpa = round(gpa, 4)
    total_sem_credits = tot_credit
    return gpa


def calcSemGPA(sem):
    sem_gpalist = []

    cursor.execute(f"SELECT DISTINCT stu_ar FROM {sem}")

    ar = cursor.fetchall()
    # print(ar)
    for item in ar:
        g_list = calcGpa(item[0], sem)
        sem_gpalist.append(g_list)
    #print(sem_gpalist)


def calcFinalgpa(reg):
    global final_credits

    final_tot = 0.0
    final_totcredit = 0
    final_gpa = 0.0

    for i in ("yr1_sem1_table", "yr1_sem2_table", "yr2_sem1_table", "yr2_sem2_table"):

        table_name = i
        cursor.execute(f"SELECT sem.result, crt.credits FROM {table_name} as sem INNER JOIN credit_table as crt ON sem.sub_code = crt.sub_code WHERE sem.stu_ar = {reg}")
        # Fetch results using fetchall() method.
        data = cursor.fetchall()

        # calculate GPA
        tot = 0
        tot_credit = 0

        for item in data:
            gpv = 0.00
            # print(item)
            if item[0] == "A+":
                gpv = 4.00
            elif item[0] == "A":
                gpv = 4.00
            elif item[0] == "A-":
                gpv = 3.70
            elif item[0] == "B+":
                gpv = 3.30
            elif item[0] == "B":
                gpv = 3.00
            elif item[0] == "B-":
                gpv = 2.70
            elif item[0] == "C+":
                gpv = 2.30
            elif item[0] == "C":
                gpv = 2.00
            elif item[0] == "C-":
                gpv = 1.70
            elif item[0] == "D+":
                gpv = 1.30
            elif item[0] == "D":
                gpv = 1.00
            elif item[0] == "E":
                gpv = 0.00

            tot = gpv * item[1] + tot
            tot_credit = item[1] + tot_credit

        final_tot = final_tot + tot
        final_totcredit = final_totcredit + tot_credit

    final_credits = final_totcredit
    final_gpa = (final_tot / final_totcredit)
    final_gpa = round(final_gpa, 4)
    return final_gpa


def calcClass(gpa):
    # global final_class
    if 4.00 >= gpa >= 3.70:
        final_class = "First Class "
    elif 3.70 > gpa >= 3.30:
        final_class = "Second Upper Class"
    elif 3.30 > gpa >= 3.00:
        final_class = "Second Lower Class"
    elif 3.00 > gpa >= 2.00:
        final_class = "General Degree"
    elif 2.00 > gpa >= 0.00:
        final_class = "No Degree Awarded"

    return final_class;


def calcFinalResults():

    sem = "yr1_sem1_table"
    cursor.execute(f"SELECT DISTINCT stu_ar FROM {sem}")
    ar_list = cursor.fetchall()

    for item in ar_list:
        one_gpa = calcFinalgpa(item[0])
        final_gpalist.append(one_gpa)
        one_class = calcClass(one_gpa)
        final_classlist.append(one_class)
        final_creditlist.append(final_credits)

    for (i, x, y, z) in zip(ar_list, final_gpalist, final_classlist, final_creditlist):
        tup = (i[0], x, y, z)
        value.append(tup)


def StoreFinalResults():

    sql1 = "DELETE FROM final_gpatable"
    cursor.execute(sql1)
    db.commit()

    sql2 = "INSERT INTO final_gpatable(stu_ar, final_gpa, final_class, final_credits) VALUES (%s, %s, %s, %s)"
    cursor.executemany(sql2, value)
    db.commit()


def getOneClass(reg):
    cursor.execute(f"SELECT final_class FROM final_gpatable WHERE stu_ar = {reg}")
    stu_class = cursor.fetchall()
    stu_class = stu_class[0][0]
    return stu_class


def getOneFinalGpa(reg):
    cursor.execute(f"SELECT final_gpa FROM final_gpatable WHERE stu_ar = {reg}")
    stu_gpa = cursor.fetchall()
    stu_gpa = stu_gpa[0][0]
    return stu_gpa


def getOneFinalCredits(reg):
    cursor.execute(f"SELECT final_credits FROM final_gpatable WHERE stu_ar = {reg}")
    stu_credits = cursor.fetchall()
    stu_credits = stu_credits[0][0]
    return stu_credits



calcFinalResults()
StoreFinalResults()



def logout():
    db.close()

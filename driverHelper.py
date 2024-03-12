import os
import subprocess
import numpy as np
import pandas as pd
import report_page as rp
import dbHandler as DbHandler
from pyswip  import Prolog





reportPageLink = r"report_page.bat"
reportPage = rp.ReportPage()
reportYear = 0
reportGpa = 0
showReport = 0
studentIdList = []
reportData = ""
database = DbHandler.MySqlConnector("student_staff", "root", "")


 




def generateReport(rg, ry):
    
    global reportGpa
    global reportYear
    global reportPage
    global studentIdList
    global showReport

    reportGpa = rg
    reportYear = ry

 
    #returns list of student IDs
    try:
        studentIdList = database.queryDb("SELECT DISTINCT student_master.studentId " +
                                        "FROM student_master " +
                                        "INNER JOIN module_details ON student_master.studentId = module_details.studentId " +
                                        "WHERE module_details.year = " + reportYear + ";")
    except Exception as e:
        print("could not extract student IDs from db\n", e)
  

    #get report data by querying db and prolog kb
    createReportData()

    reportPage.setreportGpa(reportGpa)
    reportPage.setReportYear(reportYear)
    reportPage.setreportData(reportData)
    reportPage.constructHtml()

    try: #save html report
        file = open("reportPageIndex.html", "w") 
        file.write(reportPage.getHtmlPage()) 
        file.close()
    except Exception as e:
        print("Could not open/save report html successfully\n", e)

    try:
        subprocess.call([reportPageLink]) #open report
    except Exception as e:
        print("could not open report\n", e)




    


    




def createReportData():
    global reportData 
    global reportGpa

    reportData = "ID, Student Name, GPA semester 1, GPA semester 2, Cumulative GPA*"
    studentInfo = []
    studentGpaResults = []
    
    for studentId in studentIdList:
        #returns list of stdent modules, grades, etc

        try:
            studentInfo = database.queryDb("SELECT student_master.studentId, student_master.student_Name, module_master.no_of_credits, module_details.semester, module_details.grade_points " +
                            "FROM student_master " +
                            "INNER JOIN module_details ON student_master.studentId = module_details.studentId "+
                            "INNER JOIN module_master ON module_details.moduleId = module_master.moduleId " +
                            "WHERE student_master.studentId =  " + studentId + ";")
        except Exception as e:
            print("could not extract student records\n", e)
        
        studentGpaResults = calculateGpa(studentInfo)
   
        if studentGpaResults[2] <= float(reportGpa): #if cumulative gpa is less than or equal to user entered gpa
            #appends completed student record to global list the * is added at the end as a delimiter for creating table
            reportData = reportData + studentId + "," + studentInfo[1][1] + "," + str(studentGpaResults[0]) + "," + str(studentGpaResults[1]) + "," + str(studentGpaResults[2]) + "*"
    

    

        


def calculateGpa(studentInfo):

    prolog = Prolog()
    prolog.consult("gpa_calculator.pl")
    studentGpaResults = []
    sem1CreditList = []
    sem1GradePointsList = []
    sem2CreditList = []
    sem2GradePointsList = []
    sem1Gpa = 0
    sem2Gpa = 0
    sem1TotalCredits = 0
    sem2TotalCredits = 0
    cumGpa = 0


    try: 
        # calculate grade points for each module 
        for record in studentInfo:
            if record[3] == "1": 
                sem1CreditList.append(record[2])
                for x in prolog.query(f"gradePoint({record[4]},{record[2]}, Gpa)"):
                    sem1GradePointsList.append(round(x["Gpa"], 2))
    
            if record[3] == "2":
                sem2CreditList.append(record[2])
                for x in prolog.query(f"gradePoint({record[4]},{record[2]}, Gpa)"):
                    sem2GradePointsList.append(round(x["Gpa"], 2))
    except Exception as e:
        print("could not calculate grade points\n", e)


    #cconverts gpa and credit arrays to string
    tempSem1GpaList = ",".join(str(v) for v in sem1GradePointsList)
    tempSem1CreditList = ",".join(str(v) for v in sem1CreditList)
    tempSem2GpaList = ",".join(str(v) for v in sem2GradePointsList)
    tempSem2CreditList = ",".join(str(v) for v in sem2CreditList)


    try:
        #calculate semester 1 & 2 gpa 
        if len(sem1GradePointsList) != 0 and len(sem1CreditList) != 0: #prevents divide by 0 error
            for x in prolog.query(f"calGpa([{tempSem1GpaList}], [{tempSem1CreditList}], Gpa)"):
                sem1Gpa = round(x["Gpa"], 2)
        else:
            sem1Gpa = 0

        if len(sem2GradePointsList) != 0 and len(sem2CreditList) != 0:
            for x in prolog.query(f"calGpa([{tempSem2GpaList}], [{tempSem2CreditList}], Gpa)"):
                sem2Gpa = round(x["Gpa"], 2)
        else:
            sem2Gpa = 0
    except Exception as e:
        print("could not calculate GPAs\n", e)


    try:
        #calculate cumulative gpa
        if len(sem1CreditList) != 0: #prevents null error
            for x in prolog.query(f"sum([{tempSem1CreditList}], TotalCredits)"):
                sem1TotalCredits = round(x["TotalCredits"], 2)
        else:
            sem1TotalCredits = 0

        if len(sem2CreditList) != 0: #prevents null error       
            for x in prolog.query(f"sum([{tempSem2CreditList}], TotalCredits)"):
                sem2TotalCredits = round(x["TotalCredits"], 2)
        else:
            sem2TotalCredits = 0
            
        if len(sem1GradePointsList) != 0 and len(sem2GradePointsList) != 0: #sem1 and sem 2 GPA availible
            for x in prolog.query(f"cumulative([{tempSem1GpaList}],[{tempSem2GpaList}],{sem1TotalCredits},{sem2TotalCredits}, CumulativeGpa)"):
                cumGpa = round(x["CumulativeGpa"], 2)

            studentGpaResults.append(sem1Gpa)
            studentGpaResults.append(sem2Gpa)
            studentGpaResults.append(cumGpa)

            return studentGpaResults
        
        if len(sem1GradePointsList) != 0 and len(sem2GradePointsList) == 0: #only sem1 GPA availible
            cumGpa = sem1Gpa

            studentGpaResults.append(sem1Gpa)
            studentGpaResults.append(sem2Gpa)
            studentGpaResults.append(cumGpa)

            return studentGpaResults
        
        if len(sem1GradePointsList) == 0 and len(sem2GradePointsList) != 0: #only sem 2 GPA availible
            cumGpa = sem2Gpa

            studentGpaResults.append(sem1Gpa)
            studentGpaResults.append(sem2Gpa)
            studentGpaResults.append(cumGpa)

            return studentGpaResults
    
        if len(sem1GradePointsList) == 0 and len(sem2GradePointsList) == 0: #sem1 and sem 2 GPA Not availible
            return [0,0,0]

    except Exception as e:
        print("could not calculate cumulative GPA\n", e)

    
    
    
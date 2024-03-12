import threading
import time
import dbHandler as DbHandler
import driverHelper as DriverHelper
import smtplib 
from email.mime.text import MIMEText


run = 1


class EmailService(threading.Thread):

    database = DbHandler.MySqlConnector("student_staff", "root", "")
    senderEmail = "utechacademicprobationaltert@gmail.com"
    senderEmailPassword = "utech@cademicProbationAlert10"
    senderEmailAppPassword = "bcuaxtzkvkbwnyda"
    probationIdList = []
    studentStaffInfoList = []


    def __init__(self):
        threading.Thread.__init__(self)

    
    
    def run(self):
        while(run == True):
            #re-initialize lists
            self.probationIdList = []
            self.studentStaffInfoList = []

            self.generateProbationListing() #creates a list of student IDs that met probation criteria
            self.generateStudentStaffInfoList() #creates a list of student and staff info for each ID identified

            for record in self.studentStaffInfoList:
                print("\n\nID " + record[0] + " flagged for probation")
                try:
                    self.sendEmail(record[2], self.getStudentMessage(record))
                    self.sendEmail(record[6], self.getAdvisorMessage(record))
                    self.sendEmail(record[8], self.getPdMessage(record))
                    self.sendEmail(record[10], self.getFacultyAdminMessage(record))
                except Exception as e:
                    print("error sending email")

            time.sleep(3600) #call




    


    def generateProbationListing(self):

        try:
            studentIdList = self.database.queryDb("SELECT DISTINCT student_master.studentId " +
                                                  "FROM student_master;")
        except Exception as e:
            print("could not extract student IDs from db\n", e)
    

        i = 0 #tracks student index
        for studentId in studentIdList: #querries db for each student
            try:
                studentInfo = self.database.queryDb("SELECT student_master.studentId, student_master.student_Name, module_master.no_of_credits, module_details.semester, module_details.grade_points " +
                                "FROM student_master " +
                                "INNER JOIN module_details ON student_master.studentId = module_details.studentId "+
                                "INNER JOIN module_master ON module_details.moduleId = module_master.moduleId " +
                                "WHERE student_master.studentId =  " + studentIdList[i] + ";")
            except Exception as e:
                print("could not extract student records\n", e)
        
            #calculates sem1, sem2, cumulative gpa. returns list of values
            studentGpaResults = DriverHelper.calculateGpa(studentInfo)

            if studentGpaResults[2] <= 2.2 and studentGpaResults[2] != 0:
                self.probationIdList.append([studentId, studentGpaResults[2]])

            i = i+1






    def generateStudentStaffInfoList(self):

        for record in self.probationIdList: #loops through id list, packages data in 2d array

            studentStaffInfo = 0

            # create array, [id, name, email, program, school, advisorName, advisorEmail, 
            # pdName, pdEmail, facultyAdminName, facultyAdminEmail] for each student id
            try:
                studentStaffRecord = self.database.queryDb(
                    "SELECT student_master.studentId, student_master.student_Name, student_master.email, student_master.programme,  student_master.school," +   
                    "advisor.name, advisor.email, directors.name, directors.email, school.adminName, school.adminEmail " +
                    "FROM student_master " + 
                    "INNER JOIN advisor ON advisor.advisorId = student_master.advisor " + 
                    "INNER JOIN school ON student_master.school = school.schoolID " +
                    "INNER JOIN programme ON student_master.programme = programme.pid " +
                    "INNER JOIN directors ON programme.director = directors.id " +
                    "WHERE student_master.studentId = " + record[0] + ";")

                studentStaffInfo = studentStaffRecord[0] # [a,b,c] <- [[a,b,c]]
                studentStaffInfo.append(record[1]) #appends cumulative GPA to array
                self.studentStaffInfoList.append(studentStaffInfo) #append array to global var
            except Exception as e:
                print("could not retrieve records of student and staff")
            
        





    def sendEmail(self, destination, message):

        port = 587

        server = smtplib.SMTP("smtp.gmail.com", port)
        server.starttls()
        server.login(self.senderEmail, self.senderEmailAppPassword)
        server.sendmail(self.senderEmail, destination, message)
        print("email sent to: " + destination)







    def getStudentMessage(self, record):

        msg = MIMEText(
            "Good day " + record[1] + ",\n\n"
            "This email serves to notify you that your current GPA is " + str(record[11]) + ". "
            "As per the University's policy, any cumulative GPA at or below 2.2 requires that the student " +
            "to be placed on academic probation. \n\n\n Sincerely." 
        )

        msg['Subject'] = 'Probation warning'
        msg['From'] = self.senderEmail
        msg['To'] = record[2]

        return msg.as_string()
    

    def getAdvisorMessage(self, record):

        msg = MIMEText(
            "Good day " + record[5] + ",\n\n"
            "This email serves to notify you that " + record[1] + "\'s " + "current GPA is " + str(record[11]) + ". "
            "As per the University's policy, any cumulative GPA at or below 2.2 requires that the student " +
            "to be placed on academic probation. \n\n\n Sincerely." 
        )

        msg['Subject'] = 'Probation warning'
        msg['From'] = self.senderEmail
        msg['To'] = record[6]

        return msg.as_string()
    

    def getPdMessage(self, record):

        msg = MIMEText(
            "Good day " + record[7] + ",\n\n"
            "This email serves to notify you that " + record[1] + "\'s " + "current GPA is " + str(record[11]) + ". "
            "As per the University's policy, any cumulative GPA at or below 2.2 requires that the student " +
            "to be placed on academic probation. \n\n\n Sincerely."  
        )

        msg['Subject'] = 'Probation warning'
        msg['From'] = self.senderEmail
        msg['To'] = record[8]

        return msg.as_string()
    

    def getFacultyAdminMessage(self, record):

        msg = MIMEText(
            "Good day " + record[9] + ",\n\n"
            "This email serves to notify you that " + record[1] + "\'s " + "current GPA is " + str(record[11]) + ". "
            "As per the University's policy, any cumulative GPA at or below 2.2 requires that the student " +
            "to be placed on academic probation. \n\n\n Sincerely." 
        )

        msg['Subject'] = 'Probation warning'
        msg['From'] = self.senderEmail
        msg['To'] = record[10]

        return msg.as_string()
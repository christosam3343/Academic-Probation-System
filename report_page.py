

class ReportPage:

    def __init__ (self):
        self.reportPageLink = r"report_page.bat"
        self.htmlPage = ""
        self.reportYear = ""
        self.reportGpa = ""
        self.reportData = ""
        self.REPORTGPADEFAULT = "2.2"



    
    def constructHtml(self):
        self.htmlPage = (
            "<!DOCTYPE html>" + 
                "<html lang=en>" +
                    "<head>" +
                        "<meta charset=utf-8>" +
                        "<title> Report Page </title>" +
                        "<link href=\"reportPageStyle.css\" rel=stylesheet>" +
                        "<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css\">" +
                    "</head>" +
                    "<body>" +
                        "<video autoplay loop muted id=\"video-background\">" +
                            "<source src=\"reportPageAssets/bgvid.mp4\" type=\"video/mp4\">" +
                        "</video>" +
                        "<div id=\"logo-container\">" +
                            "<img id=\"logo\" src=\"reportPageAssets/utech-logo.png\" alt=\"University Logo\">" +
                        "</div>" +
                            "<h1 id=\"title\">University of Technology</h1>" +
                            "<div id=\"university-name\">" +
                                "<h2 id=\"address\">237 Old Hope Road</h2>" +
                                "<h2 id=\"address\">Kingston 6</h2>"
                                "<h2 id=\"address\">Tel: (876)927-1680</h2>" +
                                "<span id=\"contact\"></span>" +
                            "</div>" +
                        "<br>" +
                        "<div class=\"container glass\"> " +
                            "<h2 id= \"title1\" align=center> Academic Probation Alert GPA Report </h2>" + 
                            "<h3 id= \"title3\" class=\"yrgpa\" align=center> Year: " + self.reportYear + "</h3>" +
                            "<h3 id= \"title4\" class=\"yrgpa\" align=center> GPA: " + str(self.reportGpa) + "</h3>" +
                            "<div id= \"body_div\">" + 
                                "<div id=\"sidebar_div\">" + 
                                    "<br>" +
                                    "<span id=\"sort_title\">Sort</span><br>" +
                                    "<p id=\"sort_help\">(Sorts fields 9-0 & A-Z)</p>" +
                                    "<select id=\"sort_select\" name=\"sort\">" +
                                            "<option value=\"0\">ID</option>" +
                                            "<option value=\"1\">Name</option>" +
                                            "<option value=\"2\">Semester 1</option>" +
                                            "<option value=\"3\">Semester 2</option>" +
                                            "<option value=\"4\">Cumulative GPA</option>" +
                                    "</select>" +
                                    "<br><br><br>" +
                                    "<label id=\"filter_title\" for=\"filter\">Filter</label>" + 
                                    "<input type=\"text\" id=\"filter_text\" name=\"filter\">" +
                                    "<select id=\"filter_dropdown\">" + 
                                        "<option value=\"2\">Semester 1 Gpa</option>" + 
                                        "<option value=\"3\">Semester 2 Gpa</option>" + 
                                        "<option value=\"4\">Cumulative Gpa</option>" + 
                                    "</select>" +
                                    "<br>" +
                                    "<input type=\"radio\" id=\"filter_greater\" name=\"filter_radio\" value =\"greater\" checked>" +
                                    "<label for=\"filter_greater\">Greater than</label>" +
                                    "<input type=\"radio\" id=\"filter_less\" name=\"filter_radio\" value =\"lesser\">" +
                                    "<label for=\"filter_less\">Less than</label><br>" +
                                    "<p id=\"filter_help\">(Filters for Sem 1, Sem 2 & Cum GPAs)</p>" +
                                    "<br>" +
                                    "<div id=\"filter_bttn_div\" align=center>" +
                                        "<button id=\"filter_sort_bttn\" type=\"button\"><i class=\"fas fa-sort\"></i> Filter/Sort</button>" +
                                        "<button id=\"reset_bttn\" type=\"button\">Reset</button>" +
                                    "</div>" +
                                "</div>" +
                                "<div id= \"table_div\" align=center>" + self.reportData + "</div>" +
                                "<div id=\"analytics_div\">" +
                                    "<p id=\"analytics_title\">Analytics</p>" +
                                    "<p id=\"analytics_help\" align=center>(Semester 1 and Semester 2 Average)</p>" +
                                    "<div id=\"colChart\">" +
                                        "<div id=\"sem1Bar\"></div>" +
                                        "<div id=\"sem2Bar\"></div>" +
                                    "</div>" +
                                    "<div id=\"colLegend\">" +
                                        "<p id=\"sem1Title\">Semester 1</p>" +
                                        "<p id=\"sem2Title\">Semester 2</p>" +
                                    "</div>" +
                                    "<p id=\"analytics_summary\" align=center>Data shows that there is a 5 percent diffrence between semester 1 and semester 2</p>" +
                                "</div>" +
                            "</div>" +
                        "</div>" +
                        "<script type=text/javascript src=\"reportPageScript.js\"></script>" +
                    "</body>" +
                "</html>"
                )
    
    


    def getReportYear(self):
        return self.reportYear
    
    def setReportYear(self, year):
        self.reportYear = year

    def getreportGpa(self):
        return self.reportGpa
    
    def setreportGpa(self, gpa):
        self.reportGpa = gpa

    def getreportData(self):
        return self.reportData
    
    def setreportData(self, Data):
        self.reportData = Data

    def getHtmlPage(self):
        return self.htmlPage
    
    def setHtmlPage(self, html):
        self.htmlPage = html


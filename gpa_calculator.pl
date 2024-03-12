


% gradePoint(grade, credit) takes grade and credit for a course, calculates and returns gradepoints for that course
gradePoint(Grade, Credit, Gpa):-Gpa is Grade * Credit.


% gradePointEarned([gradePoints], [totalCredits]) takes a list of gradepoints for a student and total credits, return gpa for given semester
calGpa(GradePointsList, CreditsList, Gpa):-sum_list(GradePointsList, TotalGradePoints),sum_list(CreditsList, TotalCredits),Gpa is TotalGradePoints / TotalCredits.

% cumulative(gpaSem1, gpaSem2, totalCreditsSem1, totalCreditsSem2) return cumulative gpa
cumulative(Sem1GradePointsList, Sem2GradePointsList, TotalCreditsSem1, TotalCreditsSem2, CumulativeGPA):-
    TotalCredits is TotalCreditsSem1 + TotalCreditsSem2,
    sum_list(Sem1GradePointsList, Sem1TotalGradePointsList),
    sum_list(Sem2GradePointsList, Sem2TotalGradePointsList),
    TotalGradePoints is Sem1TotalGradePointsList + Sem2TotalGradePointsList,
    CumulativeGPA is TotalGradePoints / TotalCredits.

% sumCredits([creditList]) returns a sum of all credits.
sum(List, Total ):-sum_list(List, Total ).

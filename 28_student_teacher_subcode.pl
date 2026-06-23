% 28. Write a Prolog Program for STUDENT-TEACHER-SUB-CODE.

% Facts: teaches(Teacher, Subject, Code)
teaches(mr_kumar, dbms, cs301).
teaches(mrs_priya, java, cs302).
teaches(mr_anand, prolog, cs303).
teaches(mrs_lakshmi, networks, cs304).

% Facts: enrolled(Student, SubCode)
enrolled(arjun, cs301).
enrolled(meena, cs302).
enrolled(arjun, cs303).
enrolled(divya, cs304).
enrolled(meena, cs303).

% Rule: find teacher of a given student (via subject code they're enrolled in)
student_teacher(Student, Teacher) :-
    enrolled(Student, Code),
    teaches(Teacher, _, Code).

% Rule: find subject taught by a teacher
teacher_subject(Teacher, Subject) :-
    teaches(Teacher, Subject, _).

% Rule: find all students taught by a given teacher
students_of(Teacher, Student) :-
    teaches(Teacher, _, Code),
    enrolled(Student, Code).

% Rule: find subject code for a subject name
subject_code(Subject, Code) :-
    teaches(_, Subject, Code).

/*
Sample Queries:
?- student_teacher(arjun, Teacher).
Teacher = mr_kumar ;
Teacher = mr_anand.

?- teacher_subject(mrs_priya, Subject).
Subject = java.

?- students_of(mr_anand, Student).
Student = arjun ;
Student = meena.

?- subject_code(networks, Code).
Code = cs304.
*/

% 27. Write a Prolog Program for A DB WITH NAME, DOB.

% Facts: person(Name, Day, Month, Year)
person(ravi, 12, 5, 1998).
person(anu, 23, 11, 2000).
person(karthik, 1, 1, 1999).
person(divya, 30, 7, 2001).
person(suresh, 15, 3, 1997).

% Get DOB of a given name
dob(Name, Day, Month, Year) :-
    person(Name, Day, Month, Year).

% Find all people born in a given year
born_in_year(Year, Name) :-
    person(Name, _, _, Year).

% Find all people born in a given month
born_in_month(Month, Name) :-
    person(Name, _, Month, _).

% Check if a person is older than another (by year only, simple comparison)
older_than(Name1, Name2) :-
    person(Name1, _, _, Y1),
    person(Name2, _, _, Y2),
    Y1 < Y2.

/*
Sample Queries:
?- dob(ravi, D, M, Y).
D = 12, M = 5, Y = 1998.

?- born_in_year(1999, Name).
Name = karthik.

?- born_in_month(11, Name).
Name = anu.

?- older_than(ravi, anu).
true.

?- person(Name, _, _, 2000).
Name = anu.
*/

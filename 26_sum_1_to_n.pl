% 26. Write a Prolog Program to Sum the Integers from 1 to n.

sum_n(0, 0).
sum_n(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_n(N1, Sum1),
    Sum is Sum1 + N.

/*
Sample Queries:
?- sum_n(5, S).
S = 15.

?- sum_n(10, S).
S = 55.

?- sum_n(100, S).
S = 5050.
*/

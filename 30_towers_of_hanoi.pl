% 30. Write a Prolog Program to implement Towers of Hanoi.

hanoi(N) :-
    move(N, left, middle, right).

move(0, _, _, _) :- !.
move(N, From, To, Via) :-
    N > 0,
    N1 is N - 1,
    move(N1, From, Via, To),
    format("Move disc ~w from ~w to ~w~n", [N, From, To]),
    move(N1, Via, To, From).

/*
Sample Queries:
?- hanoi(3).
Move disc 1 from left to middle
Move disc 2 from left to right
Move disc 1 from middle to right
Move disc 3 from left to middle
Move disc 1 from right to left
Move disc 2 from right to middle
Move disc 1 from left to middle
true.

?- hanoi(4).
(prints the sequence of moves for 4 discs)
*/

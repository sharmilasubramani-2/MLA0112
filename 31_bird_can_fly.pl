% 31. Write a Prolog Program to print particular bird can fly or not.
% Incorporate required queries.

% Facts
bird(sparrow).
bird(eagle).
bird(penguin).
bird(ostrich).
bird(crow).
bird(kiwi).

% Birds that cannot fly (exceptions)
cannot_fly(penguin).
cannot_fly(ostrich).
cannot_fly(kiwi).

% Rule: a bird can fly if it is a bird and not in the cannot_fly list
can_fly(X) :-
    bird(X),
    \+ cannot_fly(X).

% Rule to print result
check_fly(X) :-
    bird(X),
    can_fly(X),
    format("~w can fly.~n", [X]).
check_fly(X) :-
    bird(X),
    cannot_fly(X),
    format("~w cannot fly.~n", [X]).
check_fly(X) :-
    \+ bird(X),
    format("~w is not a recognized bird.~n", [X]).

/*
Sample Queries:
?- check_fly(sparrow).
sparrow can fly.
true.

?- check_fly(penguin).
penguin cannot fly.
true.

?- check_fly(crow).
crow can fly.
true.

?- can_fly(eagle).
true.

?- can_fly(ostrich).
false.

?- check_fly(parrot).
parrot is not a recognized bird.
true.
*/

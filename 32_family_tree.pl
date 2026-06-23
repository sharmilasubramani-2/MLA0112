% 32. Write the prolog program to implement family tree.
% Pam, Liz, Ann and Pat are female, while Tom, Bob and Jim are male persons.

% Gender facts
female(pam).
female(liz).
female(ann).
female(pat).

male(tom).
male(bob).
male(jim).

% Parent facts: parent(Parent, Child)
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pam, bob).
parent(pam, liz).
parent(liz, jim).

% Mother relation
mother(M, C) :-
    parent(M, C),
    female(M).

% Father relation
father(F, C) :-
    parent(F, C),
    male(F).

% Grandfather relation
grandfather(GF, C) :-
    parent(GF, P),
    parent(P, C),
    male(GF).

% Grandmother relation
grandmother(GM, C) :-
    parent(GM, P),
    parent(P, C),
    female(GM).

% Sister relation (shares at least one parent, is female, not same person)
sister(S, C) :-
    parent(P, S),
    parent(P, C),
    female(S),
    S \= C.

% Brother relation
brother(B, C) :-
    parent(P, B),
    parent(P, C),
    male(B),
    B \= C.

/*
Sample Queries:
?- mother(pam, bob).
true.

?- father(tom, liz).
true.

?- grandfather(tom, ann).
true.

?- grandmother(pam, ann).
true.

?- sister(pat, ann).
true.

?- brother(jim, X).
false.   % jim has no siblings sharing both listed parents in this dataset

?- sister(X, pat).
X = ann.
*/

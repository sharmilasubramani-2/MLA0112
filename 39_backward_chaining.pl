% 39. Write a Prolog Program for backward Chaining. Incorporate required queries.
%
% Backward chaining: start from a goal and work backwards, checking if
% facts/rules support it. This is exactly how Prolog's own resolution
% engine works, so we demonstrate it explicitly with rule/2 clauses
% and a query-driven proves/1 predicate (mirroring the forward_chain example).

% Known base facts
fact(has_hair).
fact(eats_meat).
fact(has_sharp_teeth).
fact(has_claws).
fact(has_forward_eyes).
fact(tawny_color).
fact(dark_spots).

% Rules: rule(Conclusion, ListOfConditions)
rule(mammal, [has_hair]).
rule(mammal, [gives_milk]).
rule(carnivore, [mammal, eats_meat]).
rule(carnivore, [mammal, has_sharp_teeth, has_claws, has_forward_eyes]).
rule(cheetah, [carnivore, tawny_color, dark_spots]).
rule(tiger, [carnivore, tawny_color, black_stripes]).

% proves(Goal): backward chaining - tries to prove Goal is true
% by checking facts first, then trying to satisfy a rule's conditions recursively
proves(Goal) :-
    fact(Goal).
proves(Goal) :-
    rule(Goal, Conditions),
    proves_all(Conditions).

% proves_all(ListOfGoals): every goal in the list must be provable
proves_all([]).
proves_all([H|T]) :-
    proves(H),
    proves_all(T).

/*
Sample Queries:
?- proves(cheetah).
true.

?- proves(mammal).
true.

?- proves(tiger).
false.    % black_stripes is not a known fact

?- proves(carnivore).
true.

% Trace for proves(cheetah):
% cheetah needs [carnivore, tawny_color, dark_spots]
%   carnivore needs [mammal, eats_meat]
%     mammal needs [has_hair] -> fact -> true
%     eats_meat -> fact -> true
%   tawny_color -> fact -> true
%   dark_spots -> fact -> true
% => cheetah proved true
*/

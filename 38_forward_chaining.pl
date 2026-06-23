% 38. Write a Prolog Program for forward Chaining. Incorporate required queries.
%
% Example domain: identifying an animal using forward chaining rules.
% Forward chaining: start from known facts, apply rules to derive new facts,
% repeat until no new facts can be derived (or the goal is reached).

:- dynamic(fact/1).

% Known facts about the animal
fact(has_hair).
fact(eats_meat).
fact(has_sharp_teeth).
fact(has_claws).
fact(has_forward_eyes).
fact(tawny_color).
fact(dark_spots).

% Rules: rule(IF_Conditions, THEN_Conclusion)
rule([has_hair], mammal).
rule([gives_milk], mammal).
rule([mammal, eats_meat], carnivore).
rule([mammal, has_sharp_teeth, has_claws, has_forward_eyes], carnivore).
rule([carnivore, tawny_color, dark_spots], cheetah).
rule([carnivore, tawny_color, black_stripes], tiger).

% forward_chain: repeatedly apply rules to derive new facts until fixpoint
forward_chain :-
    rule(Conditions, Conclusion),
    \+ fact(Conclusion),
    all_true(Conditions),
    assertz(fact(Conclusion)),
    format("Derived new fact: ~w~n", [Conclusion]),
    !,
    forward_chain.
forward_chain :-
    format("No more facts can be derived.~n").

% Helper: check that every condition in the list is already a known fact
all_true([]).
all_true([H|T]) :-
    fact(H),
    all_true(T).

/*
Sample Queries:
?- forward_chain.
Derived new fact: mammal
Derived new fact: carnivore
Derived new fact: cheetah
No more facts can be derived.
true.

?- fact(cheetah).
true.    % (after forward_chain has been run)

?- fact(mammal).
true.

% Note: forward_chain uses assertz, so run it once per session.
% To reset, restart swipl or use: retractall(fact(mammal)), retractall(fact(carnivore)), retractall(fact(cheetah)).
*/

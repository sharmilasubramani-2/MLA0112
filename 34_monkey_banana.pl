% 34. Write a Prolog program to implement Monkey Banana Problem.
%
% State is represented as: state(MonkeyPosition, MonkeyLocation, BoxPosition, HasBanana)
% MonkeyLocation is either 'onfloor' or 'onbox'
% HasBanana is either 'has' or 'hasnot'
% Banana is assumed to hang at position 'middle'.

% Move 1: Grasp the banana (only works if monkey is on box, at middle, box at middle)
move(state(middle, onbox, middle, hasnot),
     grasp,
     state(middle, onbox, middle, has)).

% Move 2: Climb on the box (monkey and box must be at the same position P)
move(state(P, onfloor, P, H),
     climb,
     state(P, onbox, P, H)).

% Move 3: Push the box from P1 to P2 (monkey must be on floor, at same place as box)
move(state(P1, onfloor, P1, H),
     push(P1, P2),
     state(P2, onfloor, P2, H)).

% Move 4: Walk from P1 to P2 (monkey on floor, box position B unaffected)
move(state(P1, onfloor, B, H),
     walk(P1, P2),
     state(P2, onfloor, B, H)).

% canget(State): true if the monkey can eventually get the banana from State
canget(state(_, _, _, has)).

canget(State1) :-
    move(State1, _, State2),
    canget(State2).

% canget_plan(State, Plan): same as canget but also returns the sequence of moves
canget_plan(state(_, _, _, has), []).
canget_plan(State1, [Move|Moves]) :-
    move(State1, Move, State2),
    canget_plan(State2, Moves).

/*
Sample Queries:
?- canget(state(atdoor, onfloor, atwindow, hasnot)).
true.

?- canget_plan(state(atdoor, onfloor, atwindow, hasnot), Plan).
Plan = [walk(atdoor, atwindow), push(atwindow, middle), climb, grasp].

?- canget(state(atdoor, onbox, atwindow, hasnot)).
true.
*/

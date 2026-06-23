% 35. Write a Prolog Program for fruit and its color using Back Tracking.

% Facts: fruit_color(Fruit, Color)
fruit_color(apple, red).
fruit_color(apple, green).
fruit_color(banana, yellow).
fruit_color(grape, green).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(mango, yellow).
fruit_color(mango, green).
fruit_color(strawberry, red).

% Rule: find color(s) of a fruit (backtracks through multiple matches)
color_of(Fruit, Color) :-
    fruit_color(Fruit, Color).

% Rule: find all fruits of a given color (backtracking over facts)
fruits_of_color(Color, Fruit) :-
    fruit_color(Fruit, Color).

% Rule: find fruits that come in more than one color
% (uses backtracking + findall to collect all solutions)
multi_color_fruit(Fruit) :-
    fruit_color(Fruit, C1),
    fruit_color(Fruit, C2),
    C1 \= C2.

% Rule: list all distinct colors a fruit has (no duplicates)
all_colors(Fruit, Colors) :-
    findall(C, fruit_color(Fruit, C), Colors).

/*
Sample Queries:
?- color_of(apple, C).
C = red ;
C = green.

?- fruits_of_color(yellow, F).
F = banana ;
F = mango.

?- multi_color_fruit(F).
F = apple ;
F = grape ;
F = mango ;
... (with repeats from backtracking; use setof/bagof to dedupe)

?- setof(F, multi_color_fruit(F), Fruits).
Fruits = [apple, grape, mango].

?- all_colors(grape, Colors).
Colors = [green, purple].
*/

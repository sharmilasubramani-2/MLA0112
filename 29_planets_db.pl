% 29. Write a Prolog Program for PLANETS DB.

% Facts: planet(Name, PositionFromSun, Type, NumMoons)
planet(mercury, 1, terrestrial, 0).
planet(venus, 2, terrestrial, 0).
planet(earth, 3, terrestrial, 1).
planet(mars, 4, terrestrial, 2).
planet(jupiter, 5, gas_giant, 79).
planet(saturn, 6, gas_giant, 83).
planet(uranus, 7, ice_giant, 27).
planet(neptune, 8, ice_giant, 14).

% Rule: find planets of a given type
planet_of_type(Type, Name) :-
    planet(Name, _, Type, _).

% Rule: find planet at a given position
planet_at(Position, Name) :-
    planet(Name, Position, _, _).

% Rule: find which planet has more moons
more_moons(P1, P2) :-
    planet(P1, _, _, M1),
    planet(P2, _, _, M2),
    M1 > M2.

% Rule: planet immediately before another (inner neighbor)
inner_neighbor(P1, P2) :-
    planet(P1, Pos1, _, _),
    planet(P2, Pos2, _, _),
    Pos2 is Pos1 + 1.

% Rule: total moons of all planets
total_moons(Total) :-
    findall(M, planet(_, _, _, M), List),
    sum_list(List, Total).

/*
Sample Queries:
?- planet_of_type(gas_giant, Name).
Name = jupiter ;
Name = saturn.

?- planet_at(3, Name).
Name = earth.

?- more_moons(saturn, earth).
true.

?- inner_neighbor(mars, jupiter).
true.

?- total_moons(T).
T = 206.
*/

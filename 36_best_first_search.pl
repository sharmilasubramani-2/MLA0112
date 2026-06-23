% 36. Write a Prolog Program to implement Best First Search algorithm.
%
% Greedy Best First Search: at each step, expand the unvisited neighbor
% with the smallest heuristic value h(Node) (estimated distance to goal).

% Graph edges (undirected, cost not used by greedy heuristic search but kept for reference)
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, d).
edge(c, e).
edge(d, f).
edge(e, f).

% Undirected neighbor relation
neighbor(X, Y) :- edge(X, Y).
neighbor(X, Y) :- edge(Y, X).

% Heuristic: estimated distance from each node to the goal 'f'
h(a, 10).
h(b, 7).
h(c, 6).
h(d, 4).
h(e, 2).
h(f, 0).

% best_first_search(+Start, +Goal, -Path)
best_first_search(Start, Goal, Path) :-
    search([Start], Start, Goal, [Start], Path).

% search(VisitedSoFarAsPath, CurrentNode, Goal, VisitedSet, FinalPath)
search(Path, Goal, Goal, _, Path) :- !.
search(PathSoFar, Current, Goal, Visited, FinalPath) :-
    findall(N-H, ( neighbor(Current, N),
                   \+ member(N, Visited),
                   h(N, H) ),
            Candidates),
    Candidates \= [],
    best_node(Candidates, Next),
    append(PathSoFar, [Next], NewPath),
    search(NewPath, Next, Goal, [Next|Visited], FinalPath).

% best_node(+ListOfNode-Heuristic, -NodeWithLowestHeuristic)
best_node([N-H|Rest], Best) :-
    best_node(Rest, N, H, Best).

best_node([], BestSoFar, _, BestSoFar).
best_node([N-H|Rest], _, BestH, Best) :-
    H < BestH, !,
    best_node(Rest, N, H, Best).
best_node([_-_|Rest], CurrentBest, CurrentBestH, Best) :-
    best_node(Rest, CurrentBest, CurrentBestH, Best).

/*
Sample Queries:
?- best_first_search(a, f, Path).
Path = [a, c, e, f].

Trace:
- At 'a': neighbors b(h=7), c(h=6) -> pick c (lowest h)
- At 'c': neighbors d(h=4), e(h=2) (b,a visited/excluded as needed) -> pick e (lowest h)
- At 'e': neighbor f(h=0) -> pick f
- f is goal -> stop. Path = [a, c, e, f]

?- best_first_search(a, d, Path).
Path = [a, c, d].
*/

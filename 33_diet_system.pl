% 33. Write a Prolog Program to suggest Dieting System based on Disease.

% Facts: disease and recommended/avoided foods
diet(diabetes, avoid, sugar).
diet(diabetes, avoid, white_rice).
diet(diabetes, eat, vegetables).
diet(diabetes, eat, whole_grains).

diet(hypertension, avoid, salt).
diet(hypertension, avoid, processed_food).
diet(hypertension, eat, fruits).
diet(hypertension, eat, low_fat_dairy).

diet(obesity, avoid, fried_food).
diet(obesity, avoid, sugary_drinks).
diet(obesity, eat, salads).
diet(obesity, eat, lean_protein).

diet(anemia, eat, spinach).
diet(anemia, eat, red_meat).
diet(anemia, eat, iron_supplements).
diet(anemia, avoid, tea_with_meals).

diet(heart_disease, avoid, saturated_fat).
diet(heart_disease, avoid, red_meat).
diet(heart_disease, eat, fish).
diet(heart_disease, eat, nuts).

% Rule: suggest foods to eat for a disease
suggest_eat(Disease, Food) :-
    diet(Disease, eat, Food).

% Rule: suggest foods to avoid for a disease
suggest_avoid(Disease, Food) :-
    diet(Disease, avoid, Food).

% Rule: print full diet plan
diet_plan(Disease) :-
    format("Diet plan for ~w:~n", [Disease]),
    format("Foods to EAT:~n"),
    forall(suggest_eat(Disease, F), format("  - ~w~n", [F])),
    format("Foods to AVOID:~n"),
    forall(suggest_avoid(Disease, F), format("  - ~w~n", [F])).

/*
Sample Queries:
?- suggest_eat(diabetes, F).
F = vegetables ;
F = whole_grains.

?- suggest_avoid(hypertension, F).
F = salt ;
F = processed_food.

?- diet_plan(obesity).
Diet plan for obesity:
Foods to EAT:
  - salads
  - lean_protein
Foods to AVOID:
  - fried_food
  - sugary_drinks
true.
*/

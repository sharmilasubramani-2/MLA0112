# Prolog Lab Programs (26–39)

This repo contains SWI-Prolog implementations for lab programs 26 through 39.

| File | Program |
|---|---|
| 26_sum_1_to_n.pl | Sum of integers from 1 to n |
| 27_db_name_dob.pl | DB with Name, DOB |
| 28_student_teacher_subcode.pl | Student-Teacher-Sub-Code DB |
| 29_planets_db.pl | Planets DB |
| 30_towers_of_hanoi.pl | Towers of Hanoi |
| 31_bird_can_fly.pl | Bird can fly or not |
| 32_family_tree.pl | Family tree |
| 33_diet_system.pl | Dieting system based on disease |
| 34_monkey_banana.pl | Monkey Banana Problem |
| 35_fruit_color_backtracking.pl | Fruit and its color using backtracking |
| 36_best_first_search.pl | Best First Search algorithm |
| 37_medical_diagnosis.pl | Medical Diagnosis |
| 38_forward_chaining.pl | Forward Chaining |
| 39_backward_chaining.pl | Backward Chaining |

Each `.pl` file has the sample queries and expected output written as a comment block at the bottom, so you can test it yourself.

---

## 1. Install SWI-Prolog

- **Windows:** download the installer from https://www.swi-prolog.org/download/stable and run it (keep default options).
- **Mac:** `brew install swi-prolog`
- **Linux:** `sudo apt update && sudo apt install swi-prolog`

Check it installed correctly:
```
swipl --version
```

## 2. Run a program

From the folder containing the `.pl` files:
```
swipl 26_sum_1_to_n.pl
```
This opens the Prolog interactive shell (`?-` prompt) with the file already loaded. Then type a query from the comments at the bottom of the file, e.g.:
```
?- sum_n(10, S).
```
Press Enter. To exit the shell: type `halt.` and press Enter.

If you'd rather load a file from inside an already-open `swipl` shell:
```
?- [26_sum_1_to_n].
```
(square brackets, filename without `.pl`, no leading `swipl`)

## 3. Push to your GitHub repo

If you haven't already cloned/initialized your repo locally:
```
git clone <your-repo-url>
cd <your-repo-folder>
```
Copy all the `.pl` files (and this README) into that folder, then:
```
git add .
git commit -m "Add Prolog lab programs 26-39"
git push origin main
```
(use `master` instead of `main` if that's your default branch name — check with `git branch`)

If this is a brand-new repo with nothing pushed yet:
```
git init
git add .
git commit -m "Add Prolog lab programs 26-39"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## Notes

- Program 38 (forward chaining) uses `assertz/1`, so it modifies the live fact database when run. If you run `forward_chain.` more than once in the same session, re-run `swipl` fresh (or use `retractall/1` as noted in that file's comments) to reset.
- Program 36 (Best First Search) is a heuristic-driven greedy search, not the cost-based A* — matches the standard syllabus version of this algorithm.

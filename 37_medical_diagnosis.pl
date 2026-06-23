% 37. Write the prolog program for Medical Diagnosis.

% Facts: symptom(Disease, Symptom)
symptom(flu, fever).
symptom(flu, cough).
symptom(flu, body_ache).
symptom(flu, headache).

symptom(cold, sneezing).
symptom(cold, runny_nose).
symptom(cold, cough).
symptom(cold, sore_throat).

symptom(malaria, fever).
symptom(malaria, chills).
symptom(malaria, sweating).
symptom(malaria, headache).

symptom(typhoid, fever).
symptom(typhoid, weakness).
symptom(typhoid, stomach_pain).
symptom(typhoid, loss_of_appetite).

symptom(covid19, fever).
symptom(covid19, cough).
symptom(covid19, breathlessness).
symptom(covid19, loss_of_smell).

% Rule: diagnose disease based on a list of symptoms entered by patient
% A disease is suggested if all its key symptoms are present in patient's list
diagnose(PatientSymptoms, Disease) :-
    findall(S, symptom(Disease, S), DiseaseSymptoms),
    DiseaseSymptoms \= [],
    subset_match(DiseaseSymptoms, PatientSymptoms).

% Helper: check every element of List1 is a member of List2
subset_match([], _).
subset_match([H|T], List2) :-
    member(H, List2),
    subset_match(T, List2).

% Rule: list all possible diseases for given symptoms (no duplicates)
possible_diseases(PatientSymptoms, Diseases) :-
    setof(D, diagnose(PatientSymptoms, D), Diseases).

/*
Sample Queries:
?- diagnose([fever, cough, body_ache, headache], flu).
true.

?- diagnose([fever, chills, sweating, headache], malaria).
true.

?- possible_diseases([fever, cough], D).
D = [covid19, flu].

?- diagnose([sneezing, runny_nose, cough, sore_throat], Disease).
Disease = cold.
*/

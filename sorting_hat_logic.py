import copy
import random

decrease_probability_accept_worse_score_each_step = 0.005


def switch_two_people(forms, people_to_switch):
    new_forms = copy.deepcopy(forms)
    for i in range(len(forms)):
        for j in range(2):
            if people_to_switch[j] in forms[i]:
                new_forms[i].remove(people_to_switch[j])
                new_forms[i].append(people_to_switch[j - 1])
    return new_forms


def sort(forms, names):
    probability_accept_worse_score = 1
    global decrease_probability_accept_worse_score_each_step
    score = get_score(forms, names)
    failures = 0
    people = list(names.keys())
    while failures < 120:
        print(score)
        to_switch = random.sample(people, 2)
        test_forms = switch_two_people(forms, to_switch)
        test_score = get_score(test_forms, names)
        if test_score > score or random.random() < probability_accept_worse_score:
            forms = test_forms
            probability_accept_worse_score -= decrease_probability_accept_worse_score_each_step
            score = test_score
            failures = 0
        else:
            failures += 1
    return [forms, score]


def get_score(forms, names):
    score = 0
    friend_bonus = 1
    gender_penalty = 5
    for form in forms:
        gender_mismatch = 0
        for person in form:
            person_data = names.get(person)
            gender = person_data[0]
            friends = person_data[1]
            if gender == "M":
                gender_mismatch += 1
            else:
                gender_mismatch -= 1
            for friend in friends:
                if friend in form:
                    score += friend_bonus
        score -= abs(gender_mismatch) * gender_penalty
    return score

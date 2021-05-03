print("beta-sorting_hat-version=2.7")
print("___commencing___")

from name_checker import name_scanner
from sys import exit
from sorting_hat_logic import sort

# {"name": ["gender("M"/"F")", ["friend1", "friend2" etc.]]}

names = {}

num_of_forms = int(input("How many forms?"))
forms = [[] for _ in range(num_of_forms)]

with open("ListOfNames.csv", "r") as name_file:
    for line in name_file:
        line = line.rstrip()
        data = line.split(",")
        name = data[0]
        gender = data[1]
        friends = data[2:]
        names[name] = [gender, friends]

bad_friends = name_scanner(list(names.keys()), [i[1] for i in names.values()])
if len(bad_friends) > 0:
    print(bad_friends)
    print("Fix the data and run again!")
    exit()
else:
    print("Data all good calibrating forms now!")

for i in range(len(names.keys())):
    forms[i % num_of_forms].append(list(names.keys())[i])

best_forms = sort(forms, names)
print(best_forms)

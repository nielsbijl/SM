import csv
import pickle

teams = ['Ajax', 'Feyenoord', 'PSV', 'FC Utrecht', 'Willem II']

combinations = []

pool = {}


""" Alle combinaties van wedstrijden maken -> tuple(Team1, Team2)"""
for thuis in teams:
    for uit in teams:
        key = tuple((thuis, uit))
        combinations.append(key)

print(combinations)


def add_combination_to_dict(combination, win_chance, draw_chance, lose_chance):
    """
    Voegt aan een combinatie van 2 teams die tegen elkaar spelen, een lijst met 100 mogeijke uitkomsten.
    Dit kan zijn bijvoorbeeld: Team1, Team2, Gelijkspel
    Er is een kans dat het team wint of verliest of gelijkspel speelt, daarom 100 mogelijke uitkomsten.
    Als bijvoorbeeld ajax 60% kans heeft om te winnen zal die 60x in de lijst van mogelijke uitkomsten staan.

    :param combination: tuple(Home-team, away-team)
    :param win_chance: kans dat home-team wint
    :param draw_chance: kans dat er gelijk spel is
    :param lose_chance: kans dat het home-team verliest
    """
    for x in range(100):
        if x < win_chance:
            value.append(combination[0])
        if x < draw_chance:
            value.append("Draw")
        if x < lose_chance:
            value.append(combination[1])
    pool[combination] = value


"""
Voor elke mogelijke wedstrijd de combinatie met de kansen toevoegen aan een dictionary
"""

for combination in combinations:
    value = []
    if combination[0] == combination[1]:
        pool[combination] = None
    elif combination[0] == "Ajax" and combination[1] == "Feyenoord":
        add_combination_to_dict(combination, 65, 17, 18)
    elif combination[0] == "Ajax" and combination[1] == "PSV":
        add_combination_to_dict(combination, 54, 21, 25)
    elif combination[0] == "Ajax" and combination[1] == "FC Utrecht":
        add_combination_to_dict(combination, 74, 14, 12)
    elif combination[0] == "Ajax" and combination[1] == "Willem II":
        add_combination_to_dict(combination, 78, 13, 9)
    elif combination[0] == "Feyenoord" and combination[1] == "Ajax":
        add_combination_to_dict(combination, 30, 21, 49)
    elif combination[0] == "Feyenoord" and combination[1] == "PSV":
        add_combination_to_dict(combination, 37, 24, 39)
    elif combination[0] == "Feyenoord" and combination[1] == "FC Utrecht":
        add_combination_to_dict(combination, 51, 22, 27)
    elif combination[0] == "Feyenoord" and combination[1] == "Willem II":
        add_combination_to_dict(combination, 60, 21, 19)
    elif combination[0] == "PSV" and combination[1] == "Ajax":
        add_combination_to_dict(combination, 39, 22, 39)
    elif combination[0] == "PSV" and combination[1] == "Feyenoord":
        add_combination_to_dict(combination, 54, 22, 24)
    elif combination[0] == "PSV" and combination[1] == "FC Utrecht":
        add_combination_to_dict(combination, 62, 20, 18)
    elif combination[0] == "PSV" and combination[1] == "Willem II":
        add_combination_to_dict(combination, 62, 22, 16)
    elif combination[0] == "FC Utrecht" and combination[1] == "Ajax":
        add_combination_to_dict(combination, 25, 14, 61)
    elif combination[0] == "FC Utrecht" and combination[1] == "Feyenoord":
        add_combination_to_dict(combination, 37, 23, 40)
    elif combination[0] == "FC Utrecht" and combination[1] == "PSV":
        add_combination_to_dict(combination, 29, 24, 47)
    elif combination[0] == "FC Utrecht" and combination[1] == "Willem II":
        add_combination_to_dict(combination, 52, 23, 25)
    elif combination[0] == "Willem II" and combination[1] == "Ajax":
        add_combination_to_dict(combination, 17, 18, 65)
    elif combination[0] == "Willem II" and combination[1] == "Feyenoord":
        add_combination_to_dict(combination, 20, 26, 54)
    elif combination[0] == "Willem II" and combination[1] == "PSV":
        add_combination_to_dict(combination, 23, 24, 53)
    elif combination[0] == "Willem II" and combination[1] == "FC Utrecht":
        add_combination_to_dict(combination, 37, 25, 38)


"""
Checken of de pool dictionary correct is
"""
for match in combinations:
    if not pool[match]:
        print(match, pool[match])
    else:
        print(match, 'Total lenght options:', len(pool[match]), 'Win:', pool[match].count(match[0]), 'Draw:',
              pool[match].count("Draw"), 'Lose:', pool[match].count(match[1]))


# # Write data to CSV
# w = csv.writer(open("pool.csv", "w"))
# w.writerow(["Home", "Away", "All-possible-outcome"])
# for key, val in pool.items():
#     w.writerow([key[0], key[1], val])

"""" 
De pool dictionary exporteren als pickle bestand
"""
file_to_write = open("pool.pickle", "wb")
pickle.dump(pool, file_to_write)

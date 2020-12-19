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


def add_combination_to_dict(combination, win_chance, draw_chance, lose_chance, curr_pool):
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
    curr_pool[combination] = value
    return curr_pool


"""
Voor elke mogelijke wedstrijd de combinatie met de kansen toevoegen aan een dictionary
"""

for combination in combinations:
    value = []
    if combination[0] == combination[1]:
        pool[combination] = None
    elif combination[0] == "Ajax" and combination[1] == "Feyenoord":
        pool = add_combination_to_dict(combination, 65, 17, 18, pool)
    elif combination[0] == "Ajax" and combination[1] == "PSV":
        pool = add_combination_to_dict(combination, 54, 21, 25, pool)
    elif combination[0] == "Ajax" and combination[1] == "FC Utrecht":
        pool = add_combination_to_dict(combination, 74, 14, 12, pool)
    elif combination[0] == "Ajax" and combination[1] == "Willem II":
        pool = add_combination_to_dict(combination, 78, 13, 9, pool)
    elif combination[0] == "Feyenoord" and combination[1] == "Ajax":
        pool = add_combination_to_dict(combination, 30, 21, 49, pool)
    elif combination[0] == "Feyenoord" and combination[1] == "PSV":
        pool = add_combination_to_dict(combination, 37, 24, 39, pool)
    elif combination[0] == "Feyenoord" and combination[1] == "FC Utrecht":
        pool = add_combination_to_dict(combination, 51, 22, 27, pool)
    elif combination[0] == "Feyenoord" and combination[1] == "Willem II":
        pool = add_combination_to_dict(combination, 60, 21, 19, pool)
    elif combination[0] == "PSV" and combination[1] == "Ajax":
        pool = add_combination_to_dict(combination, 39, 22, 39, pool)
    elif combination[0] == "PSV" and combination[1] == "Feyenoord":
        pool = add_combination_to_dict(combination, 54, 22, 24, pool)
    elif combination[0] == "PSV" and combination[1] == "FC Utrecht":
        pool = add_combination_to_dict(combination, 62, 20, 18, pool)
    elif combination[0] == "PSV" and combination[1] == "Willem II":
        pool = add_combination_to_dict(combination, 62, 22, 16, pool)
    elif combination[0] == "FC Utrecht" and combination[1] == "Ajax":
        pool = add_combination_to_dict(combination, 25, 14, 61, pool)
    elif combination[0] == "FC Utrecht" and combination[1] == "Feyenoord":
        pool = add_combination_to_dict(combination, 37, 23, 40, pool)
    elif combination[0] == "FC Utrecht" and combination[1] == "PSV":
        pool = add_combination_to_dict(combination, 29, 24, 47, pool)
    elif combination[0] == "FC Utrecht" and combination[1] == "Willem II":
        pool = add_combination_to_dict(combination, 52, 23, 25, pool)
    elif combination[0] == "Willem II" and combination[1] == "Ajax":
        pool = add_combination_to_dict(combination, 17, 18, 65, pool)
    elif combination[0] == "Willem II" and combination[1] == "Feyenoord":
        pool = add_combination_to_dict(combination, 20, 26, 54, pool)
    elif combination[0] == "Willem II" and combination[1] == "PSV":
        pool = add_combination_to_dict(combination, 23, 24, 53, pool)
    elif combination[0] == "Willem II" and combination[1] == "FC Utrecht":
        pool = add_combination_to_dict(combination, 37, 25, 38, pool)


"""
Checken of de pool dictionary correct is
"""
# for match in combinations:
#     if not pool[match]:
#         print(match, pool[match])
#     else:
#         print(match, 'Total lenght options:', len(pool[match]), 'Win:', pool[match].count(match[0]), 'Draw:',
#               pool[match].count("Draw"), 'Lose:', pool[match].count(match[1]))


"""" 
De pool dictionary exporteren als pickle bestand
"""
file_to_write = open("pool.pickle", "wb")
pickle.dump(pool, file_to_write)

keys = {('Ajax', 'Ajax'): None, ('Ajax', 'Feyenoord'): (65, 17, 18), ('Ajax', 'PSV'): (54, 21, 25), ('Ajax', 'FC Utrecht'): (74, 14, 12), ('Ajax', 'Willem II'): (78, 13, 9), ('Feyenoord', 'Ajax'): (30, 21, 49), ('Feyenoord', 'Feyenoord'): None, ('Feyenoord', 'PSV'): (37, 24, 39), ('Feyenoord', 'FC Utrecht'): (51, 22, 27), ('Feyenoord', 'Willem II'): (60, 21, 19), ('PSV', 'Ajax'): (39, 22, 39), ('PSV', 'Feyenoord'): (54, 22, 24), ('PSV', 'PSV'): None, ('PSV', 'FC Utrecht'): (62, 20, 18), ('PSV', 'Willem II'): (62, 22, 16), ('FC Utrecht', 'Ajax'): (25, 14, 61), ('FC Utrecht', 'Feyenoord'): (37, 23, 40), ('FC Utrecht', 'PSV'): (29, 24, 47), ('FC Utrecht', 'FC Utrecht'): None, ('FC Utrecht', 'Willem II'): (52, 23, 25), ('Willem II', 'Ajax'): (17, 18, 65), ('Willem II', 'Feyenoord'): (20, 26, 54), ('Willem II', 'PSV'): (23, 24, 53), ('Willem II', 'FC Utrecht'): (37, 25, 38), ('Willem II', 'Willem II'): None}

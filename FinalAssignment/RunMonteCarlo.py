import pickle
import random
import pandas as pd
import numpy as np
from FinalAssignment.MersenneTwister import MersenneTwister


def add_score(home, away, outcome, curr_score_dict, points=3):
    """
    Geeft het aangewezen team de bijbehorende punten

    :param home: Thuis team
    :param away: Uit team
    :param outcome: Welk team gewonnen of gelijkspel
    :param curr_score_dict: De huidige score van de pool (hoeveel punten elk team al heeft)
    :param points: Hoeveel punten het winnende team krijgt (default 3, bij gelijk spel 1)
    :return: De huidige score na het spelen van de match
    """
    if outcome == "Draw":
        """Roept hier zichzelf aan en geeft beide teams 1 point"""
        curr_score_dict = add_score(home, away, home, curr_score_dict, 1)
        curr_score_dict = add_score(home, away, away, curr_score_dict, 1)
    else:
        curr_score_dict[outcome] += points
    return curr_score_dict


def run_one_match(match, chance):
    """
    Deze functie speelt 1 wedstrijd

    :param match: tuple(home, away)
    :param chance: tuple(home_win_chance, draw_chance, away_win_chance)
    :return: home | "draw" | away
            Return a string of the winning team or draw
    """
    home = match[0]
    away = match[1]
    home_win = chance[0]
    draw = chance[1]
    random_number = random.get_random_number_0_1() * 100
    if 0 <= random_number < home_win:
        return home
    elif home_win <= random_number < (home_win + draw):
        return "Draw"
    elif (home_win + draw) <= random_number < 100:
        return away


def run_one_pool(curr_pool):
    """
    Runt 1x de pool, dus alle combinaties van teams worden gespeeld.
    Na 1x spelen van de pool komt er een huidige score uit met welke teams welke punten hebben.

    :param curr_pool:  Dictionoary Key: Team VS Team, Value: welke kans elke uitkomst heeft
    :return: Dictionary: Key: Team, Value: Hoeveel punten het team heeft na het spelen van de pool
    """
    curr_score = {
        "Ajax": 0,
        "Feyenoord": 0,
        "PSV": 0,
        "FC Utrecht": 0,
        "Willem II": 0
    }
    for match in curr_pool:
        if curr_pool[match]:
            teamvsteam, chance = match, curr_pool[match]
            outcome = run_one_match(teamvsteam, chance)
            curr_score = add_score(teamvsteam[0], teamvsteam[1], outcome, curr_score)
    return curr_score


def get_key_with_max_value(dictionary):
    """
    Voor het krijgen van het team met de hoogste score

    Eerst maak je een lijst van keys en values van de dict aan,
    Dan return je de key met de hoogste value
    """
    values = list(dictionary.values())
    keys = list(dictionary.keys())
    return keys[values.index(max(values))]


def rank_teams_of_curr_run(curr_score, curr_ranking):
    """
    Na het spelen van een pool heeft ieder team een ranking gekregen
    Een ranking van 1ste tot 5e plek

    :param curr_score: De huidige scoren na het spelen van een pool
    :return: Een dictionary welk team op de eerste t/m de vijfde plaats staat
    """
    for place in curr_ranking:
        curr_place = get_key_with_max_value(curr_score)
        curr_ranking[place] = curr_ranking[place].__add__([curr_place])
        curr_score.pop(curr_place)
    return curr_ranking


def run_monte_carlo(runs, pool):
    """
    Het draaien van de monte carlo machine speelt gewoon heel veel pools (de hoeveelheid runs).
    Na het spelen van een pool wordt de ranking van die partij toegevoegd aan de totale ranking.
    Als bijvoorbeeld ajax 10x eerste wordt, dan staat die 10x in de lijst van total_ranking[1]

    :param runs: Hoevaak je de machine wilt runnen
    :param pool: Welke partijen allemaal tegen elkaar spelen en wat de kans is dat ze winnen/verliezen/gelijk
    :return: Een dictionary van alle rankings van alle gespeelde pools.
            Key: Welke rank/positie (1e t/m 5e plek)
            Value: Een lijst met hoevaak een team op die plek is gekomen
    """
    total_ranking = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }
    for run in range(runs):
        curr_score = run_one_pool(pool)
        total_ranking = rank_teams_of_curr_run(curr_score, total_ranking)
    return total_ranking


def get_monte_carlo_output_as_chance_pool_position(monte_carlo_output):
    """
    Rekent uit hoeveel kans elk team heeft om op welke positie te komen.

    :param monte_carlo_output: De dictionary met de totale ranking na het spelen van de pools
    :return: Een dictionary hoeveel kans elk team heeft om op alle posities te komen.
            Key: Team
            Value: [kans_1e_plek, kans_2e_plek, kans_3e_plek, kans_4e_plek, kans_5e_plek]
    """
    teams = ['FC Utrecht', 'Feyenoord', 'Ajax', 'Willem II', 'PSV']
    chance_of_position = {'FC Utrecht': [], 'Feyenoord': [], 'Ajax': [], 'Willem II': [], 'PSV': []}
    for place in monte_carlo_output:
        curr_place_data = monte_carlo_output[place]
        for team in teams:
            chance_of_position[team] = chance_of_position[team].__add__(
                [curr_place_data.count(team) / len(curr_place_data) * 100])
    return chance_of_position


def get_monte_carlo_output_as_chance_pool_position_as_df(output_chance_pool_position):
    """
    Zet de kans dat welk team op welke positie kan komen om naar een dataframe

    :param output_chance_pool_position: Dictionary van de kans dat welk team op welke positie kan komen
    :return: Een dataframe van de kans dat welk team op welke positie kan komen
    """
    index = ['FC Utrecht', 'Feyenoord', 'Ajax', 'Willem II', 'PSV']
    data = np.array([output_chance_pool_position['FC Utrecht'],
                     output_chance_pool_position['Feyenoord'],
                     output_chance_pool_position['Ajax'],
                     output_chance_pool_position['Willem II'],
                     output_chance_pool_position['PSV']])
    df = pd.DataFrame(
        data=data,
        columns=['1st pos', '2st pos', '3st pos', '4st pos', '5st pos', ], index=index)
    return df.sort_values(by=['1st pos'], ascending=False)


pool = {
    ('Ajax', 'Ajax'): None, ('Ajax', 'Feyenoord'): (65, 17, 18), ('Ajax', 'PSV'): (54, 21, 25), ('Ajax', 'FC Utrecht'): (74, 14, 12), ('Ajax', 'Willem II'): (78, 13, 9),
    ('Feyenoord', 'Ajax'): (30, 21, 49), ('Feyenoord', 'Feyenoord'): None, ('Feyenoord', 'PSV'): (37, 24, 39), ('Feyenoord', 'FC Utrecht'): (51, 22, 27), ('Feyenoord', 'Willem II'): (60, 21, 19),
    ('PSV', 'Ajax'): (39, 22, 39), ('PSV', 'Feyenoord'): (54, 22, 24), ('PSV', 'PSV'): None, ('PSV', 'FC Utrecht'): (62, 20, 18), ('PSV', 'Willem II'): (62, 22, 16),
    ('FC Utrecht', 'Ajax'): (25, 14, 61), ('FC Utrecht', 'Feyenoord'): (37, 23, 40), ('FC Utrecht', 'PSV'): (29, 24, 47), ('FC Utrecht', 'FC Utrecht'): None, ('FC Utrecht', 'Willem II'): (52, 23, 25),
    ('Willem II', 'Ajax'): (17, 18, 65), ('Willem II', 'Feyenoord'): (20, 26, 54), ('Willem II', 'PSV'): (23, 24, 53), ('Willem II', 'FC Utrecht'): (37, 25, 38), ('Willem II', 'Willem II'): None}


random = MersenneTwister()

amount_of_runs = 10000

output = run_monte_carlo(amount_of_runs, pool)
output_chance_of_position = get_monte_carlo_output_as_chance_pool_position(output)
output_chance_of_position_df = get_monte_carlo_output_as_chance_pool_position_as_df(output_chance_of_position)
print(output)
print(output_chance_of_position)
print(pool)

print("\n")

print(output_chance_of_position_df)

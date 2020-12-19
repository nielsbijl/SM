import math
import pandas as pd
import numpy as np
from FinalAssignment.MersenneTwister import MersenneTwister


def poisson(doelpunt, gemiddelde_doelpunt):
    return ((gemiddelde_doelpunt ** doelpunt) / math.factorial(doelpunt)) * (math.e ** (-gemiddelde_doelpunt))


def team_goals_chances(gemiddeldes):
    home_chances = {}
    away_chances = {}
    for k in range(10):
        home_chances[k] = poisson(k, gemiddeldes[0])
        away_chances[k] = poisson(k, gemiddeldes[1])
    return tuple((home_chances, away_chances))


def add_goal_chances_to_pool(curr_pool):
    new_pool = {}
    for match in curr_pool:
        if curr_pool[match]:
            new_pool[match] = team_goals_chances(curr_pool[match])
        else:
            new_pool[match] = None
    return new_pool


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


def get_goals_scored_by_team(match, pool):
    home_scored = 0
    away_scored = 0
    home_random = random.get_random_number_0_1()
    away_random = random.get_random_number_0_1()
    home_chances = pool[match][0]
    away_chances = pool[match][1]
    curr_chance_home = 0
    curr_chance_away = 0
    for i in range(len(home_chances)):
        if curr_chance_home < home_random < (home_chances[i] + curr_chance_home):
            home_scored = i
        curr_chance_home += home_chances[i]
        if curr_chance_away < away_random < (away_chances[i] + curr_chance_away):
            away_scored = i
        curr_chance_away += away_chances[i]
    return tuple((home_scored, away_scored))


random = MersenneTwister()

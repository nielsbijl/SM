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

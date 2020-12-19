import math
from FinalAssignment.RandomGenerator.MersenneTwister import MersenneTwister


def poisson(doelpunt, gemiddelde_doelpunt):
    """
    Poisson verdeling functionaliteit

    :param doelpunt: Welke hoeveelheid aan doelpunten je de kans van wilt weten
    :param gemiddelde_doelpunt: De gemiddelde doelpunten
    :return: De kans dat de hoeveelheid doelpunten gescoord worden
    """
    return ((gemiddelde_doelpunt ** doelpunt) / math.factorial(doelpunt)) * (math.e ** (-gemiddelde_doelpunt))


def team_goals_chances(gemiddeldes):
    """
    Maakt de poisson verdeling voor 0 tot 10 doelpunten met de gemiddeldes van de bijbehoordende wedstrijd
    :param gemiddeldes: tuple(gemiddelde_home, gemiddelde_away)
    :return: tuple({0 doelpunten: kans, 1 doelpunt: kans, .......}, {0 doelpunten: kans, 1 doelpunt: kans, .......})
    """
    home_chances = {}
    away_chances = {}
    for k in range(10):
        home_chances[k] = poisson(k, gemiddeldes[0])
        away_chances[k] = poisson(k, gemiddeldes[1])
    return tuple((home_chances, away_chances))


def add_goal_chances_to_pool(curr_pool):
    """
    Maakt een nieuwe pool. De tuple(gemiddelde,  gemiddelde) wordt ({0 doelpunten: kans, 1 doelpunt: kans, .......},
    {0 doelpunten: kans, 1 doelpunt: kans, .......})

    :param curr_pool: De huidige pool: {(home,
                    away): (gemiddelde_doelpunten, gemiddelde_doelpunten}, .....}
    :return: {(home, away): ({0 doelpunten: kans,
            1 doelpunt: kans, .......}, {0 doelpunten: kans, 1 doelpunt: kans, .......}), .....}
    """
    new_pool = {}
    for match in curr_pool:
        if curr_pool[match]:
            new_pool[match] = team_goals_chances(curr_pool[match])
        else:
            new_pool[match] = None
    return new_pool


def get_goals_scored_by_team(match, pool):
    """
    Hier wordt voor beide team de hoeveelheid doelpunten gegenereerd doormiddel van de Mersenne Twister random generator
    en de poisson verdeling hoeveel kans er is op hoeveel doelpunten

    :param match: (home, away)
    :param pool: {(home, away): ({0 doelpunten: kans,
            1 doelpunt: kans, .......}, {0 doelpunten: kans, 1 doelpunt: kans, .......}), .....}
    :return: tuple(doelpunten_home, doelpunten_away)
    """
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


def run_one_match_with_goals(match, pool):
    """
    Hier wordt de wedstrijd uitslag gemaakt. Er wordt opgevraagt hoeveel keer welk team gescoord heeft en komt een uitslag uit.

    :param match: (home, away)
    :param pool: {(home, away): ({0 doelpunten: kans,
            1 doelpunt: kans, .......}, {0 doelpunten: kans, 1 doelpunt: kans, .......}), .....}
    :return: De uitslag van de wedstrijd: Home|Away|"Draw"
    """
    outcome = get_goals_scored_by_team(match, pool)
    home = match[0]
    away = match[1]
    if outcome[0] == outcome[1]:
        return "Draw"
    elif outcome[0] > outcome[1]:
        return home
    else:
        return away


random = MersenneTwister()

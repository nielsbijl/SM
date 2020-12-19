import math


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


pool = {
    ('Ajax', 'Ajax'): None, ('Ajax', 'Feyenoord'): ((1.5), (1.5)), ('Ajax', 'PSV'): ((1.5), (1.5)),
    ('Ajax', 'FC Utrecht'): ((1.5), (1.5)), ('Ajax', 'Willem II'): ((1.5), (1.5)),
    ('Feyenoord', 'Ajax'): ((1.5), (1.5)), ('Feyenoord', 'Feyenoord'): None, ('Feyenoord', 'PSV'): ((1.5), (1.5)),
    ('Feyenoord', 'FC Utrecht'): ((1.5), (1.5)), ('Feyenoord', 'Willem II'): ((1.5), (1.5)),
    ('PSV', 'Ajax'): ((1.5), (1.5)), ('PSV', 'Feyenoord'): ((1.5), (1.5)), ('PSV', 'PSV'): None,
    ('PSV', 'FC Utrecht'): ((1.5), (1.5)), ('PSV', 'Willem II'): ((1.5), (1.5)),
    ('FC Utrecht', 'Ajax'): ((1.5), (1.5)), ('FC Utrecht', 'Feyenoord'): ((1.5), (1.5)),
    ('FC Utrecht', 'PSV'): ((1.5), (1.5)), ('FC Utrecht', 'FC Utrecht'): None,
    ('FC Utrecht', 'Willem II'): ((1.5), (1.5)),
    ('Willem II', 'Ajax'): ((1.5), (1.5)), ('Willem II', 'Feyenoord'): ((1.5), (1.5)),
    ('Willem II', 'PSV'): ((1.5), (1.5)), ('Willem II', 'FC Utrecht'): ((1.5), (1.5)), ('Willem II', 'Willem II'): None}

pool_with_goal_chances = add_goal_chances_to_pool(pool)


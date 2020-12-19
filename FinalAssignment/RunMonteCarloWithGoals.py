from FinalAssignment.MonteCarloWithGoals import *
from FinalAssignment.MonteCarlo import *

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

pool = add_goal_chances_to_pool(pool)

amount_of_runs = 10000

output = run_monte_carlo(amount_of_runs, pool, True)
output_chance_of_position = get_monte_carlo_output_as_chance_pool_position(output)
output_chance_of_position_df = get_monte_carlo_output_as_chance_pool_position_as_df(output_chance_of_position)

print(output_chance_of_position_df)

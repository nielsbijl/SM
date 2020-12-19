from FinalAssignment.MonteCarlo.MonteCarloWithGoals import *
from FinalAssignment.MonteCarlo.MonteCarlo import *

pool = {('Ajax', 'Ajax'): None, ('Ajax', 'Feyenoord'): (2.0, 1.55), ('Ajax', 'PSV'): (2.25, 1.35), ('Ajax', 'FC Utrecht'): (2.8, 1.95), ('Ajax', 'Willem II'): (2.35, 0.95), ('Feyenoord', 'Ajax'): (1.5, 2.1), ('Feyenoord', 'Feyenoord'): None, ('Feyenoord', 'PSV'): (1.85, 1.4500000000000002), ('Feyenoord', 'FC Utrecht'): (2.4, 2.05), ('Feyenoord', 'Willem II'): (1.95, 1.05), ('PSV', 'Ajax'): (1.35, 1.9), ('PSV', 'Feyenoord'): (1.4500000000000002, 1.4500000000000002), ('PSV', 'PSV'): None, ('PSV', 'FC Utrecht'): (2.25, 1.85), ('PSV', 'Willem II'): (1.8, 0.85), ('FC Utrecht', 'Ajax'): (1.25, 2.15), ('FC Utrecht', 'Feyenoord'): (1.35, 1.7000000000000002), ('FC Utrecht', 'PSV'): (1.6, 1.5), ('FC Utrecht', 'FC Utrecht'): None, ('FC Utrecht', 'Willem II'): (1.7, 1.1), ('Willem II', 'Ajax'): (1.0, 2.4), ('Willem II', 'Feyenoord'): (1.1, 1.9500000000000002), ('Willem II', 'PSV'): (1.35, 1.75), ('Willem II', 'FC Utrecht'): (1.9, 2.35), ('Willem II', 'Willem II'): None}
pool = add_goal_chances_to_pool(pool)

amount_of_runs = 10000

output = run_monte_carlo(amount_of_runs, pool, True)
output_chance_of_position = get_monte_carlo_output_as_chance_pool_position(output)
output_chance_of_position_df = get_monte_carlo_output_as_chance_pool_position_as_df(output_chance_of_position)

print('Monte Carlo Machine with goals:')
print(output_chance_of_position_df)

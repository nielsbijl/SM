from FinalAssignment.MonteCarlo import *

pool = {
    ('Ajax', 'Ajax'): None, ('Ajax', 'Feyenoord'): (65, 17, 18), ('Ajax', 'PSV'): (54, 21, 25), ('Ajax', 'FC Utrecht'): (74, 14, 12), ('Ajax', 'Willem II'): (78, 13, 9),
    ('Feyenoord', 'Ajax'): (30, 21, 49), ('Feyenoord', 'Feyenoord'): None, ('Feyenoord', 'PSV'): (37, 24, 39), ('Feyenoord', 'FC Utrecht'): (51, 22, 27), ('Feyenoord', 'Willem II'): (60, 21, 19),
    ('PSV', 'Ajax'): (39, 22, 39), ('PSV', 'Feyenoord'): (54, 22, 24), ('PSV', 'PSV'): None, ('PSV', 'FC Utrecht'): (62, 20, 18), ('PSV', 'Willem II'): (62, 22, 16),
    ('FC Utrecht', 'Ajax'): (25, 14, 61), ('FC Utrecht', 'Feyenoord'): (37, 23, 40), ('FC Utrecht', 'PSV'): (29, 24, 47), ('FC Utrecht', 'FC Utrecht'): None, ('FC Utrecht', 'Willem II'): (52, 23, 25),
    ('Willem II', 'Ajax'): (17, 18, 65), ('Willem II', 'Feyenoord'): (20, 26, 54), ('Willem II', 'PSV'): (23, 24, 53), ('Willem II', 'FC Utrecht'): (37, 25, 38), ('Willem II', 'Willem II'): None}


amount_of_runs = 10000

output = run_monte_carlo(amount_of_runs, pool)
output_chance_of_position = get_monte_carlo_output_as_chance_pool_position(output)
output_chance_of_position_df = get_monte_carlo_output_as_chance_pool_position_as_df(output_chance_of_position)

print("Monte Carlo Machine without goals:")
print(output_chance_of_position_df)


import pandas as pd
import numpy as np

# Define the ranges for continentalness based on the provided data
c_ranges = {
    'Mushroom Fields': np.arange(-1.2, -1.05, 0.01),
    'Deep Ocean': np.arange(-1.05, -0.455, 0.01),
    'Ocean': np.arange(-0.455, -0.19, 0.01),
    'Coast': np.arange(-0.19, -0.11, 0.01),
    'Near-inland': np.arange(-0.11, 0.03, 0.01),
    'Mid-inland': np.arange(0.03, 0.3, 0.01),
    'Far-inland': np.arange(0.3, 1.0, 0.01),
    'Far inland': np.array([1.0])  # Including 1.0 as 'Far inland' explicitly
}

# Create a DataFrame to hold the C values and corresponding biomes
biomes_list = []
for biome, values in c_ranges.items():
    for value in values:
        biomes_list.append({'C': np.round(value, 2), 'Biome': biome})

biomes_df = pd.DataFrame(biomes_list)

# Save the DataFrame to a CSV file
csv_file_path = 'biome_continentalness.csv'
biomes_df.to_csv(csv_file_path, index=False)



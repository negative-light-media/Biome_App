import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Upload CSV data
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head())  # Display the first few rows of the uploaded data

    # Display interactive scatter plot matrix
    st.write("Scatter Plot Matrix")
    sns.pairplot(data)
    st.pyplot()

data = {
    "T": ["0", "1", "2", "3"],
    "H=0": ["Ice Spikes", "Cherry Grove", "Cherry Grove", "Savanna Plateau"],
    "H=1": ["Snowy Plains", "Meadow", "Cherry Grove", "Savanna Plateau"],
    "H=2": ["Snowy Plains", "Meadow", "Forest", "Forest"],
    "H=3": ["Snowy Taiga", "Meadow", "Birch Forest", "Forest"],
    "H=4": ["Snowy Taiga", "Old Growth Pine Taiga", "Dark Forest", "Jungle"]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Pivot the DataFrame for heatmap
df_pivot = df.melt(id_vars=["T"], var_name="H", value_name="Biome").pivot("H", "T", "Biome")

# Encoding the biomes
unique_biomes = pd.unique(df_pivot.to_numpy().ravel())
biome_to_num = {biome: i for i, biome in enumerate(unique_biomes)}
df_encoded = df_pivot.replace(biome_to_num)

# The encoded DataFrame and the mapping dictionary
print(df_encoded)
print(biome_to_num)

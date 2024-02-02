import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pyvista as pv

st.set_page_config(layout="wide")
# Set up the title of the app
st.title('Minecraft Biome Visualizer')

# Description
st.write("""
This app visualizes the biome distribution in Minecraft based on various parameters like temperature, humidity, continentalness, erosion, and weirdness.
""")

st.header("Example Data")

col1, col2 = st.columns(2)

with col1:
    st.write("Plateaus+ Biome Data")
    data = {
        "T": ["0", "1", "2", "3"],
        "H=0": ["Ice Spikes", "Cherry Grove", "Cherry Grove", "Savanna Plateau"],
        "H=1": ["Snowy Plains", "Meadow", "Cherry Grove", "Savanna Plateau"],
        "H=2": ["Snowy Plains", "Meadow", "Forest", "Forest"],
        "H=3": ["Snowy Taiga", "Meadow", "Birch Forest", "Forest"],
        "H=4": ["Snowy Taiga", "Old Growth Pine Taiga", "Dark Forest", "Jungle"]
    }
    df = pd.DataFrame(data)
    df_pivot = df.melt(id_vars=["T"], var_name="H", value_name="Biome").pivot("H", "T", "Biome")
    st.write(df_pivot)

with col2:
    # Encoding the biomes
    unique_biomes = pd.unique(df_pivot.to_numpy().ravel())
    biome_to_num = {biome: i for i, biome in enumerate(unique_biomes)}
    df_encoded = df_pivot.replace(biome_to_num)

    try:
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.heatmap(df_encoded, annot=df_pivot.to_numpy(), fmt="", cmap="viridis", ax=ax)
        ax.set_title("Plateaus+ Biome Distribution")
        ax.set_xlabel("Temperature (T)")
        ax.set_ylabel("Humidity (H)")
        st.pyplot(fig)
    except Exception as e:
        st.error(f"An error occurred: {e}")



        

# Footer
st.write("Developed by : ")

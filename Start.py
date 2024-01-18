import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the title of the app
st.title('Minecraft Biome Visualizer')

# Description
st.write("""
This app visualizes the biome distribution in Minecraft based on various parameters like temperature, humidity, continentalness, erosion, and weirdness.
""")

# Upload CSV data
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head())  # Display the first few rows of the uploaded data

    # Display interactive scatter plot matrix
    st.write("Scatter Plot Matrix")
    sns.pairplot(data)
    st.pyplot()

    # Additional visualizations and interactive elements can be added here

# Footer
st.write("Developed by [Your Name]")

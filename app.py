%%writefile app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set up the title and description of the app
st.title("Mock Data Analysis App")
st.write("This app demonstrates data analysis using mock data.")

# Generate mock data
st.subheader("Generated Mock Data")

# Create a DataFrame with random data
np.random.seed(42)  # For reproducibility
mock_data = pd.DataFrame({
    'A': np.random.randint(0, 100, 100),  # Random integers between 0 and 100
    'B': np.random.normal(50, 15, 100),   # Random numbers from a normal distribution
    'C': np.random.choice(['Category 1', 'Category 2', 'Category 3'], 100)  # Random categorical data
})

# Show the generated data
st.write(mock_data)

# Show basic statistics
st.subheader("Summary Statistics")
st.write(mock_data.describe())

# Data visualization
st.subheader("Data Visualization")

# Select column for visualization
column = st.selectbox("Select a numeric column to visualize", mock_data.select_dtypes(include=[np.number]).columns)

# Plot histogram for selected numeric column
st.write(f"Histogram of {column}")
fig, ax = plt.subplots()
ax.hist(mock_data[column].dropna(), bins=20, color='skyblue')
st.pyplot(fig)

# Display value counts for categorical column
st.subheader("Categorical Data Distribution")
st.bar_chart(mock_data['C'].value_counts())

import streamlit as st
import pandas as pd
from CPI import df

st.set_page_config(page_title="CPI Graph", page_icon="📈", layout="centered")

st.title("CPI Graph")
#st.write("This is a separate page.")

# Identify year column (Column 0)
year_col = df.columns[0]

# Get minimum and maximum years
min_year = int(df[year_col].min())
max_year = int(df[year_col].max())

# Range slider for years
selected_years = st.slider(
    "Select Year Range:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)  # Default: full range
)

# Filter DataFrame by selected year range
filtered_df = df[
    (df[year_col] >= selected_years[0]) & (df[year_col] <= selected_years[1])
]

# Set the year column as index so it becomes the X-axis
filtered_df = filtered_df.set_index(year_col)

# Select metric column to plot (excluding Column 0)
y_columns = filtered_df.columns.tolist()
selected_col = st.selectbox("Select month to plot:", y_columns)

# Plot
st.line_chart(filtered_df[selected_col])
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Bar Chart Example")

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 12, 37]
}
df = pd.DataFrame(data)

# Show dataframe
st.subheader("Data")
st.dataframe(df)

# Plot bar chart
st.subheader("Bar Chart")
fig, ax = plt.subplots()
ax.bar(df['Category'], df['Values'], color='skyblue')
ax.set_xlabel("Category")
ax.set_ylabel("Values")
ax.set_title("Sample Bar Chart")

# Display plot
st.pyplot(fig)
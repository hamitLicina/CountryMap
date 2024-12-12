import plotly.express as px
import pandas as pd  # Import pandas to create a DataFrame

# Prompt the user for a country name
country = input("Enter the country name: ")

# Create a DataFrame with the country name and value
data = pd.DataFrame({
    'Country': [country],
    'Values': [100]  # Example value, can be replaced with real data
})

# Generate the choropleth map
fig = px.choropleth(
    data_frame=data,
    locations='Country',             # Column with country names
    locationmode='country names',    # Match country names
    color='Values',                  # Column for color shading
    color_continuous_scale='Inferno', # Color scale
    title=f'Map of {country}'        # Title of the map
)

# Display the map
fig.show()

from geopy.geocoders import Nominatim
import plotly.express as px
import pandas as pd

# Step 1: Initialize geolocator
geolocator = Nominatim(user_agent="geoapi")

# Step 2: Get user input for multiple locations
print("Enter locations (e.g., city names, addresses, or coordinates).")
print("Type 'done' when you are finished.\n")

locations = []
while True:
    location_input = input("Enter a location: ")
    if location_input.lower() == 'done':
        break
    locations.append(location_input)

# Step 3: Geocode each location
location_data = []
for loc in locations:
    try:
        location = geolocator.geocode(loc)
        if location:
            latitude = location.latitude
            longitude = location.longitude
            country = location.address.split(",")[-1].strip()
            location_data.append({
                'location_name': f"{loc} ({country})",
                'latitude': latitude,
                'longitude': longitude
            })
            print(f"✅ Found: {loc} -> {location.address}")
        else:
            print(f"⚠️ Location not found: {loc}")
    except Exception as e:
        print(f"Error with {loc}: {e}")

# Check if we have any valid data
if location_data:
    # Step 4: Create a DataFrame
    df = pd.DataFrame(location_data)

    # Step 5: Plot the locations on a map
    fig = px.scatter_geo(
        df,
        lat='latitude',
        lon='longitude',
        text='location_name',
        title="Locations Map",
        projection='natural earth'
    )

    # Step 6: Save the map as an HTML file
    fig.write_html("locations_map.html")
    print("\n🌍 Map saved as 'locations_map.html'. Open it in your browser!")

    # Step 7: Display the map
    fig.show()
else:
    print("\nNo valid locations to plot.")

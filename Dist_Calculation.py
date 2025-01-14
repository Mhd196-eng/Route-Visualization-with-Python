import folium
import webbrowser

# Define the coordinates for Academic City KHDA and Global Village
academic_city_coords = [25.214441, 55.417405]  # Latitude, Longitude of Academic City KHDA
global_village_coords = [25.058700, 55.317360]  # Latitude, Longitude of Global Village

# Define the coordinates for E311 and E611 routes
# Example coordinates for route E311 (this would be a rough representation of the path on E311)
e311_coords = [
    [25.214441, 55.417405],  # Start at Academic City KHDA
    [25.180000, 55.430000],  # Intermediate point on E311
    [25.100000, 55.390000],  # Another intermediate point
    [25.058700, 55.317360]   # End at Global Village
]

# Example coordinates for route E611 (this would be a rough representation of the path on E611)
e611_coords = [
    [25.214441, 55.417405],  # Start at Academic City KHDA
    [25.150000, 55.440000],  # Intermediate point on E611
    [25.080000, 55.380000],  # Another intermediate point
    [25.058700, 55.317360]   # End at Global Village
]

# Create a folium map centered between Academic City KHDA and Global Village
map_center = [(academic_city_coords[0] + global_village_coords[0]) / 2,
              (academic_city_coords[1] + global_village_coords[1]) / 2]
map_route = folium.Map(location=map_center, zoom_start=13)

# Plot the E311 route (green)
folium.PolyLine(
    locations=e311_coords,
    color="green",
    weight=5,
    opacity=0.8,
    tooltip="Route via E311"
).add_to(map_route)

# Plot the E611 route (red)
folium.PolyLine(
    locations=e611_coords,
    color="red",
    weight=5,
    opacity=0.8,
    tooltip="Route via E611"
).add_to(map_route)

# Add markers for the origin (Academic City KHDA) and destination (Global Village)
folium.Marker(
    academic_city_coords,
    tooltip="Academic City KHDA",
    icon=folium.Icon(color="blue")
).add_to(map_route)

folium.Marker(
    global_village_coords,
    tooltip="Global Village",
    icon=folium.Icon(color="red")
).add_to(map_route)

# Save the map to an HTML file
map_route.save("academic_city_to_global_village.html")
print("Map saved as 'academic_city_to_global_village.html'. Opening in browser...")

# Automatically open the map in the browser
webbrowser.open("academic_city_to_global_village.html")

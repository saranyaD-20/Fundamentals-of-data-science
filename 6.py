import pandas as pd

# Assuming property_data is your DataFrame or load it from CSV
# property_data = pd.read_csv("property_data.csv")

# Example DataFrame creation (replace with your actual data loading)
property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4, 5],
    'location': ['A', 'B', 'A', 'C', 'B'],
    'number_of_bedrooms': [3, 4, 5, 3, 4],
    'area_in_square_feet': [1500, 1800, 2000, 1700, 2200],
    'listing_price': [200000, 250000, 300000, 220000, 280000]
})

# 1. Average listing price of properties in each location
average_price_by_location = property_data.groupby('location')['listing_price'].mean().reset_index()
average_price_by_location.columns = ['location', 'average_listing_price']

# 2. Number of properties with more than four bedrooms
properties_more_than_four_bedrooms = property_data[property_data['number_of_bedrooms'] > 4]
number_of_properties_more_than_four_bedrooms = pd.DataFrame({'number_of_properties_more_than_four_bedrooms': [len(properties_more_than_four_bedrooms)]})

# 3. Property with the largest area
property_with_largest_area = property_data.loc[property_data['area_in_square_feet'].idxmax()].to_frame().transpose()

# Printing the results
print("Average listing price of properties in each location:")
print(average_price_by_location)
print()

print("Number of properties with more than four bedrooms:")
print(number_of_properties_more_than_four_bedrooms)
print()

print("Property with the largest area:")
print(property_with_largest_area)

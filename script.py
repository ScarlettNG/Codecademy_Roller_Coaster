# Import internal library
import codecademylib3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 1 
# Import necessary libraries
wood= pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
# load rankings data
print(wood.head())
# load rankings data
print(steel.head())
# 2
# Create a function to plot rankings over time for 1 roller coaster
def rank_year (name, park):
  dfwood = wood[(wood['Name'] == name) & (wood['Park'] == park)]
  plt.plot(dfwood['Year of Rank'], dfwood['Rank'])
  plt.ylabel('Rank')
  plt.xlabel('Year')
  plt.title("Roller Coaster Ranking Over Time")
  plt.legend([name], loc = 1)
  plt.show()
  
print(rank_year('El Toro', 'Six Flags Great Adventure'))
# 3
# Create a plot of El Toro ranking over time
def plot_two_coasters_ranking(name1, park1, name2, park2, rankings_df):
    # Filter the DataFrame for the first roller coaster
    coaster1 = rankings_df[(rankings_df['Name'] == name1) & (rankings_df['Park'] == park1)]
    
    # Filter the DataFrame for the second roller coaster
    coaster2 = rankings_df[(rankings_df['Name'] == name2) & (rankings_df['Park'] == park2)]
    
    # Plot the rankings over time for both roller coasters
    plt.plot(coaster1['Year of Rank'], coaster1['Rank'], label=name1)
    plt.plot(coaster2['Year of Rank'], coaster2['Rank'], label=name2)
    
    # Invert the y-axis to show rank 1 at the top
    plt.gca().invert_yaxis()
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.title('Ranking of Two Roller Coasters Over Time')
    plt.legend()
    
    # Show the plot
    plt.show()

# Call the function with "El Toro" and "Boulder Dash" and the wood ranking DataFrame
plot_two_coasters_ranking('El Toro', 'Six Flags Great Adventure', 'Boulder Dash', 'Lake Compounce', wood)


# Create a plot of El Toro and Boulder dash hurricanes
# 4
# Create a function to plot top n rankings over time
# Create a plot of top n rankings over time
def plot_top_n_ranking(n, rankings_df):
    # Filter the DataFrame to include only the top n ranked roller coasters
    top_n_rankings = rankings_df[rankings_df["Rank"] <= n]
    
    # Create a figure
    plt.figure(figsize=(10, 6))
    
    # Iterate through each unique roller coaster in the filtered DataFrame
    for coaster in set(top_n_rankings["Name"]):
        # Filter the DataFrame for the current roller coaster
        coaster_rankings = top_n_rankings[top_n_rankings["Name"] == coaster]
        
        # Plot the ranking over time
        plt.plot(coaster_rankings["Year of Rank"], coaster_rankings["Rank"], label=coaster)
    
    # Invert the y-axis to show rank 1 at the top
    plt.gca().invert_yaxis()
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.title(f'Top {n} Roller Coasters Ranking Over Time')
    plt.legend()
    
    # Show the plot
    plt.show()

# Call the function with a value for n and the wood ranking DataFrame
plot_top_n_ranking(5, wood)

# 5
# load roller coaster data
rollers = pd.read_csv("roller_coasters.csv")
rollers["num_inversions"] = rollers["num_inversions"].astype(float)
print(rollers.head(5))
# 6
# Create a function to plot histogram of column values

def hist_num_visual(column_name, df):
  plt.close("all")
  #Drop missing values
  data = df[column_name].dropna()
  plt.hist(data, bins = 20, edgecolor="black")
  plt.gca().invert_xaxis()
  plt.xlabel(column_name)
  plt.ylabel("Frequency")
  plt.title(f"Histogram of {column_name}")
  plt.show()  
# Create histogram of roller coaster speed
hist_num_visual("speed", rollers)
# Create histogram of roller coaster length
hist_num_visual("length", rollers)
# Create histogram of roller coaster number of inversions
hist_num_visual("num_inversions", rollers)
# Create a function to plot histogram of height values


# Define the function to plot a histogram of height values
def plot_height_histogram(df):
    # Drop missing values in the height column
    heights = df['height'].dropna()
    
    # Create the histogram
    plt.hist(heights, bins=20, edgecolor='black')
    
    # Add labels and title
    plt.xlabel('Height (meters)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Roller Coaster Heights')
    
    # Show the plot
    plt.show()
# Create a histogram of roller coaster height
plot_height_histogram(rollers)
# 7
# Create a function to plot inversions by coaster at park
def num_inversions(park, df):
    df_park = df[df['park']==park]
    plt.clf()
    plt.bar(df_park['name'], df_park['num_inversions'], color='purple')
    plt.xlabel('Coaster at ' + str(park))
    plt.ylabel('Number of Inversions')
    plt.xticks(rotation=90)
    return plt.show()
num_inversions("Goudurix", rollers)
# 8
# Create a function to plot a pie chart of status.operating
def plot_coaster_status_pie(df):
    # Count the number of operating and closed roller coasters
    operating_count = df[df['status'] == 'status.operating'].shape[0]
    closed_count = df[df['status'] == 'status.closed.definitely'].shape[0]
    
    # Data for the pie chart
    status_counts = [operating_count, closed_count]
    status_labels = ['Operating', 'Closed']
    
    # Create the pie chart
    plt.pie(status_counts, labels=status_labels, autopct='%0.1f%%', startangle=90)
    
    # Add a title
    plt.title('Operating vs Closed Roller Coasters')
    
    # Show the plot
    plt.show()

# Call the function with the roller coaster DataFrame
plot_coaster_status_pie(rollers)


# Create pie chart of roller coasters
def plot_scatter(df, column1, column2):
    # Create the scatter plot
    plt.clf()
    plt.scatter(df[column1], df[column2])
    
    # Add labels and title
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.title(f'Scatter Plot of {column1} vs {column2}')
    
    # Show the plot
    plt.show()

# Call the function with the roller coaster DataFrame and two column names
plot_scatter(rollers, 'height', 'speed')
# 9
# Create a function to plot scatter of any two columns
def plot_seating_type_popularity(df):
  seating_count = df["seating_type"].value_counts()
  seating_count.plot(kind="bar")
  plt.xticks(rotation=45)
  plt.xlabel("Seating Type")
  plt.ylabel("Count")
  plt.title("Popularity of Roller Coaster Seating Types")
  plt.show()

plot_seating_type_popularity(rollers)
# Create a function to plot scatter of speed vs height

def plot_seating_type_comparison(df, column):
  df.boxplot(column=column, by="seating_type", grid=False)
  plt.xlabel("Seating Type")
  plt.ylabel(column.capitalize())
  plt.title(f'{column.capitalize()} by Seating Type')
  plt.suptitle("")
  plt.show()
plot_seating_type_comparison(rollers, 'height')
plot_seating_type_comparison(rollers, 'speed')
plot_seating_type_comparison(rollers, 'length')

# Create a scatter plot of roller coaster height by speed
plt.clf()
plt.scatter(rollers.height, rollers.speed)
plt.show()

def plot_manufacturer_specialties(df, column):
    manufacturer_means = df.groupby('manufacturer')[column].mean().sort_values()
    manufacturer_means.plot(kind='bar')
    plt.xlabel('Manufacturer')
    plt.ylabel(f'Average {column.capitalize()}')
    plt.title(f'Average {column.capitalize()} by Manufacturer')
    plt.show()

plot_manufacturer_specialties(rollers, 'speed')
plot_manufacturer_specialties(rollers, 'height')
plot_manufacturer_specialties(rollers, 'num_inversions')

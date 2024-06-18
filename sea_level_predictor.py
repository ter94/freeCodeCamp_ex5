import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', edgecolor='k')
    plt.title('CSIRO Adjusted Sea Level Over Time')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (inches)')
    plt.grid(True)
    plt.show()

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(data['Year'].min(), 2051)
    sea_levels_predicted = intercept + slope * years_extended
    
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', edgecolor='k', label='Observed data')
    plt.plot(years_extended, sea_levels_predicted, color='red', label='Line of best fit (all data)')
    plt.title('CSIRO Adjusted Sea Level Over Time with Line of Best Fit')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (inches)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Create second line of best fit
    recent_data = data[data['Year'] >= 2000]

    recent_slope, recent_intercept, recent_r_value, recent_p_value, recent_std_err = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_recent_extended = np.arange(2000, 2051)
    sea_levels_recent_predicted = recent_intercept + recent_slope * years_recent_extended
  
    # Add labels and title
    
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', edgecolor='k', label='Observed data')
    plt.plot(years_extended, sea_levels_predicted, color='red', label='Line of best fit (all data)')
    plt.plot(years_recent_extended, sea_levels_recent_predicted, color='green', linestyle='--', label='Line of best fit (2000 onwards)')
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    plt.grid(True)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

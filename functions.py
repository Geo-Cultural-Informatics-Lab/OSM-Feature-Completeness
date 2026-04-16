# Libraries
import pandas as pd
import geopandas as gpd
import numpy as np
import os
import json
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D


## Functions

# API get road lengths function
def get_len(bounds, filter="type:way and highway=*", time="2008-01-01/2025-01-01/P1M", path=None, filename=None):
    '''
    A function that extracts aggregated length of roads (highway tags) in a specific extent polygon from OSM using the Ohsome API, and returns all data in a json format.

    The function recieves 3 strings:
        1) **bounds** - bbox parameter, including bottom right and top left geographic coordinates
        2) **filter** - filter parameter, defaultly extracting all highway tags from way objects
        3) **time** - ISO-8621 timestamp. Defaultly extracting all data between 01/2008-01/2025 in tri-monthly intervals
    
    If the user wants to save the data, there are two additional parameters:
        1) **path** - string to path on computer
        2) **filename** - string with requested filename

    Dependencies:
    * requests
    * json
    * os
    * pandas as pd
    '''
    # Ensuring needed libraries are imported
    import requests
    import json
    import os
    import pandas as pd

    url = "https://api.ohsome.org/v1/elements/length" # URL for API

    # Defining parameters for extract
    params = {
    "bboxes": bounds,
    "filter": filter,
    "time": time,
    "format": "json"
    }

    response = requests.get(url, params=params) # Creating request

    if response.status_code == 200:
        print("Succesfully extracted lengths")
        data = response.json() # data extract

        # Saving extract to file if requested:
        if path and filename:
            os.makedirs(path, exist_ok=True)  # create directory if it doesn't exist
            file_path = os.path.join(path, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Data saved to {file_path}")

        return pd.json_normalize(data['result'])
    
    # Print errors if recieved for debugging 
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# API count road number
def get_count(bounds, filter="type:way and highway=*", time="2008-01-01/2025-01-01/P1M", path=None, filename=None):
    '''
    A function that extracts cummulative number of roads (highway tags) in a specific extent polygon from OSM using the Ohsome API, and returns all data in a json format.

    The function recieves 3 strings:
        1) **bounds** - bbox parameter, including bottom right and top left geographic coordinates
        2) **filter** - filter parameter, defaultly extracting all highway tags from way objects
        3) **time** - ISO-8621 timestamp. Defaultly extracting all data between 01/2008-01/2025 in monthly intervals
    
    If the user wants to save the data, there are two additional parameters:
        1) **path** - string to path on computer
        2) **filename** - string with requested filename

    Dependencies:
    * requests
    * json
    * os
    * pandas as pd
    '''
    # Ensuring needed libraries are imported
    import requests
    import json
    import os
    import pandas as pd

    url = "https://api.ohsome.org/v1/elements/count" # URL for API

    # Defining parameters for extract
    params = {
    "bboxes": bounds,
    "filter": filter,
    "time": time,
    "format": "json"
    }

    response = requests.get(url, params=params) # Creating request

    if response.status_code == 200:
        print("Succesfully extracted counts")
        data = response.json() # data extract

        # Saving extract to file if requested:
        if path and filename:
            os.makedirs(path, exist_ok=True)  # create directory if it doesn't exist
            file_path = os.path.join(path, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Data saved to {file_path}")

        return pd.json_normalize(data['result'])
    
    # Print errors if recieved for debugging 
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
    
# API get bulding area function
def get_area(bounds, filter="type:way and building=*", time="2008-01-01/2025-01-01/P1M", path=None, filename=None):
    '''
    A function that extracts aggregated area of buildings (highway tags) in a specific extent polygon from OSM using the Ohsome API, and returns all data in a json format.

    The function recieves 3 strings:
        1) **bounds** - bbox parameter, including bottom right and top left geographic coordinates
        2) **filter** - filter parameter, defaultly extracting all highway tags from way objects
        3) **time** - ISO-8621 timestamp. Defaultly extracting all data between 01/2008-01/2025 in monthly intervals
    
    If the user wants to save the data, there are two additional parameters:
        1) **path** - string to path on computer
        2) **filename** - string with requested filename
    
    Dependencies:
    * requests
    * json
    * os
    * pandas as pd
    '''
    # Ensuring needed libraries are imported
    import requests
    import json
    import os
    import pandas as pd

    url = "https://api.ohsome.org/v1/elements/area" # URL for API

    # Defining parameters for extract
    params = {
    "bboxes": bounds,
    "filter": filter,
    "time": time,
    "format": "json"
    }

    response = requests.get(url, params=params) # Creating request

    if response.status_code == 200:
        print("Succesfully extracted areas")
        data = response.json() # data extract

        # Saving extract to file if requested:
        if path and filename:
            os.makedirs(path, exist_ok=True)  # create directory if it doesn't exist
            file_path = os.path.join(path, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Data saved to {file_path}")

        return pd.json_normalize(data['result'])
    
    # Print errors if recieved for debugging 
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# API count road density
def get_density(bounds, filter="type:way and highway=*", type="length", time="2008-01-01/2025-01-01/P1M", path=None, filename=None):
    '''
    A function that extracts the density of some type (roads, i.e. highway tags as default) in a specific extent polygon from OSM using the Ohsome API, and returns all data in a json format.

    The function recieves 4 strings:
        1) **bounds** - bbox parameter, including bottom right and top left geographic coordinates
        2) **filter** - filter parameter, defaultly extracting all highway tags from way objects
        3) **type** - type of density required from API: `length` (default) or `area`
        4) **time** - ISO-8621 timestamp. Defaultly extracting all data between 01/2008-01/2025 in monthly intervals
    
    If the user wants to save the data, there are two additional parameters:
        1) **path** - string to path on computer
        2) **filename** - string with requested filename

    Dependencies:
    * requests
    * json
    * os
    * pandas as pd
    '''
    # Ensuring needed libraries are imported
    import requests
    import json
    import os
    import pandas as pd

    url = f"https://api.ohsome.org/v1/elements/{type}/density" # URL for API

    # Defining parameters for extract
    params = {
    "bboxes": bounds,
    "filter": filter,
    "time": time,
    "format": "json"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None

    data = response.json()

    # Save JSON if requested
    if path and filename:
        os.makedirs(path, exist_ok=True)
        file_path = os.path.join(path, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Data saved to {file_path}")

    # Extract numeric density
    if "result" in data and len(data["result"]) > 0:
        return data["result"][0].get("value", None)
    return None

# Fit addition from cummulative values
def get_add_from_cum(df):
    '''
    A function that calculates the addition of data in an OSM extent from the cummulative values extracted using the OHSOME API.
    The function receives a Pandas DataFrame with a cummulative value column and returns the same DataFrame with a new calculated column.

    This function requires an import of the `Pandas` library present in the kernel of the worksapce.

    Dependencies:
    * pandas
    '''
    # Renaming value column to deal with ambiguity
    df.rename(columns={'value': 'cummulative_value'}, inplace=True)

    # Calculating addition values
    df['added_value'] = df['cummulative_value'].diff() # Subtracting the previous cummulative sum from each current cummulative sum
    df['added_value'] = df['added_value'].fillna(df['cummulative_value']) # Fixing potential Na values in first rows

    # Return updated dataframe
    return df

# Generate a mixed transformation ratio of cumulative size divided by cumulative counts
def semi_norm_mix_transform(count_gdf, size_gdf, alpha=0.3, time_thresh=2, saturation_thresh=1.5, return_full=False):
    '''
    Receives two GeoDataFrames (assumes identical timestamps and geometry):
    1) A cumulative count of added features by timestamps
    2) A cumulative value of all features by timestamps

    The function converts timestamp to actual datetime format, transforms the values to a mixed normalized percentage of added value (length / area) per each added unit.
    After that, the function applies the following statistical test:
    
    `If all cumulative change percentage is below some alpha (default: 30%) for a stable time period (default: 2 years) without a large absolute addition (default: 150% more than saturation point), the data is considered saturated.`
    
    For possible saturated data, the function computes the saturation point (1st month in stable period) and calculates cumulative percentage up to that point.

    In all cases, the output is a DataFrame:
    * If not saturated --> the merged DataFrame, with updated timstamps and calculations.
    * If saturated --> can either return only values up to the saturation point + maximum value (default) or return the entire data with reference to the saturation point.
    
    Dependencies:
    * pandas as pd
    '''
    # Fix timestamp
    count_gdf['timestamp'] = pd.to_datetime(count_gdf['timestamp'])
    size_gdf['timestamp'] = pd.to_datetime(size_gdf['timestamp'])

    # Sort both DataFrames by timestamp and reset index for proper alignment
    count_gdf = count_gdf.sort_values('timestamp').reset_index(drop=True)
    size_gdf = size_gdf.sort_values('timestamp').reset_index(drop=True)

    # Merge Dataframes
    gdf = count_gdf.copy().rename(columns={'value' : 'count'}) # Copy DF and rename count column
    gdf['size'] = size_gdf['value'] # Append size column
    
    # Transform values
    gdf['cumulative_percentage'] = gdf['size'] / gdf['count']
    gdf['cumulative_percentage'] = gdf['cumulative_percentage'].fillna(0) # Deal with periods without addition
    gdf['normalized_cum_per'] = gdf['cumulative_percentage'] / gdf['cumulative_percentage'].max()

    # Apply completeness test for level alpha
    gdf['test'] = (gdf['normalized_cum_per'] < alpha) # Boolean term for each date in data

    ## Iterate backwards in data to find stability period
    i = -1 # Running index (from end)
    test = gdf['test'].iat[i] # Running boolean test answer (from end)
    while test:
        try: # Update index
            i -= 1
            test = gdf['test'].iat[i]
        
        except IndexError: # Break loop if at first index
            break
    
    if i == -1:
        # Deal with last value percentage being greater than alpha (i.e. no stable period)
        print('Data incomplete: no stable period')
        return gdf
    
    stable = gdf.iloc[i+1:].copy() # Extract stable period

    ## If stable period shorter than given time threshold --> data is incomplete
    if (stable['timestamp'].max() - stable['timestamp'].min()) < pd.Timedelta(days=time_thresh*365):
        print('Data incomplete: stable period shorter than threshold')
        return gdf

    ## For complete data
    else:
        # Extract saturated value
        saturation_point = stable.iloc[0]

        # Calculate saturation levels
        gdf['percentage_until_saturation'] = gdf['count'] / saturation_point['count']
        
         # Extract emprical maximal value
        real_max = gdf.iloc[-1]
      
        # Verify small absolute addition
        if (real_max['percentage_until_saturation'] >= saturation_thresh):
            print('Data incomplete: stable addition larger than threshold')
            return gdf
        
        # Extract 80% saturation timestamp
        saturated_time = gdf[gdf['percentage_until_saturation'] >= 0.8]['timestamp'].iloc[0]
        print(f'Date complete: Polygon 80% saturated at {saturated_time}')

        ### Return entire gdf if requested
        if return_full:
            return gdf
        
        ### Return compact gdf (default)
        else:
            # Filter data until saturation
            saturated = gdf.iloc[:i+1].copy()
        
            # Concatenate empirical maximal value
            saturated = pd.concat([saturated,
                                   pd.DataFrame([real_max])],
                                   ignore_index=True)       
            return saturated
        
# Wrapper function for queries for event sample data set
def wrap_api_query(row, query, filter='type:way and highway=*', time='2008-01-01/2025-01-01/P1M'):
    '''
    A wrapper function to implement API queries on a dataset rowwise. The function keeps identifier columns per each extracted data, i.e. the index in the original dataframe, the event type and the percentage of said event in the bounding box.
    
    Dependencies:
    * pandas
    '''
    # Implement API extract function
    if query == 'count':
        df = get_count(row['bbox'], filter=filter, time=time)
    elif query == 'length':
        df = get_len(row['bbox'], filter=filter,time=time)
    elif query == 'area':
        df = get_area(row['bbox'], filter=filter,time=time)
    else:
        raise ValueError(f"Unknown query type: {query}")
    
    # Append identifier columns
    df['idx'] = row.name # one-to-one index
    df['event_type'] = row['event_type'] # event type
    df['event_percentage'] = row['event_percentage'] # percentage of event in bbox

    return df

# Function to create plots for samples
def generate_measure_sample_plot(df_list,
                                 subtitle='incomplete roads data | complete building data\n(large scale events, alpha = 0.1)',
                                 n=6,
                                 length=True,
                                 logscale=True):
    '''
    Function to create a subsample plot of features.
    It allows for any number of plots, but iterates by default on 6, and all margins fit this display.
    The function enables to choose two parameters to modify the output:

    1. length / area: if `length` is defined true (default), the plot will update the axis and column labels to show road lengths; if defined false, these labels will be for building area in sq. meters.
    2. log scale / original scale: if `logscale` is defined true (default), the count and size values will be transformed using a log function; if false, it will keep the original scale.
    
    Dependencies:
    * pandas as pd
    * matplotlib.pyplot as plt
    * matplotlib.dates as mdates
    * matplotlib.lines import Line2D
    '''
    # General parameters
    fig, axes = plt.subplots(nrows=n, ncols=3, figsize=(20, 24))

    # Column titles in plot
    if length:
        column_titles = ['Length (meter) per count percentage', 'Feature Count', 'Feature Length']
    else:
        column_titles = ['Area (sq. meter) per count percentage', 'Feature Count', 'Feature Length']

    # Plot
    for i, df in enumerate(df_list[0:n]):
        for j in range(3):
            ax = axes[i, j]
            # Plot 1: saturation percentage
            if j == 0:
                # Saturated values:
                if 'percentage_until_saturation' in df.columns:
                    sat = (df['percentage_until_saturation'] >= 0.8).idxmax()
                    df_plt = df.iloc[:sat + 1]
                    ax.plot(df_plt['timestamp'], df_plt['percentage_until_saturation'], linestyle='-', color='g')

                    # Adding saturation point
                    saturation = df[df['percentage_until_saturation'] >= 0.8].iloc[0]
                    ax.scatter(saturation['timestamp'], saturation['percentage_until_saturation'], color='black', zorder=5, label='80% saturation')
                    ax.annotate(pd.to_datetime(saturation['timestamp']).strftime('%b %Y'), xy=(saturation['timestamp'], saturation['percentage_until_saturation']),
                                xytext=(5, -10), textcoords='offset points', fontsize=8, color='black')

                # Un-saturated values:      
                else:
                    ax.plot(df['timestamp'], df['normalized_cum_per'], linestyle='-', color='r')
                ax.set_ylabel('Transformed Value', weight='bold')
                if i == (n-1):
                    # Only bottom of each column
                    ax.set_xlabel('Timestamp', weight='bold')
                ax.tick_params(axis='x', rotation=45)
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
                ax.grid(True)

            # Plot 2: feature counts
            elif j == 1:
                if logscale:
                    ax.plot(df['timestamp'], np.log(df['count']), linestyle='-', color='b')
                    ax.set_ylabel('Count (cumulative, log scale)', weight='bold')
                else:
                    ax.plot(df['timestamp'], df['count'], linestyle='-', color='b')
                    ax.set_ylabel('Count (cumulative)', weight='bold')
                if i == (n-1):
                    # Only bottom of each column
                    ax.set_xlabel('Timestamp', weight='bold')
                ax.tick_params(axis='x', rotation=45)
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
                ax.grid(True)

            # Plot 3: feature lengths
            elif j == 2:
                if logscale:
                    ax.plot(df['timestamp'], np.log(df['size']), linestyle='-', color='purple')
                    if length:
                        ax.set_ylabel('Length (cumulative, log scale)', weight='bold')
                    else:
                        ax.set_ylabel('Area (cumulative, log scaled)', weight='bold')
                else:
                    ax.plot(df['timestamp'], df['size'], linestyle='-', color='purple')
                    if length:
                        ax.set_ylabel('Length (cumulative)', weight='bold')
                    else:
                        ax.set_ylabel('Area (cumulative)', weight='bold')
                if i == (n-1):
                    # Only bottom of each column
                    ax.set_xlabel('Timestamp', weight='bold')
                ax.tick_params(axis='x', rotation=45)
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
                ax.grid(True)
        
            # Set titles per each column
            if i == 0:
                axes[0, j].set_title(column_titles[j], fontsize=18, fontweight = 'bold')

    # Set legend
    if length:
        legend_elements = [
            Line2D([0], [0], color='b', lw=2, label='Cumulative feature count'),
            Line2D([0], [0], color='purple', lw=2, label='Cumulative feature lengths'), 
            Line2D([0], [0], color='r', lw=2, label='Mixed semi-normalized (length / count)'),
            Line2D([0], [0], color='g', lw=2, label='Percentage until saturation'),
            Line2D([0], [0], marker='o', color='black', linestyle='', label='80% saturation time')
        ]
    
    else:
        legend_elements = [
            Line2D([0], [0], color='b', lw=2, label='Cumulative feature count'),
            Line2D([0], [0], color='purple', lw=2, label='Cumulative feature areas'), 
            Line2D([0], [0], color='r', lw=2, label='Mixed semi-normalized (area / count)'),
            Line2D([0], [0], color='g', lw=2, label='Percentage until saturation'),
            Line2D([0], [0], marker='o', color='black', linestyle='', label='80% saturation time')
        ]

    legend = fig.legend(
        handles=legend_elements,
        loc='upper center',
        ncol=5,
        bbox_to_anchor=(0.5, -0.005),
        fontsize=12,
        frameon=True,
        title='Legend',
        title_fontsize=13
    )

    legend.get_frame().set_edgecolor('black')
    legend.get_title().set_fontweight('bold')

    # Assign title
    if length:
        fig.text(0.5, 1, f'Mixed Semi-normalized Transform for Road lengths (meter) Cumulative Addition', fontsize=24, fontweight='bold', ha='center')
    else:
        fig.text(0.5, 1, f'Mixed Semi-normalized Transform for Building areas (sq. meter) Cumulative Addition', fontsize=24, fontweight='bold', ha='center')
    fig.text(0.5, 0.97, subtitle, fontsize=20, fontweight='normal', ha='center')

    # Arrange layout
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    
    # Show plots
    plt.show()

    # Return the figure to a variable
    return fig


# Assess the feature completness measure of some polygon using cumulative feature counts and lengths/areas
def assess_feature_completeness(count_gdf, size_gdf, alpha=0.1, time_thresh=2, saturation_thresh=1.5, abs_thresh=1.5, return_full=False):
    '''
    Receives two GeoDataFrames (assumes identical timestamps and geometry):
    1) A cumulative count of added features by timestamps
    2) A cumulative value of all features by timestamps

    The function converts timestamp to actual datetime format, transforms the values to a mixed normalized percentage of added value (length / area) per each added unit.
    After that, the function applies the following statistical test:
    
    `If all cumulative change percentage is below some alpha (default: 10%) for a stable time period (default: 2 years) without a large absolute addition (default: 150% more than saturation point), the data is considered saturated.`
    
    For supposedly saturated data, the function computes the saturation point (1st month in stable period) and calculates cumulative percentage up to that point.

    The test is verified using 3 conditions:
    (1) No meaningfull relative addition (percentage<`alpha`) for at least `time_thresh` years.
    (2) No absolute addition (count<`abs_thresh`) for at least `time_thresh` years.
    (3) The absolute or relative addition change percentage since the saturation point is less than `saturation_thresh`.

    In all cases, the output is a DataFrame:
    * If not saturated --> the merged DataFrame, with updated timstamps and calculations.
    * If saturated --> can either return only values up to the saturation point + maximum value (default) or return the entire data with reference to the saturation point.
    
    Dependencies:
    * pandas as pd
    '''
    #---------------------------------------------------#
    #                   Data Wrangle                    #
    #---------------------------------------------------#

    # Fix timestamp
    count_gdf['timestamp'] = pd.to_datetime(count_gdf['timestamp'])
    size_gdf['timestamp'] = pd.to_datetime(size_gdf['timestamp'])

    # Sort both DataFrames by timestamp and reset index for proper alignment
    count_gdf = count_gdf.sort_values('timestamp').reset_index(drop=True)
    size_gdf = size_gdf.sort_values('timestamp').reset_index(drop=True)

    # Merge Dataframes
    gdf = count_gdf.copy().rename(columns={'value' : 'count'}) # Copy DF and rename count column
    gdf['size'] = size_gdf['value'] # Append size column

    #---------------------------------------------------#
    #                 Statistical Test                  #
    #---------------------------------------------------#
    
    # Transform values
    gdf['cumulative_percentage'] = gdf['size'] / gdf['count']
    gdf['cumulative_percentage'] = gdf['cumulative_percentage'].fillna(0) # Deal with periods without addition
    gdf['normalized_cum_per'] = gdf['cumulative_percentage'] / gdf['cumulative_percentage'].max()

    # Adjust alpha value for small to large mapping case
    if gdf['cumulative_percentage'].idxmax() >= (len(gdf) * 0.75):
        alpha = 1 - alpha

    # Apply completeness test for level alpha
    gdf['test'] = (gdf['normalized_cum_per'] < alpha) # Boolean term for each date in data

    #---------------------------------------------------#
    #                   Condititon 1                    #
    #---------------------------------------------------#

    # Iterate backwards in data to find stability period
    i = -1 # Running index (from end)
    test = gdf['test'].iat[i] # Running boolean test answer (from end)
    while test:
        try: # Update index
            i -= 1
            test = gdf['test'].iat[i]
        
        except IndexError: # Break loop if at first index
            break
    
    if i == -1:
        # Deal with last value percentage being greater than alpha (i.e. no stable period)
        print('Data incomplete: no stable period')
        return gdf

    stable = gdf.iloc[i+1:].copy() # Extract stable period

    ## If stable period shorter than given time threshold --> data is incomplete
    if (stable['timestamp'].max() - stable['timestamp'].min()) < pd.Timedelta(days=time_thresh*365):
        print('Data incomplete: stable period shorter than threshold')
        return gdf
    
    #---------------------------------------------------#
    #             Condititon 3 - 1st phase              #
    #---------------------------------------------------#

    else:
        # Extract saturated value
        saturation_point = stable.iloc[0]

        # Calculate saturation levels
        gdf['percentage_until_saturation'] = gdf['count'] / saturation_point['count']
        
         # Extract emprical maximal value
        real_max = gdf.iloc[-1]
      

        # Check first if data converged. If not, verify if almost converged after one-time event (if exists).
        # Test condition 3 for relative change:
        if (real_max['percentage_until_saturation'] >= saturation_thresh):

    #---------------------------------------------------#
    #                   Condititon 2                    #
    #---------------------------------------------------#

            stable['count_change'] = stable['count'] / stable['count'].max() # Calculate absolute change
            if (stable['count_change'] >= abs_thresh).any():
                # There exists some one-time addition event after saturation
                abs_add_index = stable['count_change'].idxmax()
                if (stable['timestamp'].max() - stable.loc[abs_add_index, 'timestamp']) < pd.Timedelta(days=time_thresh*365):
                    # No stable period since one-time addition event 
                    print('Data incomplete: no stable absolute addition period')
    
    #---------------------------------------------------#
    #             Condititon 3 - 2nd phase              #
    #---------------------------------------------------#

                # Redefine saturation point and levels for one-time addition event
                saturation_point = stable.iloc[abs_add_index]
                gdf['percentage_until_saturation'] = gdf['count'] / saturation_point['count']
                real_max = gdf.iloc[-1]
                
                # Test condition 3 for absoulte change:
                if (real_max['percentage_until_saturation'] >= saturation_thresh):
                    print('Data incomplete: stable absolute addition larger than threshold')
                    return gdf
            
            else:
                print('Data incomplete: stable relative addition larger than threshold')
                return gdf
    
    #---------------------------------------------------#
    #             Output Saturated Results              #
    #---------------------------------------------------#

        # Extract 80% saturation timestamp
        saturated_time = gdf[gdf['percentage_until_saturation'] >= 0.8]['timestamp'].iloc[0]
        print(f'Date complete: Polygon 80% saturated at {saturated_time}')

        ### Return entire gdf if requested
        if return_full:
            return gdf
        
        ### Return compact gdf (default)
        else:
            # Filter data until saturation
            saturated = gdf.iloc[:i+1].copy()
        
            # Concatenate empirical maximal value
            saturated = pd.concat([saturated,
                                   pd.DataFrame([real_max])],
                                   ignore_index=True)       
            return saturated
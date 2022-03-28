import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns', None)

# Import data
df =  pd.read_csv(
    'medical_examination.csv')

# Add 'overweight' column
BMI = df['weight'] / (df['height']/100)**2
# Check BMI in new column
df['overweight'] = BMI
#print(df)

# We set all column to 0
df['overweight'] = 0

# Set 1 if "overweighted" else 0
df.loc[BMI > 25, 'overweight'] = 1
#print(df)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def normalize_data(x) :
  if x <= 1:
      return 0
  else:
      return 1

df['cholesterol'] = df['cholesterol'].apply(lambda x: normalize_data(x))
df['gluc'] = df['gluc'].apply(lambda x: normalize_data(x))

#print(df)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.

    ## Re-ordered values
    df_cat = pd.melt(df, id_vars=['cardio'] , value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    #print(df_cat)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = None

    ## No need above part, I used no y position and kind="count". Just renamed labels after

    # Draw the catplot with 'sns.catplot()'

    fig = sns.catplot(x="variable",hue="value",col="cardio", data=df_cat,
                kind="count", ci=None)
    fig.set_axis_labels("variable", "total")


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.dropna()
    df['ap_lo'] <= df['ap_hi']
    df['height'] >= df['height'].quantile(0.025)
    df['height'] >= df['height'].quantile(0.025)

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

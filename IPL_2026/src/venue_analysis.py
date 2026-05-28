import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

matches = pd.read_csv('ipl_2026_data/final_matches_data.csv')
deliveries = pd.read_csv('ipl_2026_data/final_ipl_2026_deliveries_data.csv')

# 1. Highest scoring Venue

matches['total_runs'] = matches['first_ings_score'] + matches['second_ings_score']

venue_scores = (
    matches.groupby('venue')['total_runs']
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12,8))

sns.barplot(
    x=venue_scores.values,
    y=venue_scores.index
)

plt.xlabel("Average Runs")
plt.ylabel("Venue")
plt.title("Highest Scoring IPL Venues")

plt.show()

# 2. Chasing Friendly Venues

def get_chasing_team(row):

    if row['toss_decision'] == 'bat':

        if row['toss_winner'] == row['team1']:
            return row['team2']
        else:
            return row['team1']

    else:

        return row['toss_winner']
    
matches['chasing_team'] = matches.apply(
    get_chasing_team,
    axis = 1
)

matches['chasing_win'] = (
    matches['match_winner']
    == matches['chasing_team']
)

venue_chase = (
    matches.groupby('venue')['chasing_win']
    .mean()
    * 100
).sort_values(ascending=False)

plt.figure(figsize=(12,8))

sns.barplot(
    x=venue_chase.values,
    y=venue_chase.index
)

plt.xlabel("Chasing Win Percentage")
plt.ylabel("Venue")
plt.title("Venues Favoring Chasing Teams")

plt.show()
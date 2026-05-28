import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

matches = pd.read_csv('ipl_2026_data/final_matches_data.csv')
deliveries = pd.read_csv('ipl_2026_data/final_ipl_2026_deliveries_data.csv')

bowling = deliveries.copy()

bowling['is_dot'] = (
    (bowling['total_runs'] == 0)
    .astype(int)
)

bowling['is_wicket'] = (
    bowling['wicket_type']
    .notnull()
).astype(int)

bowling.loc[
    bowling['wicket_type'] == 'run out',
    'is_wicket'
] = 0

bowler_stats = bowling.groupby('bowler').agg({
    'total_runs': 'sum',
    'is_dot': 'sum',
    'is_wicket': 'sum'
})

bowler_stats['balls'] = (
    bowling.groupby('bowler')
    .size()
)

bowler_stats = bowler_stats.reset_index()

bowler_stats['overs'] = (
    bowler_stats['balls'] / 6
)

bowler_stats['economy'] = (
    bowler_stats['total_runs']
    / bowler_stats['overs']
)

bowler_stats['dot_ball_pct'] = (
    bowler_stats['is_dot']
    / bowler_stats['balls']
) * 100

bowler_stats = bowler_stats[
    bowler_stats['balls'] >= 60
]

# 1. Economy Leaders

best_economy = bowler_stats.sort_values(
    by='economy'
).head(10)

plt.figure(figsize=(10,6))

sns.barplot(
    data=best_economy,
    x='economy',
    y='bowler'
)

plt.title("Most Economical Bowlers")
plt.xlabel("Economy Rate")
plt.ylabel("Bowler")

plt.show()

# 2. Economy vs Wickets

plt.figure(figsize=(10,8))

sns.scatterplot(
    data=bowler_stats,
    x='economy',
    y='is_wicket',
    size='dot_ball_pct',
    sizes=(50, 500),
    alpha=0.7
)

plt.title("Bowler Performance Analysis")
plt.xlabel("Economy Rate")
plt.ylabel("Wickets")

plt.show()

# 3. Dot Ball Specialists

top_dot = bowler_stats.sort_values(
    by='dot_ball_pct',
    ascending=False
).head(10)

plt.figure(figsize=(10,6))

sns.barplot(
    data=top_dot,
    x='dot_ball_pct',
    y='bowler'
)

plt.title("Highest Dot Ball Percentage")
plt.xlabel("Dot Ball %")
plt.ylabel("Bowler")

plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

matches = pd.read_csv('ipl_2026_data/final_matches_data.csv')
deliveries = pd.read_csv('ipl_2026_data/final_ipl_2026_deliveries_data.csv')

# -------------------------------
# PLAYER IMPACT SCORE
# -------------------------------

deliveries['is_out'] = (
    deliveries['player_dismissed']
    .notnull()
    .astype(int)
)

batter_stats = deliveries.groupby('striker').agg({
    'runs_of_bat': 'sum',
    'is_boundary': 'sum',
    'is_out': 'sum'
})

batter_stats['balls_faced'] = (
    deliveries.groupby('striker')
    .size()
)

batter_stats['strike_rate'] = (
    batter_stats['runs_of_bat']
    / batter_stats['balls_faced']
) * 100

batter_stats = batter_stats[
    batter_stats['balls_faced'] >= 60
]

batter_stats['average'] = (
    batter_stats['runs_of_bat']
    / batter_stats['is_out']
)

batter_stats['boundary_pct'] = (
    batter_stats['is_boundary']
    / batter_stats['balls_faced']
) * 100

batter_stats['impact_score'] = (
    0.4 * batter_stats['strike_rate']
    + 0.3 * batter_stats['average']
    + 0.3 * batter_stats['boundary_pct']
)

top_impact = batter_stats.sort_values(
    by='impact_score',
    ascending=False
).head(10)

# 1. Top Impact Players

plt.figure(figsize=(10,6))

sns.barplot(
    data=top_impact,
    x='impact_score',
    y=top_impact.index
)

plt.title("Top Player Impact Scores")
plt.xlabel("Impact Score")
plt.ylabel("Batter")

plt.show()
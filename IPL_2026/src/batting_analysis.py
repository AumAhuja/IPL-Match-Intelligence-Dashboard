import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

matches = pd.read_csv('ipl_2026_data/final_matches_data.csv')
deliveries = pd.read_csv('ipl_2026_data/final_ipl_2026_deliveries_data.csv')

# 1. Top Run Scorers upto match 51

top_batters = deliveries.groupby('striker')['runs_of_bat'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_batters.values,
    y=top_batters.index
)

plt.xlabel("Total Runs")
plt.ylabel("Batter")
plt.title("Top 10 Run Scorers in IPL 2026")

plt.show()

# 2. Boundary Hitters

deliveries['is_boundary'] = deliveries[
    'runs_of_bat'
].isin([4,6])

boundaries = (
    deliveries.groupby('striker')['is_boundary']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

sns.barplot(
    x=boundaries.values,
    y=boundaries.index
)

plt.xlabel("Number of Boundaries")
plt.ylabel("Batter")
plt.title("Top Boundary Hitters")

plt.show()

# 3. Top Strike Rates upto Match 51

stats = deliveries.groupby('striker').agg({
    'runs_of_bat': 'sum',
    'over': 'count'
})

stats.rename(columns={
    'over': 'balls_faced'
}, inplace=True)

stats['strike_rate'] = (
    stats['runs_of_bat']
    / stats['balls_faced']
) * 100

stats = stats[
    stats['balls_faced'] >= 50
]

top_sr = stats.sort_values(
    'strike_rate',
    ascending=False
).head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_sr['strike_rate'],
    y=top_sr.index
)

plt.xlabel("Strike Rate")
plt.ylabel("Batter")
plt.title("Top 10 Batters by Strike Rate")

plt.show()

# -------------------------------
# DEATH OVER SPECIALISTS
# -------------------------------

# 1. Best Finishers

death = deliveries[deliveries['phase'] == 'Death Overs']

death_runs = (
    death.groupby('striker')['runs_of_bat']
    .sum()
    .sort_values(ascending=False)
)

top_10 = death_runs.head(10)

plt.figure(figsize=(10,6))

sns.barplot(
    x=top_10.values,
    y=top_10.index
)

plt.title("Top Death Over Run Scorers")
plt.xlabel("Runs")
plt.ylabel("Batter")

plt.show()

# 2. Boundary Percentage

death['is_boundary'] = death['runs_of_bat'].isin([4,6]).astype(int)

boundary_pct = death.groupby('striker')['is_boundary'].mean() * 100

boundary_pct = (
    boundary_pct
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=boundary_pct.values,
    y=boundary_pct.index
)

plt.title("Top Boundary Percentage in Death Overs")
plt.xlabel("Boundary Percentage")
plt.ylabel("Batter")

plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

matches = pd.read_csv('ipl_2026_data/matches.csv')
deliveries = pd.read_csv('ipl_2026_data/ipl_2026_deliveries.csv')

# print(matches.head(5))
# print(deliveries.head(5))

# print(matches.info())
# print(deliveries.info())

# print(matches.shape)
# print(deliveries.shape)

# print(matches.isna().sum() / len(matches) * 100)
# print(deliveries.isna().sum() / len(matches) * 100)

# -------------------------------------
# CLEANING MATCH DATASET
# -------------------------------------

matches = matches.drop(columns=['wb_runs'])
matches = matches.drop(columns=['wb_wickets'])

matches = matches[matches['match_result']!='abandoned']
# print(matches.isna().sum() / len(matches) * 100)

matches['date'] = pd.to_datetime(matches['date'])

# print(matches[matches.duplicated()])
# print(matches.dtypes)

# Checking for outliers

# cols = ['match_id', 'first_ings_score', 'first_ings_wkts','second_ings_score','second_ings_wkts','balls_left','highscore']

# plt.figure(figsize=(15, 5))

# for i, col in enumerate(cols, 1):
#     plt.subplot(1, 7, i)
#     sns.boxplot(y=matches[col], color='skyblue', width=0.3)
#     plt.title(f'Boxplot of {col}', fontsize=12)
#     plt.ylabel('')
#     plt.grid(axis='y', linestyle='--', alpha=0.6)

# plt.tight_layout()
# plt.show()

# -------------------------------------
# FINAL MATCH DATASET UPTO MATCH 39
# -------------------------------------

# matches.to_csv('ipl_2026_data/final_matches_data.csv', index=False)

# -------------------------------------
# CLEANING DELIVERIES DATASET
# -------------------------------------

deliveries['wicket_type'] = deliveries['wicket_type'].fillna('Wicketless delivery')
deliveries['player_dismissed'] = deliveries['player_dismissed'].fillna('N/A')
deliveries['fielder'] = deliveries['fielder'].fillna('N/A')
# print(deliveries.isna().sum() / len(matches) * 100)

# print(deliveries[deliveries.duplicated()])

deliveries['date'] = pd.to_datetime(deliveries['date'])
# print(deliveries.dtypes)

# cols = ['match_id', 'season', 'match_no','innings','over','runs_of_bat']

# plt.figure(figsize=(15, 5))

# for i, col in enumerate(cols, 1):
#     plt.subplot(1, 6, i)
#     sns.boxplot(y=deliveries[col], color='skyblue', width=0.3)
#     plt.title(f'Boxplot of {col}', fontsize=12)
#     plt.ylabel('')
#     plt.grid(axis='y', linestyle='--', alpha=0.6)

# plt.tight_layout()
# plt.show()


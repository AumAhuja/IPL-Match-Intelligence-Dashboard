import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

matches = pd.read_csv('ipl_2026_data/final_matches_data.csv')
deliveries = pd.read_csv('ipl_2026_data/final_ipl_2026_deliveries_data.csv')

corr_df = deliveries[[
    'runs_of_bat',
    'extras',
    'total_runs',
    'is_boundary',
    'is_dot',
    'over'
]]

correlation_matrix = corr_df.corr()

plt.figure(figsize=(10,7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Correlation Analysis of Match Features")

plt.show()
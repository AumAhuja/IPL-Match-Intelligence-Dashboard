import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

matches = pd.read_csv('ipl_2026_data/final_matches_data.csv')
deliveries = pd.read_csv('ipl_2026_data/final_ipl_2026_deliveries_data.csv')

# Total Runs Column
deliveries['total_runs'] = deliveries['runs_of_bat'] + deliveries['extras']

# Boundary Column
deliveries['is_boundary'] = deliveries['runs_of_bat'].apply(
    lambda x: 1 if x in [4,6] else 0
)

# Dot Delivery Column
deliveries['is_dot'] = deliveries['total_runs'].apply(
    lambda x: 1 if x==0 else 0
)

# Phase Column

def phase(over):
    if over<=6:
        return 'Powerplay'
    elif over<=15:
        return 'Middle Overs'
    else:
        return 'Death Overs'
    
deliveries['phase'] = deliveries['over'].apply(phase)

deliveries.to_csv('ipl_2026_data/final_ipl_2026_deliveries_data.csv',index=False)

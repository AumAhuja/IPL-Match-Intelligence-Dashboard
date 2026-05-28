import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

matches = pd.read_csv('ipl_2026_data/final_matches_data.csv')
deliveries = pd.read_csv('ipl_2026_data/final_ipl_2026_deliveries_data.csv')

# 1. Teams generally prefer to Bat first or Bowl first?

sns.countplot(data=matches, x='toss_decision')
plt.show()

# 2. Which decision has frequently guaranteed wins to the teams in IPL 2026?

wins = (matches['toss_winner'] == matches['match_winner'])
sns.countplot(data = matches, x=wins)
plt.title("Did Toss Winner Also Win the Match?", fontsize=14)
plt.xlabel("Toss Winner Won Match")
plt.ylabel("Number of Matches")

plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()

# 3. Mathematical analysis

print((matches['toss_winner'] == matches['match_winner']).mean())     # 55.26%

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers,PillowWriter
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA

#data is collected on the internet and saved in csv file
data=pd.read_csv('62-24csv.csv')
data.head()

# you can make change here if you want 
target_years = [1961,1967, 1970,1975, 1980,1985,1990,1995,2000,2005, 2010,2018, 2023]


fig, axes = plt.subplots(figsize=(10, 6))

fig.patch.set_facecolor('black')
axes.set_facecolor('black')

axes.set_ylim(0, data['Population_MM'].max() + 10)
axes.set_xlabel('Year',color='white')
axes.set_ylabel('Population',color='white')
axes.set_title('Evolution of the Algerian population (in millions)',color='white')

# this is important for animation 
def animation_function(i):
    axes.clear()  # Efface le contenu précédent
    axes.set_ylim(0, data['Population_MM'].max() + 10)  # Re-définir les limites des y
    axes.set_title('Evolution of the Algerian population (in millions)',color='white',fontsize=14)
    axes.bar(data['Year'][:i+1], data['Population_MM'][:i+1], color='skyblue', edgecolor='black')
    bars=axes.bar(data['Year'][:i+1],data['Population_MM'][:i+1],color='skyblue', edgecolor='black')
    for bar in bars:
        height = bar.get_height()
        x = bar.get_x() + bar.get_width() / 2.0
        y = -1  # Position verticale du texte
        year = data["Year"].iloc[list(bars).index(bar)]

        if year in target_years:
            axes.text(
                bar.get_x() + bar.get_width() / 2.0, height + 0.5,
                f'{data["Year"].iloc[list(bars).index(bar)]}',
                ha='center', va='bottom',
                rotation=60,
                color='white'
            )
        if year in target_years:
            axes.text(
                x, y - 1.5,  # Position verticale pour la population
                f'{data["Population_MM"].iloc[list(bars).index(bar)]:.1f}',
                ha='center', va='top',
                color='white', 
                weight='bold'
            )
        axes.set_xticks([])
        axes.set_xticklabels([]) 
        axes.set_yticks([])

fig.text(0.95, 0.01, 'Source: Worldata & ONS.DZ', ha='right', color='white', fontsize=10)
fig.text(0.05, 0.01, 'Made by Abdenour Dellil', ha='left', color='white', fontsize=10)

#saving the vizualisation in gif
animation = FuncAnimation(fig, animation_function, frames=len(data), interval=280, repeat=False)

writer=PillowWriter(fps=2)

animation.save('population_evolution.gif',writer=writer)

plt.show()

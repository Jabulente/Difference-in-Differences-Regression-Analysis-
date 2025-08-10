import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visulize_lineplot(df, date_col, value_col, group_col, event_date, title, xlabel, ylabel, label, figsize = (9, 6)):
    fig, ax = plt.subplots(figsize=figsize)
    
    plt.rcParams.update({'font.family': 'Sans-Serif', 'font.style': 'normal', 'font.size': 9})
    sns.lineplot(data=df, x=date_col, y=value_col, hue=group_col, palette='Set2', alpha=1, errorbar=None, linewidth=3)
    plt.axvline(event_date, color='gray', linestyle='--', label=f'{label}: {event_date.strftime('%B %d, %Y')}')
    plt.title(title, fontweight='bold', fontsize=24, pad=20, fontfamily='Agency FB')
    sns.despine(ax=ax, left=True, right=True, bottom=False)
    plt.grid(linestyle='--', alpha=0.2) 
    
    plt.xlabel(xlabel, fontsize=11, labelpad=10)
    plt.ylabel(ylabel, fontsize=11, labelpad=10)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend(frameon=False, fontsize=10)
    
    plt.tight_layout()
    plt.show()
    
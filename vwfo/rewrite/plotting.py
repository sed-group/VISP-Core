import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib import rc
import seaborn as sns

# Set the global font to be DejaVu Sans, size 10 (or any other sans-serif font of your choice!)
rc('font',**{'family':'sans-serif','sans-serif':['DejaVu Sans'],'size':10})

# Set the font used for MathJax - more on this later
rc('mathtext',**{'default':'regular'})

marker_options = ['s', 'o', 'x', 'v', '^', '<', '>', '8', 'p', '*', 'h', 'H', 'D', 'd']

color_options = ['#1f77b4', '#ff7f0e', '#2ca02c', '#8fbbd9', '#ffbf86', '#95cf95', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

technology_labels = {
    1: "Technology 1",
    2: "Technology 2",
    3: "Technology 3",
}

# Create a list of legend elements
legend_elements = []
for tech_id, label in technology_labels.items():
    # Use marker 'o' for in and 'x' for out, adjust if different markers are used per tech
    legend_elements.append(mlines.Line2D([], [], color=color_options[tech_id-1], marker='o', linestyle='None', markersize=10, label=label))
legend_elements.append(mlines.Line2D([], [], color='#7f7f7f', marker='x', linestyle='None', markersize=10, label='Incompatible design'))

# Increasing the default font sizes
plt.rc('font', size=18)  # controls default text size
plt.rc('axes', titlesize=24)  # fontsize of the axes title
plt.rc('axes', labelsize=24)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=20)  # fontsize of the x tick labels
plt.rc('ytick', labelsize=20)  # fontsize of the y tick labels
plt.rc('legend', fontsize=20)  # legend fontsize

def plot_figure_SV_V(designs):
    figs = []
    for platform in [0,1,2]:
        fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
        # Additional padding can be adjusted in subplots_adjust if necessary
        fig.subplots_adjust(wspace=0.1, hspace=0.1)
        #fig.suptitle(f"Tradespace storyboard of an sequence of 3 scenarios", fontsize=16)
        for scenario in [0,1,2]:
            x_in =  [design.volume for design in designs[scenario][platform] if design.platform_compatible]
            x_out = [design.volume for design in designs[scenario][platform] if not design.platform_compatible]
            y_in =  [-design.value for design in designs[scenario][platform] if design.platform_compatible]
            y_out = [-design.value for design in designs[scenario][platform] if not design.platform_compatible]
            markers = ['o' if design.platform_compatible else 'x' for design in designs[scenario][platform]]
            colors = [color_options[design.technology-1] if design.platform_compatible else color_options[design.technology+2] for design in designs[scenario][platform]]
            colors_in =  [color_options[design.technology-1] for design in designs[scenario][platform] if design.platform_compatible]
            colors_out = ['#7f7f7f' for design in designs[scenario][platform] if not design.platform_compatible]

            ax = axes[scenario]

            ax.scatter(x_in, [element for element in y_in], alpha=0.7, marker='o', color=colors_in, s=10, label=f"Technology")
            ax.scatter(x_out, [element for element in y_out], alpha=0.3, marker='x', color=colors_out, s=10)

            ax.set_title(f"{2022+2*scenario}-{2024+2*scenario}", y=0.95, pad=-10, loc='right', x=0.95)  # Add a title to the axes.

            ax.set_xlabel("Volume (L)")  # Add an x-label to the axes.
            ax.set_ylabel("Surplus Value (M€)")  # Add a y-label.
            ax.set_xlim([0, 20])
            ax.set_ylim([0, 200])
            #ax.legend();  # Add a legend.
            ax.grid(True)
        fig.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=len(technology_labels)+1, frameon=False)
        plt.tight_layout()
        plt.savefig(f'platform{platform}.png', format='png', dpi=900, bbox_inches='tight')
        plt.savefig(f'platform{platform}.svg', format='svg', dpi=900, bbox_inches='tight')
        figs.append(fig)
    return figs


# Set the overall context and style for Seaborn plots
sns.set_theme(style="whitegrid")
sns.set_context("notebook", font_scale=2.5)
# makes axis black
sns.set_style("ticks", {'axes.grid' : True})

def plot_violinplot(df, puntos4):

    g = sns.FacetGrid(df, height=6, aspect=2, ylim=(0,1.2))

    g.map(sns.violinplot,
                        data=puntos4, 
                        dodge=False,
                        color=(0.9, 0.9, 0.9, 0.5),
                        scale='count',
                        inner="quart",
                        fill=True,
                        width=1.2,
                        )

    g.map(sns.swarmplot,data=df, 
                        x='platform',
                        y='vwfo',
                        dodge=False, 
                        #hue='technology', 
                        palette=[color_options[0]], 
                        s=10)

    # Adjusting the y axis label and size
    g.set_ylabels("VWFO")
    g.set_titles(size=14) # If your FacetGrid has titles, adjust their size as needed

    #g.set_xlabels("Platforms")
    g.set_xticklabels(["Platform A:\nOver-constrained", "Platform B:\nUnder-constrained", "Platform C:\nBalanced"])

    # for ax in g.axes.ravel():
    #        ax.text(1.5, 1.1, "Custom text", 
    #               fontsize = 12,          # Size
    #               fontstyle = "oblique",  # Style
    #               color = "red",          # Color
    #               ha = "center", # Horizontal alignment
    #               va = "center") # Vertical alignment

    # Adding a legend for the quartile lines
    g.add_legend(title="", 
                    label_order=['Top and bottom quartiles', 'Median'],
                    labels=['Top and bottom quartiles', 'Median'],
                    # labels text size
                    fontsize=20,
                    loc='upper center', 
                    bbox_to_anchor=(0.33, 1.07), 
                    ncol=2, 
                    frameon=False)

    g.savefig(f'platforms.svg', format='svg', dpi=900, bbox_inches='tight')

    return g

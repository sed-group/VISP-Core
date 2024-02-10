import streamlit as st
import numpy as np
import pandas as pd
from TotalMechanicalVolumeOfHUD import TotalMechanicalVolumeOfHUD as tmv
from SurplusValue import surplus_value as sv
from vwfo import Scenario, Platform, Technology, Design, calculate_tradespace_designs
from plotting import plot_figure_SV_V, plot_violinplot
import plotly.express as px

# Sidebar
# st.sidebar.header("This is a sidebar")


# Title
st.title("VWFO")

num_samples = st.slider("Select a number of samples", 1, 1000, 10)


data_scenarios = pd.DataFrame(
    {
        "id": [1, 2, 3],
        "description": ["Scenario 1", "Scenario 2", "Scenario 3"],
        "s_x1": [
            ["Technology 1", "Technology 2"],
            ["Technology 1", "Technology 2"],
            ["Technology 1", "Technology 2", "Technology 3"],
        ],
        "s_x2": [[2022, 2024], [2024, 2026], [2026, 2030]],
        "s_x3": [100, 80, 80],
    }
)

data_platforms = pd.DataFrame(
    {
        "id": [1, 2, 3],
        "p_x1": [300, 400, 350],
        "p_x2": [250, 400, 350],
        "p_x3": [200, 300, 250],
    }
)

data_technologies = pd.DataFrame(
    {
        "id": [1, 2, 3],
        "name": ["Technology 1", "Technology 2", "Technology 3"],
        "volume_coefficients": [[1, 3, 1], [1, 3, 2], [1, 3, 0.5]],
        "t_x1": [[5, 10], [7, 15], [10, 20]],
        "t_x2": [[2, 4], [3, 7], [4, 10]],
        "t_x3": [[1000, 5000], [5000, 20000], [1000, 30000]],
    }
)

scenarios = []
for index, row in data_scenarios.iterrows():
    scenarios.append(
        Scenario(
            id=row["id"],
            description=row["description"],
            s_x1=row["s_x1"],
            s_x2=row["s_x2"],
            s_x3=row["s_x3"],
        )
    )

platforms = []
for index, row in data_platforms.iterrows():
    platforms.append(
        Platform(
            id=row["id"],
            p_x1=row["p_x1"],
            p_x2=row["p_x2"],
            p_x3=row["p_x3"],
        )
    )

technologies = []
for index, row in data_technologies.iterrows():
    technologies.append(
        Technology(
            id=row["id"],
            name=row["name"],
            volume_coeficients=row["volume_coefficients"],
            factors={"t_x1": row["t_x1"], "t_x2": row["t_x2"], "t_x3": row["t_x3"]},
        )
    )

# Three tabs
tab_scenarios, tab_platforms, tab_technologies = st.tabs(
    ["Scenarios", "Platforms", "Technologies"]
)

with tab_scenarios:
    scenarios_data_editor = st.data_editor(
        data_scenarios,
        hide_index=True,
    )

with tab_platforms:
    platforms_data_editor = st.data_editor(
        data_platforms,
        hide_index=True,
    )

with tab_technologies:
    technologies_data_editor = st.data_editor(
        data_technologies,
        hide_index=True,
    )

# do something if button is clicked
if st.button("Generate designs"):
    progress_text = "Operation in progress. Please wait."
    tradespace_bar = st.progress(0, text=progress_text)
    designs = []
    for i, scenario in enumerate(scenarios):
        designs.append([])
        designs_scenario = []
        for j, platform in enumerate(platforms):
            designs_scenario.append([])
            designs_platform = []
            for k, technology in enumerate(technologies):
                if technology.name in scenario.s_x1:
                    tradespace_bar.progress(
                        ((i + 1) * (j + 1) * (k + 1))
                        / (len(scenarios) * len(platforms) * len(technologies)),
                        text=progress_text,
                    )
                    # st.write(f"Scenario {i+1} Platform {j+1} Technology {k+1}")
                    # designs_scenario.append([i,j,k])
                    designs_platform += calculate_tradespace_designs(
                        technology.factors,
                        num_samples,
                        scenario,
                        platform,
                        technology.id,
                    )
            designs_scenario[j] = designs_platform
        designs[i] = designs_scenario

    # Make a flat list of all designs
    designs_list = []
    for scenario in [0, 1, 2]:
        for platform in [0, 1, 2]:
            for design in designs[scenario][platform]:
                designs_list.append(
                    [
                        design.scenario.id,
                        design.platform.id,
                        design.technology,
                        design.platform_compatible,
                        design.volume,
                        -design.value,
                        design.t_x1,
                        design.t_x2,
                        design.t_x3,
                        design.x,
                        design.y,
                        design.z,
                    ]
                )
    columns = [
        "scenario",
        "platform",
        "technology",
        "platform_compatible",
        "volume",
        "value",
        "t_x1",
        "t_x2",
        "t_x3",
        "x",
        "y",
        "z",
    ]
    df = pd.DataFrame(designs_list, columns=columns)
    # add a new column calculated as the multiplication of t_x1 and t_x2
    df["FOV"] = (df["t_x1"] * df["t_x2"] * 100) / (67 * 20)

    # tabs for the plots
    tab_scatter_matrix, tab_par_coord, tab_statistics, tab_figure1, tab_figure2 = (
        st.tabs(
            [
                "Scatter Matrix",
                "Parallel Coordinates",
                "Statistics",
                "Figure 1",
                "Figure 2",
            ]
        )
    )

    # scatter_matrix of the designs
    fig_scatter_matrix = px.scatter_matrix(
        df.filter(
            items=[
                "volume",
                "value",
                "FOV",
                "t_x3",
            ]
        ),
        color="value",
        height=800,
    )
    with tab_scatter_matrix:
        st.plotly_chart(fig_scatter_matrix, use_container_width=True)

    # parallel coordinates plot of the designs
    fig_par_coord = px.parallel_coordinates(
        df.filter(
            items=[
                "volume",
                "value",
                "FOV",
                "t_x3",
            ]
        ),
        color="value",
    )
    with tab_par_coord:
        st.plotly_chart(fig_par_coord, use_container_width=True)

    tradespace_bar.empty()
    # st.write(f"Total number of designs generated: {len(df)}")

    s1 = df[df["scenario"] == 1]
    s2 = df[df["scenario"] == 2].reset_index()
    s3 = df[df["scenario"] == 3].reset_index()
    s23 = df[(df["scenario"] == 2) | (df["scenario"] == 3)].reset_index()

    number_of_designs_s1 = len(s1)
    number_of_designs_s2 = len(s2)
    number_of_designs_s3 = len(s3)
    number_of_designs_s23 = len(s23)
    # st.write(f"Number of designs in Scenario 1: {number_of_designs_s1}")
    # st.write(f"Number of designs in Scenario 2: {number_of_designs_s2}")
    # st.write(f"Number of designs in Scenario 3: {number_of_designs_s3}")
    # st.write(f"Number of designs in Scenario 2 and 3: {number_of_designs_s23}")

    my_bar = st.progress(0, text=progress_text)
    puntos4 = [[], [], []]
    puntos4_tech = [[], [], []]
    for i, design_i in s1.iterrows():
        my_bar.progress((i + 1) / number_of_designs_s1, text=progress_text)
        N = 0
        sigma = 0
        if design_i["platform_compatible"]:
            for j, design_j in s23.iterrows():
                if design_j["platform_compatible"]:
                    # print(design_i['value'], design_j['value'])
                    sign = np.sign(design_j["value"] - s23.loc[i]["value"])
                    # print(sign)
                    sigma = sigma + sign
                    N = N + 1
            design_i["vwfo"] = (1 / (N - 1)) * sigma
            puntos4[design_i["platform"] - 1].append(design_i["vwfo"])
            puntos4_tech[design_i["platform"] - 1].append(design_i["technology"])
    my_bar.empty()

    # Calculating medians and upper quartiles (Q3) for each sublist
    medians = [np.median(sublist) for sublist in puntos4]
    lower_quartiles = [np.percentile(sublist, 25) for sublist in puntos4]
    upper_quartiles = [np.percentile(sublist, 75) for sublist in puntos4]

    def quartile_counts(sublist):
        median = np.median(sublist)
        Q1 = np.percentile(sublist, 25)
        Q3 = np.percentile(sublist, 75)

        count_Q1 = len([x for x in sublist if x <= Q1])
        count_Q2 = len([x for x in sublist if Q1 < x <= median])
        count_Q3 = len([x for x in sublist if median < x <= Q3])
        count_Q4 = len([x for x in sublist if x > Q3])

        return count_Q1, count_Q2, count_Q3, count_Q4

    quartile_counts_per_sublist = [quartile_counts(sublist) for sublist in puntos4]

    # Additional relevant statistical values for each sublist
    means = [np.mean(sublist) for sublist in puntos4]
    std_devs = [np.std(sublist) for sublist in puntos4]
    min_values = [np.min(sublist) for sublist in puntos4]
    max_values = [np.max(sublist) for sublist in puntos4]

    platform_ids = ["A", "B", "C"]

    # Present that in a table
    with tab_statistics:
        st.table(
            pd.DataFrame(
                {
                    "Platform": platform_ids,
                    "Lower Quartile (Q1)": lower_quartiles,
                    "Median": medians,
                    "Upper Quartile (Q3)": upper_quartiles,
                    "Q1 Count": [x[0] for x in quartile_counts_per_sublist],
                    "Q2 Count": [x[1] for x in quartile_counts_per_sublist],
                    "Q3 Count": [x[2] for x in quartile_counts_per_sublist],
                    "Q4 Count": [x[3] for x in quartile_counts_per_sublist],
                    "Mean": means,
                    "Standard Deviation": std_devs,
                    "Minimum Value": min_values,
                    "Maximum Value": max_values,
                }
            )
        )

    # Preparing data for DataFrame
    data = []
    for i in range(len(puntos4)):
        for j in range(len(puntos4[i])):
            # Appending each row to the data list
            data.append([i + 1, puntos4[i][j], puntos4_tech[i][j]])

    # Creating DataFrame
    df_results = pd.DataFrame(data, columns=["platform", "vwfo", "technology"])
    # st.dataframe(df_results)

    figs = plot_figure_SV_V(designs)
    g = plot_violinplot(df_results, puntos4)
    with tab_figure1:
        for fig in figs:
            st.pyplot(fig)
    with tab_figure2:
        st.pyplot(g)

    # Pareto Front indentification and plotting
    import matplotlib.pyplot as plt

    def identify_pareto(df):
        df_sorted = df.sort_values(by=["volume", "value"], ascending=[True, False])
        pareto_front = pd.DataFrame(columns=df_sorted.columns)
        current_max_value = -float("inf")

        for _, row in df_sorted.iterrows():
            if row["value"] > current_max_value:
                pareto_front = pareto_front.append(row)
                current_max_value = row["value"]

        return pareto_front

    # Identify Pareto front
    pareto_front_df = identify_pareto(df)

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot all designs on the axis object
    ax.scatter(df["volume"], df["value"], color="blue", label="All Designs")

    # Highlight Pareto-optimal designs on the same axis object
    ax.scatter(
        pareto_front_df["volume"],
        pareto_front_df["value"],
        color="red",
        label="Pareto Designs",
    )

    # Labeling
    ax.set_xlabel("Volume", fontsize=10)
    ax.set_ylabel("Value", fontsize=10)
    ax.set_title("Designs and Pareto Front", fontsize=10)
    ax.legend(fontsize=10)
    ax.tick_params(axis="both", which="major", labelsize=10)

    # Pass the figure object to Streamlit's pyplot function
    st.pyplot(fig)

    marker_styles = {
        "1": "o",  # Circle
        "2": "s",  # Square
        "3": "^",  # Triangle
        # Add more mappings as needed
    }
    color_options = ['#1f77b4', '#ff7f0e', '#2ca02c', '#8fbbd9', '#ffbf86', '#95cf95', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

    for scenario in df["scenario"].unique():
        # Filter the DataFrame for the current scenario
        df_scenario = df[df["scenario"] == scenario]

        # Identify Pareto front for the current scenario
        pareto_front_df = identify_pareto(df_scenario)

        # Create a figure and axis object for the current scenario
        fig2, ax2 = plt.subplots()
        ax2.set_ylim(0, 200)

        for tech, marker in marker_styles.items():
            # Filter the DataFrame for the current technology within the scenario
            df_tech = df_scenario[df_scenario["technology"] == int(tech)]

            # Check if df_tech is not empty to avoid errors
            if not df_tech.empty:
                # Plot designs for the current technology with its specific marker
                ax2.scatter(
                    df_tech["volume"],
                    df_tech["value"],
                    color=color_options[int(tech)-1],
                    marker=marker,
                    label=f"Tech: {tech}",
                )

        # Plot all designs for the current scenario
        # ax2.scatter(df_scenario['volume'], df_scenario['value'], color='blue', label=f'All Designs for Scenario {scenario}')

        # Highlight Pareto-optimal designs for the current scenario
        ax2.scatter(
            pareto_front_df["volume"],
            pareto_front_df["value"],
            color="red",
            label=f"Pareto Designs for Scenario {scenario}",
        )

        # Extract x and y coordinates
        x = pareto_front_df["volume"].values
        y = pareto_front_df["value"].values

        # Fit a polynomial of degree n (e.g., n=2 for quadratic)
        degree = 2
        coefficients = np.polyfit(x, y, degree)

        # Create a polynomial function from the coefficients
        polynomial_function = np.poly1d(coefficients)

        # Generate x values for plotting the polynomial curve (e.g., 100 points)
        x_fit = np.linspace(x.min(), x.max(), 100)

        # Calculate y values using the polynomial function
        y_fit = polynomial_function(x_fit)
        # Plot the polynomial fit
        ax2.plot(x_fit, y_fit, color="red", label=f"{degree} Degree Polynomial Fit")
        # Labeling with fontsize set to 10
        ax2.set_xlabel("Volume", fontsize=10)
        ax2.set_ylabel("Value", fontsize=10)
        ax2.set_title(f"Designs and Pareto Front for Scenario {scenario}", fontsize=10)
        ax2.legend(fontsize=10)

        # Set tick labels to fontsize 10
        ax2.tick_params(axis="both", which="major", labelsize=10)

        # Display the plot in Streamlit
        st.pyplot(fig2)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, Optional

def build_space_filling_lhs(factor_level_ranges: Dict[str, list], num_samples: Optional[int] = None, seed: Optional[int] = 42) -> pd.DataFrame:
    """
    Generates a space-filling Latin Hypercube Sampling design dataframe from a dictionary
    of factor/level ranges with an option to set a random seed for reproducibility.

    Parameters:
    - factor_level_ranges: Dict[str, list], where the key is the factor name and the value is a list [min, max].
    - num_samples: Optional[int], the number of samples to be generated.
    - seed: Optional[int], a seed for the random number generator for reproducibility.

    Returns:
    - pd.DataFrame containing the LHS design with the specified number of samples.
    """
    # Set the random seed if provided
    if seed is not None:
        np.random.seed(seed)

    num_factors = len(factor_level_ranges)
    if num_samples is None:
        num_samples = num_factors
    design_matrix = np.zeros((num_samples, num_factors))

    for i, (factor, bounds) in enumerate(factor_level_ranges.items()):
        min_val, max_val = bounds
        intervals = np.linspace(min_val, max_val, num_samples + 1)
        for j in range(num_samples):
            lower_bound = intervals[j]
            upper_bound = intervals[j + 1]
            design_matrix[j, i] = np.random.uniform(lower_bound, upper_bound)
        np.random.shuffle(design_matrix[:, i])

    df = pd.DataFrame(design_matrix, columns=factor_level_ranges.keys())
    return df

# Test the function
def test_build_space_filling_lhs():
    factor_level_ranges = {'Pressure': [50, 70], 'Temperature': [290, 350], 'Flow rate': [0.9, 1.0]}
    num_samples = 1000
    seed = 42
    df = build_space_filling_lhs(factor_level_ranges, num_samples, seed)
    assert len(df) == num_samples
    assert all(df['Pressure'] >= 50) and all(df['Pressure'] <= 70)
    assert all(df['Temperature'] >= 290) and all(df['Temperature'] <= 350)
    assert all(df['Flow rate'] >= 0.9) and all(df['Flow rate'] <= 1.0)

def example_usage():
    factor_level_ranges = {'Pressure': [50, 70], 'Temperature': [290, 350], 'Flow rate': [0.9, 1.0]}
    num_samples = 1000
    seed = 42
    df = build_space_filling_lhs(factor_level_ranges, num_samples, seed)
    print(df)

    df_with_seed = build_space_filling_lhs(factor_level_ranges, num_samples, seed)

    # Plotting the results for visualization
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))
    axs[0].scatter(df_with_seed['Pressure'], df_with_seed['Temperature'], color='red')
    axs[0].set_xlabel('Pressure')
    axs[0].set_ylabel('Temperature')
    axs[0].set_title('Pressure vs Temperature')

    axs[1].scatter(df_with_seed['Pressure'], df_with_seed['Flow rate'], color='blue')
    axs[1].set_xlabel('Pressure')
    axs[1].set_ylabel('Flow rate')
    axs[1].set_title('Pressure vs Flow rate')

    axs[2].scatter(df_with_seed['Temperature'], df_with_seed['Flow rate'], color='green')
    axs[2].set_xlabel('Temperature')
    axs[2].set_ylabel('Flow rate')
    axs[2].set_title('Temperature vs Flow rate')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test_build_space_filling_lhs()
    example_usage()
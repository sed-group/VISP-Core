from deap import creator

import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

SMALL_SIZE = 12
MEDIUM_SIZE = 16
BIGGER_SIZE = 20

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the figure title

plt.rcParams['figure.figsize'] = 12, 8

n_components = 300

def visualise_components(components):
    plt.scatter([components[idx_component]['volume'] for idx_component in components],
                [components[idx_component]['value'] for idx_component in components],
                color = 'purple', alpha=0.04
               )

    for idx_component, component in components.items():
        plt.annotate(f'{idx_component:02.0f}', xy=(component['volume'], component['value']), fontsize=MEDIUM_SIZE)

    plt.xlabel('volume [m^3]')
    plt.ylabel('value [€]')
    plt.title('Components')

def generate_components(n_components = 20, 
                      volume_mean = 0.1, volume_sd = 10,
                      value_mean = 0.1, value_sd = 100,
                      value_distribution_mode = 'random',
                      noise_factor = 1./2,
                      seed = 3141592653, visualise=True):
    """
    n_components: int. the total number of components to choose from
    volume_mean: float. the mean of the volume distribution
    volume_sd: float. the standard deviation of the volume distribution
    value_mean: float. when value_distribution_mode='random': the mean of the monetary 
    value_distribution_mode: str. (default: 'random', 'squared')
    noise_factor: float. when value_distribution_mode='squared': the standard deviation of the noise introduced
    """

    np.random.seed(seed)

    volumes = np.abs(np.random.normal(volume_mean, volume_sd, n_components))

    if 'squared' == value_distribution_mode:
        values =  volumes ** 2 
        values += values * np.random.normal(0, noise_factor, len(volumes))
        values = np.abs(values)
    elif 'random' == value_distribution_mode:
        values = np.abs(np.random.normal(value_mean, value_sd, n_components))
        
    components = {idx: {'volume': volumes[idx], 'value': values[idx]} for idx in range(n_components)}
    
    if visualise:
        visualise_components(components)

        
    return components

components = generate_components(n_components, value_distribution_mode="random")

plt.show()
import noise
import numpy as np

def add_perlin_noise(lon_lat_val_list, iterations, scale=1.0, octaves=1, persistence=0.5, lacunarity=2.0):
    """
    Apply Perlin noise to val based on (lon, lat) over multiple iterations.

    Parameters:
    lon_lat_val_list : list of tuples (lon, lat, val)
        The list of longitude, latitude, and values.
    iterations : int
        The number of iterations to apply Perlin noise.
    scale : float
        Scale of the Perlin noise.
    octaves : int
        Number of octaves for the Perlin noise generation.
    persistence : float
        Persistence value for Perlin noise.
    lacunarity : float
        Lacunarity value for Perlin noise.
    
    Returns:
    list
        List of updated values after applying Perlin noise over iterations.
    """
    # Initialize values list with the input values
    updated_values = [v for _, _, v in lon_lat_val_list]

    # Iterate over the desired number of iterations
    for iteration in range(iterations):
        new_values = []
        for i, (lon, lat, val) in enumerate(lon_lat_val_list):
            # Generate Perlin noise based on longitude and latitude
            perlin_noise = noise.pnoise2(lon * scale, lat * scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)
            
            # Add Perlin noise to the existing value
            new_val = updated_values[i] + perlin_noise
            new_values.append(new_val)
        
        # Update the values with the new ones for the next iteration
        updated_values = new_values

    # Return the final updated list of (lon, lat, val) with the modified values
    return [(lon, lat, updated_val) for (lon, lat, _), updated_val in zip(lon_lat_val_list, updated_values)]

# Example usage
lon_lat_val_list = [
    (34.05, -118.25, 10.0),  # Example point in Los Angeles
    (40.71, -74.01, 20.0),   # Example point in New York
    (37.77, -122.42, 15.0)   # Example point in San Francisco
]

for _ in range(10):
    lon_lat_val_list = add_perlin_noise(lon_lat_val_list, iterations=10, scale=0.1)
    print(lon_lat_val_list)

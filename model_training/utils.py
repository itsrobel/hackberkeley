import math
import copy
import branca
import branca.colormap as cm
# starters
import numpy as np
import pandas as pd
from folium.plugins import HeatMap, HeatMapWithTime
from shapely.geometry import Point, shape
import geopandas as gpd

# packages for fetching & files
import os
import folium

import geopandas as gpd
from shapely.geometry import Point, Polygon
import os
from pyproj import Transformer

os.environ['SHAPE_RESTORE_SHX'] = 'YES'

SHP_FILE = gpd.read_file('./CA_State.shp')
SHP_FILE = SHP_FILE.set_crs(epsg=3857)
SHP_FILE = SHP_FILE.to_crs(epsg=4326)
california_polygon = SHP_FILE.geometry.values[0]

def is_in_california(lon, lat):
    point = Point(lat, lon)
    res = california_polygon.contains(point)
    # print(res)
    return res

def circle_map(df, feature = 'latitude', save_name = './test_map.html'):
    colormap = cm.LinearColormap(["green", "blue", "yellow", "red"], 
                                index=np.linspace(df[feature].min(), df[feature].max(), 4),
                                vmin=df[feature].min(), vmax=df[feature].max())

    map_obj = folium.Map(prefer_canvas=True, width=500, height=500, location=[df.latitude[0], df.longitude[0]], zoom_start=6)

    for row in range(df.shape[0]):
        folium.CircleMarker(location=[df.loc[row, "latitude"], df.loc[row, "longitude"]],
                            radius=df.loc[row,feature] , fill=True,
                            color=colormap(df.loc[row, feature]),
                            fill_opacity=0.5, weight=1).add_to(map_obj)

    
    map_obj.add_child(colormap)
    map_obj.save(save_name)
    
    # print(map_obj.to_h)
    
def get_data(df, feature, sample_percent=30):
    # Normalize the feature column
    df[feature] = (
        (df[feature] - df[feature].min()) / 
        (df[feature].max() - df[feature].min())
    )
    
    # Randomly select X% of the data
    sample_size = int(sample_percent / 100 * df.shape[0])
    sampled_df = df.sample(n=sample_size, random_state=42).reset_index(drop=True)

    data = []
    for i in range(sampled_df.shape[0]):
        data.append([float(sampled_df['latitude'][i]), float(sampled_df['longitude'][i]), float(sampled_df[feature][i])])
    return data
    
def color_map(df, feature = 'latitude', save_name = './heatmap.html'):
    data = get_data(df, feature)
    m = folium.Map(prefer_canvas=True, width=500, height=500, radius=25, location=[df.latitude[0], df.longitude[0]], zoom_start=6)
    HeatMap(data, min_opacity=0.05, 
                max_opacity=0.9, 
                radius=15,
                use_local_extrema=False).add_to(m)
    m.save(save_name)
    
def live_update_map(df, timesteps = 100, feature = 'latitude', save_name = './time_heatmap.html'):
    m = folium.Map(prefer_canvas=True, width=500, height=500, radius=25, location=[df.latitude[0], df.longitude[0]], zoom_start=6)
            
    data = [get_data(df, feature)]
    mx = -1e9
    
    for _ in range(timesteps):
        nxt = copy.deepcopy(data[-1])

        for i in nxt:
            i[2] += (float(np.random.random()) - 0.5) * 100
            i[0] += (float(np.random.random()) - 0.5) * 0.7
            i[1] += (float(np.random.random()) - 0.5) * 0.7
            mx = max(mx, i[2])
        data.append(nxt)
        
    display_data = []
    
    for i in data:
        display_data.append([[point[0], point[1], math.exp(point[2] - mx)] for point in i if is_in_california(point[0], point[1])])
        
        print(math.exp(i[2] - mx))
        
    HeatMapWithTime(display_data, min_opacity=0.05, 
                max_opacity=0.9, 
                radius=15,
                use_local_extrema=False).add_to(m)
    m.save(save_name)
    
if __name__ == '__main__':
    df = pd.read_csv('/Users/timothygao/Downloads/hackberkeley/Fire_Dataset_NoScaleProcessed.csv')
    # df = pd.read_csv('/Users/timothygao/Downloads/hackberkeley/dataset/housing/housing.csv')
    # save_colormap(df, feature = 't2m')
    # color_map(df, feature = 't2m')
    live_update_map(df, timesteps=100, feature = 't2m')

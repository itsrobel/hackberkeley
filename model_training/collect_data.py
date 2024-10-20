import random
from datetime import datetime, timedelta
import pandas as pd
from satellite_api import main_query_function

START_DATE = datetime(2010, 1, 1)
END_DATE = datetime(2023, 12, 31)

LAT_MIN = 34.0
LAT_MAX = 35.0
LON_MIN = -121.0
LON_MAX = -120.0

SAMPLES = 1000

FEATURES = [
    'prectot', 'ps', 't10m', 'ws10m', 'diffuse_illuminance', 
    'direct_illuminance', 'gwetprof', 't2mdew', 'distroad1', 
    'z', 'ndvi', 'population_density', 'pres', 'ppt'
]

def random_date(start, end):
    """Generates a random datetime between `start` and `end`."""
    delta = end - start
    random_days = random.randint(0, delta.days)
    random_seconds = random.randint(0, 86400)  # seconds in a day
    return start + timedelta(days=random_days, seconds=random_seconds)

def random_location():
    """Generates random latitude and longitude within bounds."""
    lat = random.uniform(LAT_MIN, LAT_MAX)
    lon = random.uniform(LON_MIN, LON_MAX)
    return lat, lon

def collect_training_data(samples):
    """Collects the training data by querying the satellite API."""
    training_data = []

    for _ in range(samples):
        date = random_date(START_DATE, END_DATE)
        lat, lon = random_location()

        feature_data = {}
        for feature in FEATURES:
            try:
                result = main_query_function(feature, lon, lat, date)
                feature_data[feature] = result.get(feature, -9999)
            except Exception as e:
                print(f"Error querying {feature} for {lat}, {lon}, {date}: {e}")
                feature_data[feature] = -9999 

        
        future_date = date + timedelta(days=7)
        # future_date = date + timedelta(days=365) YEAR

        try:
            fire_result = main_query_function('fire', lon, lat, future_date)
            feature_data["Fire"] = 1 if fire_result.get("fire", 0) > 0 else 0
        except Exception as e:
            print(f"Error querying fire feature for {lat}, {lon}, {future_date}: {e}")
            feature_data["Fire"] = 0  

        training_data.append(feature_data)
    return training_data

def main():
    data = collect_training_data(SAMPLES)

    df = pd.DataFrame(data)

    df.to_csv("Fire_Dataset_NoScaleProcessed.csv", index=False)

    print(f"Data collection complete. {len(df)} samples collected.")
    print("Saved to fire_training_data_with_future.csv")

if __name__ == "__main__":
    main()

import ee
import pandas as pd
import math
from datetime import datetime, timedelta

ee.Initialize()

class SatelliteQuery:
    def __init__(self):
        self.max_range = 900
        self.scale = 4000 
        self.dataset = self._initialize_dataset()
    
    def _initialize_dataset(self):
        datasets = {
            'prectot': ee.ImageCollection("IDAHO_EPSCOR/GRIDMET"),
            'ps': ee.ImageCollection("NOAA/NWS/RTMA"),
            't10m': ee.ImageCollection("NOAA/NWS/RTMA"),
            'ws10m': ee.ImageCollection("IDAHO_EPSCOR/GRIDMET"),
            'diffuse_illuminance': ee.ImageCollection("MODIS/006/MCD19A2_GRANULES"),
            'direct_illuminance': ee.ImageCollection("MODIS/006/MCD19A2_GRANULES"),
            'gwetprof': ee.ImageCollection("IDAHO_EPSCOR/GRIDMET"),
            't2mdew': ee.ImageCollection("IDAHO_EPSCOR/GRIDMET"),
            'distroad1': ee.ImageCollection("MODIS/006/MCD12Q1"),
            'z': ee.ImageCollection("GRIDMET/DROUGHT"),
            'ndvi': ee.ImageCollection("MODIS/MYD09GA_006_NDVI"),
            'population_density': ee.ImageCollection("CIESIN/GPWv411/GPW_Population_Density"),
            'pres': ee.ImageCollection("NOAA/NWS/RTMA"),
            'ppt': ee.ImageCollection("NASA/ORNL/DAYMET_V4")
        }
        return datasets

    # Transforms client-side ee.Image.getRegion array to pandas.DataFrame.
    def ee_array_to_df(self, arr, list_of_bands):
        df = pd.DataFrame(arr)
        headers = df.iloc[0]
        df = pd.DataFrame(df.values[1:], columns=headers)

        for band in list_of_bands:
            df[band] = pd.to_numeric(df[band], errors='coerce')

        df['datetime'] = pd.to_datetime(df['time'], unit='ms')
        return df[['time', 'datetime', *list_of_bands]]

    def getDate(self, dt, freq):
        sub = timedelta(freq)
        return [dt - sub, dt]

    def request(self, i_date, f_date, lon, lat, feature_array):
        cur = self.dataset.select(feature_array).filter(ee.Filter.date(i_date, f_date))
        pos = ee.Geometry.Point(lon, lat)
        res = cur.getRegion(pos, self.scale).getInfo()
        return self.ee_array_to_df(res, feature_array)

    def query(self, lon, lat, dat, daterange, feature_array):
        try:       
            i_d, f_d = self.getDate(dat, daterange)
            cur = self.request(i_d, f_d, lon, lat, feature_array)
            temp, nans = self._initialize_temp_and_nan(feature_array)
            temp_date = self._initialize_temp_date(feature_array)

            for i in range(len(cur)):
                for j in feature_array:
                    if cur[j][i] == cur[j][i] and not math.isnan(cur[j][i]):
                        nans, temp = self._update_temp(cur, j, i, temp, temp_date, nans)

            if float(nans) != 0.0 and float(daterange) != float(self.max_range):
                raise Exception("NaN value detected -> try larger date range")
            
            return temp
        except Exception as e:
            print(f"Error on querying:::::: {str(e)} {lon} bad {lat} {daterange}")
            if daterange == self.max_range:
                return {j: -9999 for j in feature_array}
            
            return self.query(lon, lat, dat, min(2 * daterange, self.max_range), feature_array)

    def _initialize_temp_and_nan(self, feature_array):
        temp = {j: -9999 for j in feature_array}
        nans = len(feature_array)
        return temp, nans

    def _initialize_temp_date(self, feature_array):
        return {j: (datetime(2000, 1, 1), 1) for j in feature_array}

    def _update_temp(self, cur, j, i, temp, temp_date, nans):
        if float(temp[j]) == -9999:
            nans -= 1
        curdt = cur['datetime'][i].to_pydatetime()
        if (curdt.year != temp_date[j][0].year or 
            curdt.month != temp_date[j][0].month or
            curdt.day != temp_date[j][0].day):
            temp_date[j] = (curdt, 1)
            temp[j] = cur[j][i]
        else:
            temp[j] = (temp[j] * temp_date[j][1] + cur[j][i]) / (temp_date[j][1] + 1)
            temp_date[j] = (temp_date[j][0], temp_date[j][1] + 1)
        return nans, temp

def main_query_function(feature, lon, lat, datetime):
    sat_query = SatelliteQuery()

    feature_map = {
        'prectot': ['prectot'],
        'ps': ['ps'],
        't10m': ['t10m'],
        'ws10m': ['ws10m'],
        'diffuse_illuminance': ['diffuse_illuminance'],
        'direct_illuminance': ['direct_illuminance'],
        'gwetprof': ['gwetprof'],
        't2mdew': ['t2mdew'],
        'distroad1': ['distroad1'],
        'z': ['z'],
        'ndvi': ['ndvi'],
        'population_density': ['population_density'],
        'pres': ['pres'],
        'ppt': ['ppt'],
        'fire' : ['fire']
    }
    
    feature_array = feature_map.get(feature, [])
    if not feature_array:
        raise ValueError(f"Feature {feature} not supported")
    
    result = sat_query.query(lon, lat, datetime, daterange=1, feature_array=feature_array)
    return result


if __name__ == "__main__":
    feature = 'ndvi'
    lon = -120.3239
    lat = 34.9847
    date = datetime(2016, 7, 9)
    
    result = main_query_function(feature, lon, lat, date)
    print(result)

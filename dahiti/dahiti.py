import requests

API_URL = 'http://dahiti.dgfi.tum.de/api/v1/'
COORDS = ['longitude', 'latitude']


def list_targets(username, password, **kw):
    """Query DAHITI API

    Parameters
    ----------
    username, password : str
        credentials
    kw : additional keyword arguments
        passed as payload
        see API docs at http://dahiti.dgfi.tum.de/en/api/doc/

    Returns
    -------
    list of dict
        results from query
    """
    kw['username'] = username
    kw['password'] = password
    kw['action'] = 'list-targets'
    response = requests.get(API_URL, params=kw)
    response.raise_for_status()
    results = response.json()
    return results


def download(dahiti_id, username, password, **kw):
    """Download DAHITI data

    Parameters
    ----------
    dahiti_id : str or int
        id of target to download
    username, password : str
        credentials
    kw : additional keyword arguments
        passed as payload
        see API docs at http://dahiti.dgfi.tum.de/en/api/doc/

    Returns
    -------
    list of dict
        data records
    """
    kw['username'] = username
    kw['password'] = password
    kw['action'] = 'download'
    kw['dahiti_id'] = dahiti_id
    response = requests.get(API_URL, params=kw)
    response.raise_for_status()
    results = response.json()
    return results


def results_to_dataframe(results):
    """Convert query results to Pandas dataframe

    Parameters
    ----------
    results : list of dict
        as returned by `list_targets`

    Returns
    -------
    pandas.DataFrame
        converted results
    """
    import pandas as pd
    df = pd.DataFrame(results).set_index('id')
    df[COORDS] = pd.to_numeric(df[COORDS])
    return df


def results_to_geodataframe(results):
    """Convert query results to GeoPandas geodataframe

    Parameters
    ----------
    results : list of dict
        as returned by `list_targets`

    Returns
    -------
    geopandas.GeoDataFrame
        converted results
    """
    import geopandas as gpd
    import shapely.geometry
    df = results_to_dataframe(results)
    xy = df[COORDS].values
    geometry = [shapely.geometry.Point(x, y) for x, y in xy]
    gdf = gpd.GeoDataFrame(
        df.drop(COORDS, axis='columns'),
        geometry=geometry,
        crs={'init': 'epsg:4326'})
    return gdf


def data_to_dataframe(data):
    """Convert data to Pandas dataframe

    Parameters
    ----------
    data : list of dict
        as returned by `download`

    Returns
    -------
    pandas.DataFrame
        converted data
    """
    import pandas as pd
    df = pd.DataFrame(data)
    df['date'] = df['date'].apply(pd.to_datetime)
    df = df.set_index('date')
    for name in ['error', 'height']:
        df[name] = pd.to_numeric(df[name])
    return df

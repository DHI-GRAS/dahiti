import pytest


def test_list_targets(dahiti_credentials, small_query):
    from dahiti import dahiti
    kw = dahiti_credentials.copy()
    kw.update(small_query)
    results = dahiti.list_targets(**kw)
    assert isinstance(results, list)
    assert len(results) > 0
    assert 'id' in results[0]


def test_download(dahiti_credentials, small_query):
    from dahiti import dahiti
    kw = dahiti_credentials.copy()
    kw.update(small_query)
    results = dahiti.list_targets(**kw)
    dahiti_id = results[0]['id']
    data = dahiti.download(dahiti_id, **dahiti_credentials)
    assert isinstance(data, list)
    assert isinstance(data[0], dict)


def test_results_to_dataframe(dahiti_credentials, small_query):
    pandas = pytest.importorskip('pandas')
    from dahiti import dahiti
    kw = dahiti_credentials.copy()
    kw.update(small_query)
    results = dahiti.list_targets(**kw)
    print(results)
    assert len(results) > 0
    df = dahiti.results_to_dataframe(results)
    assert isinstance(df, pandas.DataFrame)


def test_results_to_geodataframe(dahiti_credentials, small_query):
    geopandas = pytest.importorskip('geopandas')
    from dahiti import dahiti
    kw = dahiti_credentials.copy()
    kw.update(small_query)
    results = dahiti.list_targets(**kw)
    print(results)
    assert len(results) > 0
    gdf = dahiti.results_to_geodataframe(results)
    assert isinstance(gdf, geopandas.GeoDataFrame)


def test_data_to_dataframe(dahiti_credentials, small_query):
    pandas = pytest.importorskip('pandas')
    from dahiti import dahiti
    kw = dahiti_credentials.copy()
    kw.update(small_query)
    results = dahiti.list_targets(**kw)
    dahiti_id = results[0]['id']
    data = dahiti.download(dahiti_id, **dahiti_credentials)
    df = dahiti.data_to_dataframe(data)
    assert isinstance(df, pandas.DataFrame)

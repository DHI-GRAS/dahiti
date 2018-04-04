

def test_list_targets(dahiti_credentials):
    from dahiti import dahiti
    results = dahiti.list_targets(basin='Amazon', **dahiti_credentials)
    assert isinstance(results, list)
    assert len(results) > 0
    assert 'dahiti_id' in results[0]


def test_download(dahiti_credentials):
    from dahiti import dahiti
    results = dahiti.list_targets(basin='Amazon', **dahiti_credentials)
    dahiti_id = results[0]['dahiti_id']
    dahiti.download(dahiti_id, **dahiti_credentials)

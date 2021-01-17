import json
def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.data == b"Online!"

def test_pads(app, client):
    res = client.get('/pads')
    assert res.status_code == 200
    assert type(res.data) == type(res.data)

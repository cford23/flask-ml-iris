def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'hello': 'world'}

    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json == {'hello': 'world'}

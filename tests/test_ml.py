def test_iris(client):
    response = client.get('/iris')
    assert response.status_code == 200
    assert response.json == {'message': 'iris ml model'}

from fastapi.testclient import TestClient
from Back.api import app 

client = TestClient(app)

def test_get_list_cours():

    response = client.get("/cours/getListCours")
    
    assert response.status_code == 200
    
    assert isinstance(response.json(), list)
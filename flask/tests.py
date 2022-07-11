import requests


if __name__ == "__main__":
    response = requests.get("http://127.0.0.1:5000/")
    assert response.status_code == 200

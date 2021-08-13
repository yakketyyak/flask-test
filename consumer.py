import requests

api_url = "https://jsonplaceholder.typicode.com/todos/"
def test_get_request():
    response = requests.get(api_url + "1")
    print(response.json())
    print(response.status_code)


def test_post_request():
    todo = {"userId": 1, "title": "Buy milk", "completed": False}
    response = requests.post(api_url, json=todo)
    print(response.json())
    print(response.status_code)

if __name__ == '__main__':
    test_get_request()
    test_post_request()

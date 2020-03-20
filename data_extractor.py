import requests
def get_emp_data():
    url = "http://dummy.restapiexample.com/api/v1/employees"

    headers = {
        'cache-control': "no-cache",
        'postman-token': "2e310b71-6596-9b78-0529-55f7423f758a"
    }

    response = requests.request("GET", url)

    print(response.text)
    return response.content

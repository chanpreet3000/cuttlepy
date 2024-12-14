from cuttlepy import get, post, CuttleClient


def print_response(response, method):
    print(f"\n--- {method} Response ---")
    print(f"Status Code: {response.status_code}")
    print("Headers:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")
    print("\nContent:")
    print(response.json())


# Using normal methods
print("Using normal methods:")

# GET request
response = get('https://httpbin.org/get')
print_response(response, "GET")

# POST request
data = {"key": "value"}
response = post('https://httpbin.org/post', json=data)
print_response(response, "POST")

# Using CuttleClient
print("\nUsing CuttleClient:")

client = CuttleClient()

# GET request
response = client.get('https://httpbin.org/get')
print_response(response, "GET")

# POST request
response = client.post('https://httpbin.org/post', json=data)
print_response(response, "POST")

# Demonstrating client reuse for multiple requests
print("\nDemonstrating client reuse:")

# GET request with parameters
response = client.get('https://httpbin.org/get', params={"param1": "value1", "param2": "value2"})
print_response(response, "GET with params")

# POST request with custom headers
headers = {"X-Custom-Header": "CustomValue"}
response = client.post('https://httpbin.org/post', json=data, headers=headers)
print_response(response, "POST with custom headers")

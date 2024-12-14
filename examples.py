from cuttlepy import get

# Make a GET request to a sample API
response = get('https://jsonplaceholder.typicode.com/todos/1')

# Print the response status code
print(f"Status Code: {response.status_code}")

# Print the response headers
print("Headers:")
for key, value in response.headers.items():
    print(f"  {key}: {value}")

# Print the response content
print("\nContent:")
print(response.json())

# Demonstrate error handling
try:
    response.raise_for_status()
    print("\nRequest was successful!")
except Exception as e:
    print(f"\nAn error occurred: {e}")

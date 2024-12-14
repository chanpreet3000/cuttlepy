import cuttlepy

response = cuttlepy.get(
    'https://httpbin.org/get',
    timeout=15
)

response.raise_for_status()
print(response.status_code)

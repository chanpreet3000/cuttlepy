from cuttlepy import CuttleClient

client = CuttleClient(
    timeout=10,
)

response = client.get("https://httpbin.org/get")
response.raise_for_status()
print(response.status_code)

# CuttlePy

A fully typed Python HTTP client built on top of [primp](https://github.com/deedy5/primp) - the fastest Python HTTP
client with browser impersonation capabilities.

## Acknowledgements

This project is powered by the excellent [primp](https://github.com/deedy5/primp) library. CuttlePy provides type hints
and a more structured interface while utilizing primp's powerful features under the hood.

## Features

- Full type hints support for better IDE integration
- All the power of primp with a typed interface
- Browser impersonation capabilities
- Support for all HTTP methods
- Comprehensive response object with typed properties

## Installation

```bash
pip install cuttlepy
```

## Usage

### Making Requests

```python
from cuttlepy import get, CuttleClient

# Using convenience functions
response = get("https://api.example.com/data")
print(response.json())

# Using the client
client = CuttleClient(
    impersonate="chrome_131",
    timeout=30
)
response = client.get("https://api.example.com/data")
```

### Response Object

The `CuttleResponse` object provides typed access to response data:

```python
response = get("https://api.example.com/data")

# Access response properties with proper typing
content: bytes = response.content
status_code: int = response.status_code
headers: Dict[str, str] = response.headers
cookies: CookieJar = response.cookies
text: str = response.text

# Parse JSON with proper typing
data: Any = response.json()
```

### HTTP Methods

All standard HTTP methods are supported with full type hints:

```python
from cuttlepy import CuttleClient

client = CuttleClient()

# GET request
response = client.get(
    url="https://api.example.com/data",
    params={"key": "value"},
    headers={"Authorization": "Bearer token"}
)

# POST request with JSON
response = client.post(
    url="https://api.example.com/data",
    json={"key": "value"}
)

# POST with form data
response = client.post(
    url="https://api.example.com/data",
    data={"key": "value"}
)

# POST with files
response = client.post(
    url="https://api.example.com/data",
    files={"file": open("document.pdf", "rb").read()}
)
```

### Authentication

```python
# Basic auth
client = CuttleClient(auth=("username", "password"))

# Bearer token
client = CuttleClient(auth_bearer="your-token")
```

### Browser Impersonation

```python
client = CuttleClient(impersonate="chrome_131")
```

## 📖 API Reference

### CuttleClient

```python
class CuttleClient:
    def __init__(
            self,
            *,
            auth: Optional[Tuple[str, str]] = None,
            auth_bearer: Optional[str] = None,
            params: Optional[Dict[str, str]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            timeout: float = 30,
            cookie_store: bool = True,
            referer: bool = True,
            proxy: Optional[str] = None,
            impersonate: Optional[str] = None,
            follow_redirects: bool = True,
            max_redirects: int = 20,
            verify: bool = True,
            ca_cert_file: Optional[str] = None,
            http1: Optional[bool] = None,
            http2: Optional[bool] = None
    ): ...
```

### CuttleResponse

```python
class CuttleResponse:
    @property
    def content(self) -> bytes: ...

    @property
    def cookies(self) -> CookieJar: ...

    @property
    def encoding(self) -> Optional[str]: ...

    @property
    def headers(self) -> Dict[str, str]: ...

    @property
    def status_code(self) -> int: ...

    @property
    def text(self) -> str: ...

    def json(self) -> Any: ...

    @property
    def url(self) -> str: ...

    def raise_for_status(self) -> None: ...
```

## License

MIT License

## Links

- [primp Documentation](https://github.com/deedy5/primp) - The underlying HTTP client used by CuttlePy

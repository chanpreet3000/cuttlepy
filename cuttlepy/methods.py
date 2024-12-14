from typing import Any, Optional, Dict, Tuple, Union, List
from .client import CuttleClient


def get(
        url: str,
        *,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        cookies: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, Optional[str]]] = None,
        auth_bearer: Optional[str] = None,
        timeout: Optional[float] = None,
        proxy: Optional[str] = None,
        impersonate: Optional[str] = None,
        verify: Optional[bool] = None,
):
    """
    Send a GET request to the specified URL.

    Args:
        url (str): The URL to send the GET request to.
        params (Optional[Dict[str, str]]): Query parameters to include in the request URL.
        headers (Optional[Dict[str, str]]): HTTP headers to include in the request.
        cookies (Optional[Dict[str, str]]): Cookies to include in the request.
        auth (Optional[Tuple[str, Optional[str]]]): Authentication credentials (username, password).
        auth_bearer (Optional[str]): Bearer token for authentication.
        timeout (Optional[float]): Request timeout in seconds.
        proxy (Optional[str]): Proxy server URL.
        impersonate (Optional[str]): Browser to impersonate in the request.
        verify (Optional[bool]): Whether to verify SSL certificates.

    Returns:
        CuttleResponse: The response from the server.
    """
    client = CuttleClient(
        auth=auth,
        auth_bearer=auth_bearer,
        proxy=proxy,
        impersonate=impersonate,
        verify=verify,
    )
    return client.get(
        url,
        params=params,
        headers=headers,
        cookies=cookies,
        auth=auth,
        auth_bearer=auth_bearer,
        timeout=timeout
    )


def head(
        url: str,
        *,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        cookies: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, Optional[str]]] = None,
        auth_bearer: Optional[str] = None,
        timeout: Optional[float] = None,
        proxy: Optional[str] = None,
        impersonate: Optional[str] = None,
        verify: Optional[bool] = None,
):
    """
    Send a HEAD request to the specified URL.

    Args:
        url (str): The URL to send the HEAD request to.
        params (Optional[Dict[str, str]]): Query parameters to include in the request URL.
        headers (Optional[Dict[str, str]]): HTTP headers to include in the request.
        cookies (Optional[Dict[str, str]]): Cookies to include in the request.
        auth (Optional[Tuple[str, Optional[str]]]): Authentication credentials (username, password).
        auth_bearer (Optional[str]): Bearer token for authentication.
        timeout (Optional[float]): Request timeout in seconds.
        proxy (Optional[str]): Proxy server URL.
        impersonate (Optional[str]): Browser to impersonate in the request.
        verify (Optional[bool]): Whether to verify SSL certificates.

    Returns:
        CuttleResponse: The response from the server.
    """
    client = CuttleClient(
        auth=auth,
        auth_bearer=auth_bearer,
        proxy=proxy,
        impersonate=impersonate,
        verify=verify,
    )
    return client.head(
        url,
        params=params,
        headers=headers,
        cookies=cookies,
        auth=auth,
        auth_bearer=auth_bearer,
        timeout=timeout
    )


def options(
        url: str,
        *,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        cookies: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, Optional[str]]] = None,
        auth_bearer: Optional[str] = None,
        timeout: Optional[float] = None,
        proxy: Optional[str] = None,
        impersonate: Optional[str] = None,
        verify: Optional[bool] = None,
):
    """
    Send an OPTIONS request to the specified URL.

    Args:
        url (str): The URL to send the OPTIONS request to.
        params (Optional[Dict[str, str]]): Query parameters to include in the request URL.
        headers (Optional[Dict[str, str]]): HTTP headers to include in the request.
        cookies (Optional[Dict[str, str]]): Cookies to include in the request.
        auth (Optional[Tuple[str, Optional[str]]]): Authentication credentials (username, password).
        auth_bearer (Optional[str]): Bearer token for authentication.
        timeout (Optional[float]): Request timeout in seconds.
        proxy (Optional[str]): Proxy server URL.
        impersonate (Optional[str]): Browser to impersonate in the request.
        verify (Optional[bool]): Whether to verify SSL certificates.

    Returns:
        CuttleResponse: The response from the server.
    """
    client = CuttleClient(
        auth=auth,
        auth_bearer=auth_bearer,
        proxy=proxy,
        impersonate=impersonate,
        verify=verify,
    )
    return client.options(
        url,
        params=params,
        headers=headers,
        cookies=cookies,
        auth=auth,
        auth_bearer=auth_bearer,
        timeout=timeout
    )


def delete(
        url: str,
        *,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        cookies: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, Optional[str]]] = None,
        auth_bearer: Optional[str] = None,
        timeout: Optional[float] = None,
        proxy: Optional[str] = None,
        impersonate: Optional[str] = None,
        verify: Optional[bool] = None,
):
    """
    Send a DELETE request to the specified URL.

    Args:
        url (str): The URL to send the DELETE request to.
        params (Optional[Dict[str, str]]): Query parameters to include in the request URL.
        headers (Optional[Dict[str, str]]): HTTP headers to include in the request.
        cookies (Optional[Dict[str, str]]): Cookies to include in the request.
        auth (Optional[Tuple[str, Optional[str]]]): Authentication credentials (username, password).
        auth_bearer (Optional[str]): Bearer token for authentication.
        timeout (Optional[float]): Request timeout in seconds.
        proxy (Optional[str]): Proxy server URL.
        impersonate (Optional[str]): Browser to impersonate in the request.
        verify (Optional[bool]): Whether to verify SSL certificates.

    Returns:
        CuttleResponse: The response from the server.
    """
    client = CuttleClient(
        auth=auth,
        auth_bearer=auth_bearer,
        proxy=proxy,
        impersonate=impersonate,
        verify=verify,
    )
    return client.delete(
        url,
        params=params,
        headers=headers,
        cookies=cookies,
        auth=auth,
        auth_bearer=auth_bearer,
        timeout=timeout
    )


def post(
        url: str,
        *,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        cookies: Optional[Dict[str, str]] = None,
        content: Optional[bytes] = None,
        data: Optional[Any] = None,
        json: Optional[Any] = None,
        files: Optional[Dict[str, Union[bytes, List[bytes]]]] = None,
        auth: Optional[Tuple[str, Optional[str]]] = None,
        auth_bearer: Optional[str] = None,
        timeout: Optional[float] = None,
        proxy: Optional[str] = None,
        impersonate: Optional[str] = None,
        verify: Optional[bool] = None,
):
    """
    Send a POST request to the specified URL.

    Args:
        url (str): The URL to send the POST request to.
        params (Optional[Dict[str, str]]): Query parameters to include in the request URL.
        headers (Optional[Dict[str, str]]): HTTP headers to include in the request.
        cookies (Optional[Dict[str, str]]): Cookies to include in the request.
        content (Optional[bytes]): Raw bytes to include in the request body.
        data (Optional[Any]): Form data to include in the request body.
        json (Optional[Any]): JSON data to include in the request body.
        files (Optional[Dict[str, Union[bytes, List[bytes]]]]): Files to upload.
        auth (Optional[Tuple[str, Optional[str]]]): Authentication credentials (username, password).
        auth_bearer (Optional[str]): Bearer token for authentication.
        timeout (Optional[float]): Request timeout in seconds.
        proxy (Optional[str]): Proxy server URL.
        impersonate (Optional[str]): Browser to impersonate in the request.
        verify (Optional[bool]): Whether to verify SSL certificates.

    Returns:
        CuttleResponse: The response from the server.
    """
    client = CuttleClient(
        auth=auth,
        auth_bearer=auth_bearer,
        proxy=proxy,
        impersonate=impersonate,
        verify=verify,
    )
    return client.post(
        url,
        params=params,
        headers=headers,
        cookies=cookies,
        content=content,
        data=data,
        json=json,
        files=files,
        auth=auth,
        auth_bearer=auth_bearer,
        timeout=timeout
    )


def put(
        url: str,
        *,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        cookies: Optional[Dict[str, str]] = None,
        content: Optional[bytes] = None,
        data: Optional[Any] = None,
        json: Optional[Any] = None,
        files: Optional[Dict[str, Union[bytes, List[bytes]]]] = None,
        auth: Optional[Tuple[str, Optional[str]]] = None,
        auth_bearer: Optional[str] = None,
        timeout: Optional[float] = None,
        proxy: Optional[str] = None,
        impersonate: Optional[str] = None,
        verify: Optional[bool] = None,
):
    """
    Send a PUT request to the specified URL.

    Args:
        url (str): The URL to send the PUT request to.
        params (Optional[Dict[str, str]]): Query parameters to include in the request URL.
        headers (Optional[Dict[str, str]]): HTTP headers to include in the request.
        cookies (Optional[Dict[str, str]]): Cookies to include in the request.
        content (Optional[bytes]): Raw bytes to include in the request body.
        data (Optional[Any]): Form data to include in the request body.
        json (Optional[Any]): JSON data to include in the request body.
        files (Optional[Dict[str, Union[bytes, List[bytes]]]]): Files to upload.
        auth (Optional[Tuple[str, Optional[str]]]): Authentication credentials (username, password).
        auth_bearer (Optional[str]): Bearer token for authentication.
        timeout (Optional[float]): Request timeout in seconds.
        proxy (Optional[str]): Proxy server URL.
        impersonate (Optional[str]): Browser to impersonate in the request.
        verify (Optional[bool]): Whether to verify SSL certificates.

    Returns:
        CuttleResponse: The response from the server.
    """
    client = CuttleClient(
        auth=auth,
        auth_bearer=auth_bearer,
        proxy=proxy,
        impersonate=impersonate,
        verify=verify,
    )
    return client.put(
        url,
        params=params,
        headers=headers,
        cookies=cookies,
        content=content,
        data=data,
        json=json,
        files=files,
        auth=auth,
        auth_bearer=auth_bearer,
        timeout=timeout
    )


def patch(
        url: str,
        *,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        cookies: Optional[Dict[str, str]] = None,
        content: Optional[bytes] = None,
        data: Optional[Any] = None,
        json: Optional[Any] = None,
        files: Optional[Dict[str, Union[bytes, List[bytes]]]] = None,
        auth: Optional[Tuple[str, Optional[str]]] = None,
        auth_bearer: Optional[str] = None,
        timeout: Optional[float] = None,
        proxy: Optional[str] = None,
        impersonate: Optional[str] = None,
        verify: Optional[bool] = None,
):
    """
    Send a PATCH request to the specified URL.

    Args:
        url (str): The URL to send the PATCH request to.
        params (Optional[Dict[str, str]]): Query parameters to include in the request URL.
        headers (Optional[Dict[str, str]]): HTTP headers to include in the request.
        cookies (Optional[Dict[str, str]]): Cookies to include in the request.
        content (Optional[bytes]): Raw bytes to include in the request body.
        data (Optional[Any]): Form data to include in the request body.
        json (Optional[Any]): JSON data to include in the request body.
        files (Optional[Dict[str, Union[bytes, List[bytes]]]]): Files to upload.
        auth (Optional[Tuple[str, Optional[str]]]): Authentication credentials (username, password).
        auth_bearer (Optional[str]): Bearer token for authentication.
        timeout (Optional[float]): Request timeout in seconds.
        proxy (Optional[str]): Proxy server URL.
        impersonate (Optional[str]): Browser to impersonate in the request.
        verify (Optional[bool]): Whether to verify SSL certificates.

    Returns:
        CuttleResponse: The response from the server.
    """
    client = CuttleClient(
        auth=auth,
        auth_bearer=auth_bearer,
        proxy=proxy,
        impersonate=impersonate,
        verify=verify,
    )
    return client.patch(
        url,
        params=params,
        headers=headers,
        cookies=cookies,
        content=content,
        data=data,
        json=json,
        files=files,
        auth=auth,
        auth_bearer=auth_bearer,
        timeout=timeout
    )

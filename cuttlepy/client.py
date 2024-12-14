from typing import Any, Optional, Dict, Tuple, Union, List
from primp import Client as PrimpClient
from .response import CuttleResponse


class CuttleClient:
    """
    A client for making HTTP requests using the PrimpClient as a backend.

    This class provides methods for various HTTP operations (GET, POST, PUT, etc.)
    and returns responses wrapped in CuttleResponse objects.
    """

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
    ):
        """
        Initialize a new CuttleClient instance.

        Args:
            auth (Optional[Tuple[str, str]]): Basic authentication credentials (username, password).
            auth_bearer (Optional[str]): Bearer token for authentication.
            params (Optional[Dict[str, str]]): Default query parameters to be sent with each request.
            headers (Optional[Dict[str, str]]): Default headers to be sent with each request.
            cookies (Optional[Dict[str, str]]): Default cookies to be sent with each request.
            timeout (float): Default timeout for requests in seconds.
            cookie_store (bool): Whether to enable cookie storage between requests.
            referer (bool): Whether to automatically set the Referer header.
            proxy (Optional[str]): Proxy server URL.
            impersonate (Optional[str]): Browser to impersonate in requests.
            follow_redirects (bool): Whether to automatically follow redirects.
            max_redirects (int): Maximum number of redirects to follow.
            verify (bool): Whether to verify SSL certificates.
            ca_cert_file (Optional[str]): Path to a CA certificate file.
            http1 (Optional[bool]): Whether to enable HTTP/1.1.
            http2 (Optional[bool]): Whether to enable HTTP/2.
        """
        self._client = PrimpClient(
            auth=auth,
            auth_bearer=auth_bearer,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            cookie_store=cookie_store,
            referer=referer,
            proxy=proxy,
            impersonate=impersonate,
            follow_redirects=follow_redirects,
            max_redirects=max_redirects,
            verify=verify,
            ca_cert_file=ca_cert_file,
            http1=http1,
            http2=http2
        )

    def get(
            self,
            url: str,
            *,
            params: Optional[Dict[str, str]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, Optional[str]]] = None,
            auth_bearer: Optional[str] = None,
            timeout: Optional[float] = None,
    ) -> CuttleResponse:
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

        Returns:
            CuttleResponse: The response from the server.
        """
        response = self._client.get(
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            auth_bearer=auth_bearer,
            timeout=timeout
        )
        return CuttleResponse(response)

    def head(
            self,
            url: str,
            *,
            params: Optional[Dict[str, str]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, Optional[str]]] = None,
            auth_bearer: Optional[str] = None,
            timeout: Optional[float] = None,
    ) -> CuttleResponse:
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

        Returns:
            CuttleResponse: The response from the server.
        """
        response = self._client.head(
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            auth_bearer=auth_bearer,
            timeout=timeout
        )
        return CuttleResponse(response)

    def options(
            self,
            url: str,
            *,
            params: Optional[Dict[str, str]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, Optional[str]]] = None,
            auth_bearer: Optional[str] = None,
            timeout: Optional[float] = None,
    ) -> CuttleResponse:
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

        Returns:
            CuttleResponse: The response from the server.
        """
        response = self._client.options(
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            auth_bearer=auth_bearer,
            timeout=timeout
        )
        return CuttleResponse(response)

    def delete(
            self,
            url: str,
            *,
            params: Optional[Dict[str, str]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, Optional[str]]] = None,
            auth_bearer: Optional[str] = None,
            timeout: Optional[float] = None,
    ) -> CuttleResponse:
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

        Returns:
            CuttleResponse: The response from the server.
        """
        response = self._client.delete(
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            auth_bearer=auth_bearer,
            timeout=timeout
        )
        return CuttleResponse(response)

    def post(
            self,
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
    ) -> CuttleResponse:
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

        Returns:
            CuttleResponse: The response from the server.
        """
        response = self._client.post(
            url=url,
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
        return CuttleResponse(response)

    def put(
            self,
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
    ) -> CuttleResponse:
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

        Returns:
            CuttleResponse: The response from the server.
        """
        response = self._client.put(
            url=url,
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
        return CuttleResponse(response)

    def patch(
            self,
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
    ) -> CuttleResponse:
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

        Returns:
            CuttleResponse: The response from the server.
        """
        response = self._client.patch(
            url=url,
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
        return CuttleResponse(response)

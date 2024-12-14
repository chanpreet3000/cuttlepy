from email.message import Message
from typing import Any, Dict, Optional
from http.cookiejar import CookieJar
from urllib.error import HTTPError


class CuttleResponse:
    """
    A wrapper class for PrimpResponse that provides access to various response attributes and methods.
    """

    def __init__(self, primp_response: Any):
        """
        Initialize the CuttleResponse with a PrimpResponse object.

        Args:
            primp_response (Any): The PrimpResponse object to wrap.
        """
        self._primp_response = primp_response

    @property
    def content(self) -> bytes:
        """
        Get the content of the response in bytes.

        Returns:
            bytes: The response content.
        """
        return self._primp_response.content

    @property
    def cookies(self) -> CookieJar:
        """
        Get the cookies from the response.

        Returns:
            CookieJar: The response cookies.
        """
        return self._primp_response.cookies

    @property
    def encoding(self) -> Optional[str]:
        """
        Get the encoding of the response content.

        Returns:
            Optional[str]: The response encoding, if available.
        """
        return self._primp_response.encoding

    @property
    def headers(self) -> Dict[str, str]:
        """
        Get the headers of the response.

        Returns:
            Dict[str, str]: The response headers.
        """
        return self._primp_response.headers

    @property
    def status_code(self) -> int:
        """
        Get the HTTP status code of the response.

        Returns:
            int: The response status code.
        """
        return self._primp_response.status_code

    @property
    def text(self) -> str:
        """
        Get the content of the response as a string.

        Returns:
            str: The response content as text.
        """
        return self._primp_response.text

    def json(self) -> Any:
        """
        Parse the response content as JSON.

        Returns:
            Any: The parsed JSON content.

        Raises:
            ValueError: If the response body does not contain valid JSON.
        """
        return self._primp_response.json()

    @property
    def text_markdown(self) -> str:
        """
        Get the content of the response as markdown text.

        Returns:
            str: The response content as markdown.
        """
        return self._primp_response.text_markdown

    @property
    def text_plain(self) -> str:
        """
        Get the content of the response as plain text.

        Returns:
            str: The response content as plain text.
        """
        return self._primp_response.text_plain

    @property
    def text_rich(self) -> str:
        """
        Get the content of the response as rich text.

        Returns:
            str: The response content as rich text.
        """
        return self._primp_response.text_rich

    @property
    def url(self) -> str:
        """
        Get the URL of the response.

        Returns:
            str: The response URL.
        """
        return self._primp_response.url

    def raise_for_status(self) -> None:
        """
        Raise an HTTPError if the HTTP request returned an unsuccessful status code.

        Raises:
            HTTPError: If the response status code is 4xx or 5xx.
        """
        if 400 <= self.status_code < 600:
            error_msg = f"Error for url: {self.url}"
            raise HTTPError(self.url, self.status_code, error_msg, hdrs=Message(), fp=None)

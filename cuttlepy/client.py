from typing import Any, Optional, Dict, Tuple, Union, List
from primp import Client as PrimpClient
from .response import CuttleResponse


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
    ):
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

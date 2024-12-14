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

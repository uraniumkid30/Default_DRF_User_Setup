from typing import Union
from logging import Logger

from requests import request
import requests.exceptions as req_exceptions

from .exceptions import (
    UnExpectedStatusCode,
    TooManyRequests,
    NotFoundException,
    BadRequestException,
)
from .enums import (
    HttpMethods,
    ExpectedStatusCode,
    RequestStatusCode,
    RequestTimeout,
)


class BaseClient:
    LOG_NAME: str = ""
    BASE_URL: str = ""
    DATE_FORMAT = "%Y-%m-%d"
    MAX_RETRY: int = 5
    MAX_LIMIT: int = 50
    CALLS_PER_MINUTE: int = 200

    def __init__(self, *args, **kwargs):
        self.logger: Logger = self.get_logger(**kwargs)

    def set_base_url(self) -> str:
        """
        Updates and Returns the base url of Application api
        @return: str
        """
        raise NotImplementedError()

    def get_logger(self, **kwargs) -> Logger:
        """Get the logger to use here"""
        raise NotImplementedError()

    @staticmethod
    def format_response(response) -> Union[dict, str]:
        try:
            data = response.json()
        except Exception as err:
            print(f"Error getting json format of response {err}")
            data = response.text
        finally:
            return data

    @staticmethod
    def raise_appropriate_exception_if_needed(response, expected_status_code=None):
        """
        Raises an appropriate exception for different status codes
        Exceptions may be used to handle the flow of code in callers.
        @raises: Exception
        """
        _status_code = int(response.status_code)
        response_data = BaseClient.format_response(response)
        if _status_code == RequestStatusCode.HTTP_400_BAD_REQUEST:
            raise BadRequestException(response_data)
        if _status_code == RequestStatusCode.HTTP_404_NOT_FOUND:
            raise NotFoundException(response_data)
        if _status_code == RequestStatusCode.HTTP_429_TOO_MANY_REQUESTS:
            raise TooManyRequests(
                "Too many requests. Try sleeping for 1 minutes."
            )
        if expected_status_code:
            if _status_code not in expected_status_code:
                raise UnExpectedStatusCode(
                    f"Was expecting status code {expected_status_code} but I have received {_status_code}."
                    f"{response_data}."
                )

    def _generate_params(
        self,
        raw_params={}
    ) -> dict:
        """
        generates parameters from provided values
        """
        params = {}
        if raw_params:
            params.update(raw_params)
        return params

    def make_request(
        self,
        url: str,
        method: str = HttpMethods.GET,
        extra_headers: dict = None,
        data=None,
        json_=None,
        params: dict = {},
        headers: dict = {},
        computed_url: str = "",
        timeout: RequestTimeout = RequestTimeout(),
        raise_exceptions=True,
    ):
        """
        Makes request to Any server for a Legal url
        """
        full_url = f"{computed_url or self.BASE_URL}/{url}"

        if data is None:
            data = {}

        if extra_headers:
            headers.update(extra_headers)

        try:
            response = request(
                method, full_url,
                headers=headers, data=data,
                json=json_, params=params,
                timeout=timeout.timeout()
            )
            # header_response = response.headers
            response_data = self.format_response(response)
            status_code = response.status_code
        except (
            req_exceptions.ConnectionError,
            req_exceptions.ConnectTimeout,
        ) as err:
            self.logger.warning(f"Connection error {err}")
            raise_exceptions = False
            status_code = RequestStatusCode.HTTP_500_INTERNAL_SERVER_ERROR
            response_data = {"error": err}
            raise err

        if raise_exceptions:
            _expected_status_code = ExpectedStatusCode.get(method.upper())
            self.raise_appropriate_exception_if_needed(
                response, _expected_status_code
            )

        return status_code, response_data

    def __retrieve_items(self, url: str = "", **kwargs) -> list:
        """
        Handles retrieval of resources, etc
        ** To retrieve by use of params is available etc
        """

        raw_params = kwargs.get("params")
        computed_url = kwargs.get("computed_url")
        params = self._generate_params(
            raw_params
        )
        call_more_responses = True
        _data = []
        while call_more_responses:
            status_code, response_json = self.make_request(url, params=params, computed_url=computed_url)
            if RequestStatusCode.is_successful(status_code):
                if isinstance(response_json, (dict, str)):
                    call_more_responses = False
                    _data = response_json or {}
                elif isinstance(response_json, list):
                    data = response_json or []
                    _data.extend(data)
                    call_more_responses = False
                if not call_more_responses:
                    return _data
            else:
                return []

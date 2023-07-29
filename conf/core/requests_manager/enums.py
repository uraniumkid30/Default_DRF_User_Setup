import re
from dataclasses import dataclass
from typing import Tuple, Union

from conf.core.base_dataclasses import BaseSchema


@dataclass(frozen=True)
class HttpMethods(BaseSchema):
    GET: str = "GET"
    POST: str = "POST"
    PUT: str = "PUT"
    DELETE: str = "DELETE"
    PATCH: str = "PATCH"
    HEAD: str = "HEAD"
    OPTIONS: str = "OPTIONS"
    CONNECT: str = "CONNECT"
    TRACE: str = "TRACE"


@dataclass(frozen=True)
class RequestTimeout(BaseSchema):
    ConnectTimeout: float = 2.0
    ReadTimeout: float = 5.0

    def timeout(self, format="Tuple") -> Union[Tuple[float], float]:
        if format == "Tuple":
            return (self.ConnectTimeout, self.ReadTimeout)
        else:
            return (self.ConnectTimeout + self.ReadTimeout)


@dataclass(frozen=True)
class RequestStatusCode:
    # 1XX series Informational
    HTTP_100_CONTINUE: int = 100
    HTTP_101_SWITCHING_PROTOCOLS: int = 101
    # 2XX serires Successful
    HTTP_200_OK: int = 200
    HTTP_201_CREATED: int = 201
    HTTP_202_ACCEPTED: int = 202
    HTTP_203_NON_AUTHORITATIVE_INFORMATION: int = 203
    HTTP_204_NO_CONTENT: int = 204
    HTTP_205_RESET_CONTENT: int = 205
    HTTP_206_PARTIAL_CONTENT: int = 206
    HTTP_207_MULTI_STATUS: int = 207
    HTTP_208_ALREADY_REPORTED: int = 208
    HTTP_226_IM_USED: int = 226
    # 3XX series Redirection
    HTTP_300_MULTIPLE_CHOICES: int = 300
    HTTP_301_MOVED_PERMANENTLY: int = 301
    HTTP_302_FOUND: int = 302
    HTTP_303_SEE_OTHER: int = 303
    HTTP_304_NOT_MODIFIED: int = 304
    HTTP_305_USE_PROXY: int = 305
    HTTP_306_RESERVED: int = 306
    HTTP_307_TEMPORARY_REDIRECT: int = 307
    HTTP_308_PERMANENT_REDIRECT: int = 308
    # 4XX series ClientError
    HTTP_400_BAD_REQUEST: int = 400
    HTTP_401_UNAUTHORIZED: int = 401
    HTTP_402_PAYMENT_REQUIRED: int = 402
    HTTP_403_FORBIDDEN: int = 403
    HTTP_404_NOT_FOUND: int = 404
    HTTP_405_METHOD_NOT_ALLOWED: int = 405
    HTTP_406_NOT_ACCEPTABLE: int = 406
    HTTP_407_PROXY_AUTHENTICATION_REQUIRED: int = 407
    HTTP_408_REQUEST_TIMEOUT: int = 408
    HTTP_409_CONFLICT: int = 409
    HTTP_410_GONE: int = 410
    HTTP_411_LENGTH_REQUIRED: int = 411
    HTTP_412_PRECONDITION_FAILED: int = 412
    HTTP_413_REQUEST_ENTITY_TOO_LARGE: int = 413
    HTTP_414_REQUEST_URI_TOO_LONG: int = 414
    HTTP_415_UNSUPPORTED_MEDIA_TYPE: int = 415
    HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE: int = 416
    HTTP_417_EXPECTATION_FAILED: int = 417
    HTTP_422_UNPROCESSABLE_ENTITY: int = 422
    HTTP_423_LOCKED: int = 423
    HTTP_424_FAILED_DEPENDENCY: int = 424
    HTTP_426_UPGRADE_REQUIRED: int = 426
    HTTP_428_PRECONDITION_REQUIRED: int = 428
    HTTP_429_TOO_MANY_REQUESTS: int = 429
    HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE: int = 431
    HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS: int = 451
    # 5XX series ServerError
    HTTP_500_INTERNAL_SERVER_ERROR: int = 500
    HTTP_501_NOT_IMPLEMENTED: int = 501
    HTTP_502_BAD_GATEWAY: int = 502
    HTTP_503_SERVICE_UNAVAILABLE: int = 503
    HTTP_504_GATEWAY_TIMEOUT: int = 504
    HTTP_505_HTTP_VERSION_NOT_SUPPORTED: int = 505
    HTTP_506_VARIANT_ALSO_NEGOTIATES: int = 506
    HTTP_507_INSUFFICIENT_STORAGE: int = 507
    HTTP_508_LOOP_DETECTED: int = 508
    HTTP_509_BANDWIDTH_LIMIT_EXCEEDED: int = 509
    HTTP_510_NOT_EXTENDED: int = 510
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED: int = 511

    @staticmethod
    def is_status_code_a_match(series: str, status_code: int) -> bool:
        """
        Checks if the status code is in a particular series
        """
        if re.match(series, str(status_code)):
            return True
        return False
    
    @classmethod
    def is_informational(cls, status_code: int) -> bool:  # 1xx
        series = "1[0-9]{2}$"
        return cls.is_status_code_a_match(series, status_code)

    @classmethod
    def is_successful(cls, status_code: int) -> bool:  # 2xx
        series = "2[0-9]{2}$"
        return cls.is_status_code_a_match(series, status_code)

    @classmethod
    def is_redirect(cls, status_code: int) -> bool:  # 3xx
        series = "3[0-9]{2}$"
        return cls.is_status_code_a_match(series, status_code)

    @classmethod
    def is_client_error(cls, status_code: int) -> bool:  # 4xx
        series = "4[0-9]{2}$"
        return cls.is_status_code_a_match(series, status_code)

    @classmethod
    def is_server_error(cls, status_code: int) -> bool:  # 5xx
        series = "5[0-9]{2}$"
        return cls.is_status_code_a_match(series, status_code)


@dataclass(frozen=True)
class ExpectedStatusCode:
    GET: Tuple[int] = (RequestStatusCode.HTTP_200_OK,)
    POST: Tuple[int] = (
        RequestStatusCode.HTTP_201_CREATED,
        RequestStatusCode.HTTP_206_PARTIAL_CONTENT,
    )
    PUT: Tuple[int] = (
        RequestStatusCode.HTTP_200_OK,
        RequestStatusCode.HTTP_204_NO_CONTENT,
    )
    DELETE: Tuple[int] = (
        RequestStatusCode.HTTP_200_OK,
        RequestStatusCode.HTTP_202_ACCEPTED,
        RequestStatusCode.HTTP_204_NO_CONTENT,
    )
    PATCH: Tuple[int] = (
        RequestStatusCode.HTTP_200_OK,
        RequestStatusCode.HTTP_204_NO_CONTENT,
    )
    HEAD: Tuple[int] = (RequestStatusCode.HTTP_200_OK,)
    OPTIONS: Tuple[int] = (RequestStatusCode.HTTP_200_OK,)
    CONNECT: Tuple[int] = (RequestStatusCode.HTTP_200_OK,)
    TRACE: Tuple[int] = (RequestStatusCode.HTTP_200_OK,)

class BaseException(Exception):
    pass


class BadRequestException(BaseException):
    pass


class AppNotFoundException(BaseException):
    pass


class NotFoundException(BaseException):
    pass


class UnExpectedStatusCode(BaseException):
    pass


class TooManyRequests(BaseException):
    pass


class UnauthorizedException(BaseException):
    pass


class ForbiddenException(BaseException):
    pass


class InternalServerErrorException(BaseException):
    pass
